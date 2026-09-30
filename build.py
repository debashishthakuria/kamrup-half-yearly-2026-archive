"""Generate the 2026 Kamrup half-yearly subject archive."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
BASE = 'https://debashishthakuria.github.io/'
SUBJECTS = [
    dict(slug='english', name='English', group='Language', phase='finished', material='working'),
    dict(slug='alternative-english', name='Alternative English', group='MIL', phase='finished', material='available', links=[
        ('Open the full Alternative English revision site', 'alte/index.html'),
        ('Read the 2026 paper and suggested answers', 'alte/question-paper.html'),
        ('Read the post-exam guide audit', 'alte/paper-report.html'),
    ]),
    dict(slug='assamese', name='Assamese', group='MIL', phase='finished', material='working'),
    dict(slug='mathematics', name='Mathematics', group='Elective', phase='upcoming', material='soon'),
    dict(slug='physics', name='Physics', group='Elective', phase='finished', material='available', links=[
        ('Read the actual paper, worked answers and analysis', 'physics-paper-2026.html'),
        ('Download the supplied eight-page question paper', 'physics-paper-2026.pdf'),
        ('Open the full Physics revision guide', 'physics/physics.html'),
        ('Browse chapter-wise derivations', 'physics/physics-derivations.html'),
        ('Review formulas and practice', 'physics/physics-formulas.html'),
    ]),
    dict(slug='chemistry', name='Chemistry', group='Elective', phase='finished', material='working'),
    dict(slug='biology', name='Biology', group='Elective', phase='upcoming', material='soon'),
    dict(slug='computer-science', name='Computer Science', group='Elective', phase='upcoming', material='soon'),
    dict(slug='general-studies', name='General Studies', group='Compulsory', phase='finished', material='available', links=[
        ('Open the full General Studies study book', BASE+'gshy/#overview'),
        ('Chapter 1 · Our Northeast, Our Neighbourhood', BASE+'gshy/#ch1'),
        ('Chapter 2 · Inculcation of Scientific Temper', BASE+'gshy/#ch2'),
        ('Chapter 3 · Cultural Heritage', BASE+'gshy/#ch3'),
        ('Chapter 4 · Importance of CCA', BASE+'gshy/#ch4'),
        ('Chapter 5 · Indian Knowledge System', BASE+'gshy/#ch5'),
        ('Rapid Revision', BASE+'gshy/#rapid'),
        ('Exam Plan', BASE+'gshy/#plan'),
    ]),
]

# Material status and exam status are independent: a completed paper may still lack an archive.
LABELS = {'available':'Materials available','working':'Working on it','soon':'Coming soon'}
PHASES = {'finished':'Exam finished','upcoming':'Exam yet to be held','unspecified':'Exam status not confirmed'}

def nav(current=''):
    items = ''.join('<a href="'+s['slug']+'.html"'+(' aria-current="page"' if s['slug']==current else '')+'>'+escape(s['name'])+'</a>' for s in SUBJECTS)
    return '<nav class="subject-nav" aria-label="Subject tabs">'+items+'</nav>'

def layout(title, content, current=''):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#f7f3ed"><meta name="description" content="Kamrup district half-yearly exam subject archive, study resources and post-exam reviews."><title>'+escape(title)+' · Kamrup Half-Yearly 2026</title><link rel="stylesheet" href="style.css"></head><body><header class="site-head"><div class="wrap head-row"><a class="logo" href="index.html"><span>Half-Yearly <small>Kamrup · 2026</small></span></a><span class="head-meta">HS second year / subject archive</span></div></header><div class="wrap">'+nav(current)+'<main>'+content+'</main><footer><span>Kamrup district · HS second year · 2026</span><span>Revision materials are unofficial. Paper analysis follows the actual paper when available.</span></footer></div></body></html>'

def status(s):
    return '<div class="badges"><span class="badge '+s['phase']+'">'+PHASES[s['phase']]+'</span><span class="badge '+s['material']+'">'+LABELS[s['material']]+'</span></div>'

def card(s):
    description = {'available':'Study resources and available review links.', 'working':'No subject preparation or post-exam review has been published here yet.', 'soon':'This exam is still ahead. Resources will be added later.'}[s['material']]
    if s['slug']=='physics': description='The supplied paper, worked answers and analysis are ready alongside the revision guide.'
    if s['slug']=='general-studies': description='Preparation notes are available. A post-exam analysis is not published here yet.'
    if s['slug']=='assamese': description='The Assamese MIL exam is finished. Preparation and post-exam review are still being prepared.'
    return '<a class="subject-card" href="'+s['slug']+'.html"><span class="overline">'+escape(s['group'])+'</span><h3>'+escape(s['name'])+' <span aria-hidden="true">↗</span></h3>'+status(s)+'<p>'+escape(description)+'</p></a>'

home = '<section class="hero"><p class="eyebrow">A subject-by-subject record · 2026</p><h1>One place for the<br><em>half-yearly record.</em></h1><p class="lead">Preparation, papers and post-exam reviews for the Kamrup district HS second-year half-yearly exams. We’ll add each paper only when it is available.</p><div class="hero-stats"><span><strong>6</strong> papers reported finished</span><span><strong>3</strong> exams still ahead</span><span><strong>3</strong> subjects with study materials</span></div></section>'
home += '<section class="intro"><div><p class="eyebrow">Browse the archive</p><h2>Subjects, without the noise.</h2></div><p>Two statuses appear on each subject: whether the exam has happened, and whether materials are published. “Working on it” means the exam may be finished but the archive is not ready.</p></section>'
home += '<section class="group"><div class="group-head"><span class="group-count">01 / 04</span><h2>Languages</h2><p>English and the two MIL options.</p></div><div class="card-grid">'+''.join(card(s) for s in SUBJECTS if s['group'] in ('Language','MIL'))+'</div></section>'
home += '<section class="group"><div class="group-head"><span class="group-count">02 / 04</span><h2>Main electives</h2><p>Mathematics, Physics, Chemistry and Biology.</p></div><div class="card-grid">'+''.join(card(s) for s in SUBJECTS if s['group']=='Elective' and s['slug']!='computer-science')+'</div></section>'
home += '<section class="group"><div class="group-head"><span class="group-count">03 / 04</span><h2>Additional elective</h2><p>Computer Science.</p></div><div class="card-grid">'+card(next(s for s in SUBJECTS if s['slug']=='computer-science'))+'</div></section>'
home += '<section class="group"><div class="group-head"><span class="group-count">04 / 04</span><h2>Compulsory</h2><p>General Studies.</p></div><div class="card-grid">'+card(next(s for s in SUBJECTS if s['slug']=='general-studies'))+'</div></section>'
home += '<aside class="note"><strong>What’s not here yet?</strong> The Physics paper and worked review are now available. Subjects marked “Working on it” do not have a new paper review here. This is a student study archive, not an official district results portal.</aside>'
(ROOT/'index.html').write_text(layout('Overview',home),encoding='utf8')

for s in SUBJECTS:
    phase = PHASES[s['phase']]
    content = '<div class="crumb"><a href="index.html">All subjects</a> / '+escape(s['group'])+'</div><section class="subject-hero"><p class="eyebrow">'+escape(s['group'])+' · Kamrup half-yearly 2026</p><h1>'+escape(s['name'])+'</h1>'+status(s)+'</section>'
    if s['material']=='available':
        content += '<section class="resource-block"><p class="eyebrow">Resources</p><h2>What’s available</h2><div class="resource-list">'+''.join('<a href="'+escape(url,quote=True)+'"'+(' target="_blank" rel="noopener noreferrer"' if url.startswith('https://') else '')+'><span>'+escape(label)+'</span><span aria-hidden="true">↗</span></a>' for label,url in s['links'])+'</div></section>'
        if s['slug']=='physics': content += '<section class="empty-block"><p class="eyebrow">Post-exam record</p><h2>Paper and worked review available.</h2><p>The eight-page question paper, worked answers for every printed option, and a paper-level analysis are now included in this archive. The diagrams have been reconstructed from the supplied text for your review. This is not an official marking scheme.</p></section>'
        elif s['slug']=='general-studies': content += '<section class="empty-block"><p class="eyebrow">Post-exam record</p><h2>Paper and analysis pending.</h2><p>The General Studies paper has not been shared yet. When it arrives, the questions and post-exam review can be added here; the linked study book is preparation material, not a paper analysis.</p></section>'
        else: content += '<section class="empty-block"><p class="eyebrow">Post-exam record</p><h2>Paper review available.</h2><p>The Alternative English pages in this archive include the supplied paper, suggested answers and a guide audit. It is unofficial.</p></section>'
    else:
        heading = 'Coming Soon' if s['material']=='soon' else 'Working on it'
        text = 'The exam is still ahead. This page will hold its preparation and, later, the actual paper and review.' if s['material']=='soon' else 'The exam is finished, but preparation materials and post-exam analytics have not been published for this subject.'
        if s['slug']=='assamese': text='The Assamese MIL exam is finished. Preparation materials and post-exam analytics have not been published for this subject yet; no paper or analysis is shown.'
        content += '<section class="empty-block"><div class="empty-symbol" aria-hidden="true">'+('↗' if s['material']=='soon' else '…')+'</div><h2>'+heading+'</h2><p>'+text+'</p></section>'
    content += '<a class="back" href="index.html">← Back to all subjects</a>'
    (ROOT/(s['slug']+'.html')).write_text(layout(s['name'],content,s['slug']),encoding='utf8')
print('generated',len(SUBJECTS),'subject pages and home')
