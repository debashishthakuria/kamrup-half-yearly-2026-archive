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
        self.assertIn('The actual Physics paper will be added',p)
        self.assertIn('alte/question-paper.html',(ROOT/'alternative-english.html').read_text(encoding='utf8'))
        self.assertTrue((ROOT/'alte/question-paper.html').is_file())

if __name__=='__main__': unittest.main()
