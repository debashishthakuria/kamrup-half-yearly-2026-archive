import unittest
from pathlib import Path
from html.parser import HTMLParser
from build import ROOT, SUBJECTS, LABELS, PHASES

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.tabs=[]; self.headings=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='a': self.links.append(attrs.get('href',''))
        if tag=='nav' and attrs.get('aria-label')=='Subject tabs': self.tabs.append(tag)

class ArchiveTests(unittest.TestCase):
    def test_each_subject_has_own_page_and_correct_status(self):
        self.assertEqual(len(SUBJECTS),9)
        self.assertEqual(sum(s['phase']=='finished' for s in SUBJECTS),6)
        self.assertEqual(sum(s['phase']=='upcoming' for s in SUBJECTS),3)
        for s in SUBJECTS:
            with self.subTest(s=s['slug']):
                page=(ROOT/(s['slug']+'.html')).read_text(encoding='utf8')
                self.assertIn(LABELS[s['material']],page)
                self.assertIn(PHASES[s['phase']],page)
                self.assertIn('aria-current="page"',page)
                if s['material']=='soon': self.assertIn('<h2>Coming Soon</h2>',page)
                if s['material']=='working': self.assertIn('<h2>Working on it</h2>',page)
                if s['material']=='available': self.assertIn('class="resource-list"',page)
    def test_navigation_and_external_links(self):
        pages=[ROOT/'index.html']+[ROOT/(s['slug']+'.html') for s in SUBJECTS]
        for page in pages:
            with self.subTest(page=page.name):
                parser=Links(); parser.feed(page.read_text(encoding='utf8'))
                for s in SUBJECTS: self.assertIn(s['slug']+'.html',parser.links)
                for href in parser.links:
                    if '://' not in href and not href.startswith('#'):
                        self.assertTrue((ROOT/href.split('#')[0]).is_file(),(page.name,href))
    def test_general_studies_chapters_are_extracted_from_existing_site(self):
        page=(ROOT/'general-studies.html').read_text(encoding='utf8')
        source='https://debashishthakuria.github.io/gshy/'
        for anchor,title in [
            ('ch1','Our Northeast, Our Neighbourhood'),
            ('ch2','Inculcation of Scientific Temper'),
            ('ch3','Cultural Heritage'),
            ('ch4','Importance of CCA'),
            ('ch5','Indian Knowledge System'),
            ('rapid','Rapid Revision'),
            ('plan','Exam Plan'),
        ]:
            with self.subTest(anchor=anchor):
                self.assertIn(title,page)
                self.assertIn(source+'#'+anchor,page)
        self.assertIn(source+'#overview',page)
        self.assertIn('The General Studies paper has not been shared',page)
        self.assertNotIn('suggested answers',page.lower())

    def test_physics_and_alternative_english_use_local_full_guides(self):
        expected = {
            'physics': ['physics.html','physics-derivations.html','physics-electric-charges-fields.html','physics-potential-capacitance.html','physics-current-electricity.html','physics-moving-charges-magnetism.html','physics-magnetism-matter.html','physics-electromagnetic-induction.html'],
            'alte': ['index.html','question-paper.html','paper-report.html','chapters.html','grammar.html','writing.html','essays.html','a-cup-of-tea.html'],
        }
        for subject, guide in [('physics','physics'),('alternative-english','alte')]:
            page=(ROOT/(subject+'.html')).read_text(encoding='utf8')
            self.assertIn(f'{guide}/',page)
            self.assertNotIn('href="https://debashishthakuria.github.io/'+('asseb-half-yearly-study-plan-2026/' if subject=='physics' else 'alte-harmony-revision/'), page)
        for folder, pages in expected.items():
            for filename in pages:
                with self.subTest(folder=folder,filename=filename):
                    self.assertTrue((ROOT/folder/filename).is_file())
                    self.assertIn('href="../index.html"',(ROOT/folder/filename).read_text(encoding='utf8'))

    def test_physics_paper_has_all_questions_or_options_and_diagrams(self):
        page=(ROOT/'physics-paper-2026.html').read_text(encoding='utf8')
        for q,n in [(1,6),(2,9),(3,6),(4,3)]:
            for letter in 'abcdefghi'[:n]:
                with self.subTest(question=f'{q}{letter}'):
                    self.assertIn(f'id="q{q}{letter}"',page)
        for q in ['q3a','q3b','q3c','q3d','q3e','q3f','q4a','q4b','q4c']:
            self.assertIn(f'id="{q}-or"',page)
        for graphic in ('wheatstone.svg','shell-field.svg','capacitor-network.svg','resistor-network.svg'):
            self.assertIn('diagrams/'+graphic,page)
            self.assertTrue((ROOT/'diagrams'/graphic).is_file())
        self.assertIn('8 pages',page)
        self.assertIn('The original PDF uses diagram placeholders',page)
        self.assertIn('Paper analysis',page)
        self.assertIn('2.5 × 10',page)
        self.assertIn('40/3',page)
        self.assertIn('120 V',page)
        self.assertIn('18 J',page)
        self.assertIn('750 V',page)
        self.assertIn('Do not treat this as an official mark scheme',page)
        self.assertIn('physics-paper-2026.html',(ROOT/'physics.html').read_text(encoding='utf8'))
        self.assertIn('The Physics paper and worked review are now available',(ROOT/'index.html').read_text(encoding='utf8'))

    def test_every_physics_paper_page_has_existing_local_assets(self):
        import re
        page=ROOT/'physics-paper-2026.html'
        parser=Links(); parser.feed(page.read_text(encoding='utf8'))
        refs=parser.links + re.findall(r'(?:src|href)=["\']([^"\']+)',page.read_text(encoding='utf8'))
        for href in refs:
            if href.startswith(('http:','https:','#','mailto:','data:')): continue
            with self.subTest(href=href):
                self.assertTrue((ROOT/href.split('#')[0]).is_file())

    def test_answer_math_is_prerendered_with_local_fonts(self):
        from html.parser import HTMLParser
        class MathProbe(HTMLParser):
            def __init__(self):
                super().__init__(); self.in_answer=False; self.answers=[]; self.depth=0
            def handle_starttag(self,tag,attrs):
                if tag=='div' and ('class','answer') in attrs:
                    self.in_answer=True; self.depth=1; self.answers.append(0)
                elif self.in_answer:
                    if tag=='div': self.depth+=1
                    if tag=='math': self.answers[-1]+=1
            def handle_endtag(self,tag):
                if self.in_answer and tag=='div':
                    self.depth-=1
                    if not self.depth:self.in_answer=False
        page=(ROOT/'physics-paper-2026.html').read_text(encoding='utf8')
        probe=MathProbe();probe.feed(page)
        self.assertGreaterEqual(sum(probe.answers),60)
        self.assertEqual(len(probe.answers),33)
        self.assertIn('physics/katex-fonts.css',page)
        self.assertIn('physics/katex.min.css',page)
        self.assertTrue((ROOT/'physics/katex.min.css').is_file())
        self.assertIn('class="katex"',page)

    def test_paper_transcription_matches_source_pages_and_solutions(self):
        import pymupdf
        from build_physics_paper import SOURCE, Q1, Q2, Q3, Q4
        doc=pymupdf.open(SOURCE)
        self.assertEqual(len(doc),8)
        self.assertEqual([len(g) for g in (Q1,Q2,Q3,Q4)],[6,9,6,3])
        self.assertEqual(sum(alt is not None for *_,alt in Q3+Q4),9)
        self.assertIn('DIAGRAM PLACEHOLDER',doc[6].get_text())
        self.assertIn('DIAGRAM PLACEHOLDER',doc[7].get_text())
        self.assertIn('Or /',doc[7].get_text())
        self.assertIn('wheatstone bridge',doc[3].get_text().lower())
        self.assertIn('4 × 10−3',doc[6].get_text())

    def test_math_source_covers_every_complex_answer(self):
        import json
        math=json.loads((ROOT/'paper-math.json').read_text(encoding='utf8'))
        for q in ('q2g','q3a','q3a-or','q3b-or','q3c','q3c-or','q3d-or','q3e','q3f','q4a','q4a-or','q4b-or','q4c','q4c-or'):
            with self.subTest(question=q):self.assertTrue(math.get(q))
        self.assertIn('\\frac{V(R_2+R_3)}',math['q4c-or'][-1])
        self.assertIn('\\tfrac{40}3',math['q4c'][1])

    def test_archive_header_has_no_logo(self):
        for page in [ROOT/'index.html']+[ROOT/(s['slug']+'.html') for s in SUBJECTS]:
            with self.subTest(page=page.name):
                text=page.read_text(encoding='utf8')
                self.assertNotIn('class="mark"',text)
                self.assertIn('Half-Yearly <small>Kamrup · 2026</small>',text)

    def test_assamese_mil_exam_is_finished_without_invented_materials(self):
        page=(ROOT/'assamese.html').read_text(encoding='utf8')
        self.assertIn('Exam finished',page)
        self.assertIn('<h2>Working on it</h2>',page)
        self.assertNotIn('Exam status not confirmed',page)
        self.assertEqual(sum(s['phase']=='finished' for s in SUBJECTS),6)

    def test_all_mirrored_local_links_and_assets_exist(self):
        import re
        for folder in ('physics','alte'):
            for page in (ROOT/folder).glob('*.html'):
                with self.subTest(page=page.name,folder=folder):
                    parser=Links(); parser.feed(page.read_text(encoding='utf8'))
                    paths=parser.links
                    paths += re.findall(r'(?:src|href)=["\']([^"\']+)',page.read_text(encoding='utf8'))
                    for href in paths:
                        href=href.split('#')[0].split('?')[0]
                        if not href or href.startswith(('http:','https:','mailto:','tel:','data:','javascript:','//')): continue
                        self.assertTrue((page.parent/href).is_file(),(page.name,href))

    def test_paper_pending_and_alternative_paper_real_route(self):
        p=(ROOT/'physics.html').read_text(encoding='utf8')
        self.assertIn('Paper and worked review available',p)
        self.assertIn('physics-paper-2026.html',p)
        self.assertIn('alte/question-paper.html',(ROOT/'alternative-english.html').read_text(encoding='utf8'))
        self.assertTrue((ROOT/'alte/question-paper.html').is_file())

if __name__=='__main__': unittest.main()
