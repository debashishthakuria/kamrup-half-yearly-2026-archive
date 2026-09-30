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
        self.assertEqual(sum(s['phase']=='finished' for s in SUBJECTS),5)
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
    def test_paper_pending_and_alternative_paper_real_route(self):
        p=(ROOT/'physics.html').read_text(encoding='utf8')
        self.assertIn('The actual Physics paper will be added',p)
        self.assertIn('question-paper.html',(ROOT/'alternative-english.html').read_text(encoding='utf8'))
        self.assertNotIn('paper.html"',(ROOT/'alternative-english.html').read_text(encoding='utf8').replace('question-paper.html"',''))

if __name__=='__main__': unittest.main()
