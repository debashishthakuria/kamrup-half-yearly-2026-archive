"""Build the English syllabus guide from the supplied Flamingo/Vistas and 2026 paper."""
from html import escape
from build import ROOT, layout

# PDF page numbers below are 1-based PDF pages, not printed textbook pages.
CHAPTERS = [
 ('lost-spring','Lost Spring','Flamingo',22,30,'Anees Jung','Saheb-e-Alam searches Seemapuri rubbish for survival; Mukesh of Firozabad hopes to break from his family’s bangle-making work and become a motor mechanic.',[
 ('Where did Saheb’s family come from, and why?','They came from Dhaka in Bangladesh; storms had swept away their home and fields.'),
 ('Why is Saheb’s name ironic?','Saheb-e-Alam means “lord of the universe”, but he is a poor child who searches garbage for a living.'),
 ('What changes when Saheb takes a tea-stall job?','He earns 800 rupees and meals, but loses the freedom he had as a ragpicker; the canister belongs to the owner.'),
 ('What does Mukesh want to become?','A motor mechanic. His ambition contrasts with his family’s inherited bangle-making trade.'),
 ('What does garbage mean to adults and children?','To adults it is survival; to children it can also hold wonder and the hope of finding a coin.')]),
 ('indigo','Indigo','Flamingo',55,64,'Louis Fischer','Rajkumar Shukla brings Gandhi to Champaran, where indigo sharecroppers face unjust conditions. Legal resistance, an inquiry and local social work turn fear into collective action.',[
 ('Why was Gandhi at Lucknow in 1916?','For the Indian National Congress convention, where Shukla approached him.'),
 ('How did Shukla convince Gandhi to go to Champaran?','He followed Gandhi persistently and waited for him at their agreed meeting in Calcutta.'),
 ('Where did Gandhi and Shukla travel together by train?','To Patna, before Gandhi went towards Muzaffarpur and Champaran.'),
 ('Why did the lawyers agree to stay?','Gandhi asked what would happen to the peasants if he went to jail. They felt it would be shameful to abandon the peasants while an outsider risked imprisonment.'),
 ('Why did Gandhi accept only a partial refund?','The amount mattered less than making the landlords surrender some power and restoring the peasants’ confidence.')]),
 ('memoirs','Memoirs of a Chota Sahib','Flamingo',98,104,'John Rowntree','A forest officer recalls the Brahmaputra, Peacock Island, contrasting north and south banks, monsoon journeys and forest bungalows around pre-Independence Guwahati.',[
 ('Who is the Chota Sahib?','John Rowntree, the author and former British Senior Conservator of Forests of Assam.'),
 ('What was visible from his bungalow veranda?','The Brahmaputra and river traffic, the Himalayas beyond it, and Peacock Island in the foreground.'),
 ('What does the account say about Manas?','Manas Sanctuary bordered Bhutan and had a few rhinoceroses. Nearby rivers held mahseer, a freshwater fish.'),
 ('What was a mar boat?','A river ferry: a plank platform over two side-by-side boats, paddled or driven by the current along a cable.'),
 ('Why was Kulsi the author’s favourite bungalow?','It was pleasantly situated above the river and surrounded by teak plantations, with a rubber plantation nearby.')]),
 ('going-places','Going Places','Flamingo',86,96,'A. R. Barton','Sophie fantasises about glamorous work and meeting footballer Danny Casey. Her friend Jansie sees the family’s economic limits, while Geoff becomes a confidant for her imagined world.',[
 ('What work did Jansie expect for herself and Sophie?','Jobs at the biscuit factory after school.'),
 ('What careers did Sophie imagine?','Running a boutique, managing a shop, acting and fashion design.'),
 ('Why does Sophie confide in Geoff?','His quiet, seemingly wider world fascinates her; she hopes to share the world beyond their neighbourhood.'),
 ('Did Danny Casey meet Sophie by the canal?','No. She waits for him, but nobody comes; the story frames their supposed earlier encounter as her fantasy.'),
 ('What does the contrast between Sophie and Jansie show?','Sophie is an imaginative dreamer; Jansie is practical about money and their likely jobs.')]),
 ('my-mother','My Mother at Sixty-Six','Flamingo',107,108,'Kamala Das','A drive to Cochin airport makes the speaker confront her ageing mother and her old fear of separation. Energetic trees and children contrast with the mother’s frailty.',[
 ('What does the speaker notice about her mother in the car?','She is dozing with her mouth open; her face appears pale and ashen.'),
 ('Why are the young trees and merry children significant?','They evoke movement and youth, contrasting with her mother’s age and stillness.'),
 ('What is the childhood fear?','Fear of losing her mother and being separated from her.'),
 ('Why does the speaker smile at parting?','She masks her anxiety and tries to reassure herself and her mother with a hopeful farewell.')]),
 ('keeping-quiet','Keeping Quiet','Flamingo',112,114,'Pablo Neruda','Neruda proposes a brief pause in speech and action for shared reflection, non-violence and self-understanding; he explicitly rejects death and permanent inactivity.',[
 ('Why does he ask everyone to count to twelve?','To create a brief shared pause for silence and reflection.'),
 ('Does the poet advocate permanent inactivity?','No. He distinguishes his momentary stillness from death and total inactivity.'),
 ('What is the sadness in the poem?','People fail to understand themselves and threaten themselves through destructive actions.'),
 ('What does the Earth teach?','Apparent stillness can conceal renewal and continuing life.')]),
 ('roadside-stand','A Roadside Stand','Flamingo',117,119,'Robert Frost','A roadside seller hopes passing city traffic will buy farm produce. Instead, motorists ignore the stand, object to its signs or stop for other reasons; the poem criticises unequal access to prosperity.',[
 ('What do the sellers hope to obtain?','Some city money from customers buying their produce, not charity.'),
 ('What is their childish longing?','To hear a vehicle stop and have a traveller ask the price of their goods; it is usually disappointed.'),
 ('How do motorists react?','Most pass by. Some dislike the signs, and those who stop may ask for directions, fuel or room to turn around instead of buying.'),
 ('What does the poet criticise in the promised help?','Powerful benefactors claim to help the rural poor but take away independence and do not meet their real needs.')]),
 ('tiger-king','The Tiger King','Vistas',9,14,'Kalki','A ruler hunts tigers to evade a prediction that a tiger will cause his death. The hundredth animal survives his shot; later an infected splinter from a wooden toy tiger kills him.',[
 ('What prediction was made at his birth?','He would die because of a tiger; later the astrologer warned especially of the hundredth tiger.'),
 ('How many tigers had he killed before searching for the last one?','Ninety-nine. The hundredth survived his shot and was killed by hunters afterwards.'),
 ('Why did he marry a princess from another state?','Her state had many tigers, giving him more opportunities to hunt after those in his own state ran out.'),
 ('How did he die?','A splinter from a wooden toy tiger pierced his hand, became infected, and the king died after an operation.')]),
 ('memories','Memories of Childhood','Vistas',52,55,'Zitkala-Sa and Bama','Two autobiographical accounts show children confronting oppression: Zitkala-Sa resists the forced cutting of her hair at school; Bama learns why an elder must carry food without touching it and resolves to study hard.',[
 ('Why does Zitkala-Sa resist the haircut?','In her culture short or shingled hair carried shame; she resists having it forced upon her.'),
 ('Who warned her about the haircut?','Her friend Judewin, who understood a little English.'),
 ('Why did the elder hold the food packet by its string?','Caste prejudice forbade him from touching the food intended for the landlord.'),
 ('What advice does Bama’s brother give her?','Study diligently and progress so that others cannot so easily deny her dignity.'),
 ('What unites the two accounts?','Both show children recognising and resisting different forms of discrimination.')]),
]
GRAMMAR = [
 ('tense','Tense','Choose a verb form using the time marker and sequence of events; a continuing state from a past point may take the present perfect or present perfect continuous.',[
 ('By the time the bus arrived, we ___ (wait) for an hour.','had been waiting','An ongoing past action preceded another past event.'),
 ('The girl ___ (read) now; please keep quiet.','is reading','“Now” points to an action in progress.'),
 ('I ___ (know) my friend since 2017.','have known','A state begun in the past and continuing now; “know” is normally not progressive.'),
 ('If I ___ (be) you, I would revise the poems.','were','Hypothetical condition: “If I were you”.')]),
 ('voice','Voice','Keep tense and meaning; make the active object the passive subject. Retain necessary prepositions such as “at”.',[
 ('The committee has announced the winners. (Passive)','The winners have been announced by the committee.','Present perfect passive: have/has been + past participle.'),
 ('They laughed at the speaker. (Passive)','The speaker was laughed at by them.','Keep the preposition “at”.'),
 ('The letter was written by Rima. (Active)','Rima wrote the letter.','Past passive becomes simple past active.'),
 ('Close the gate. (Passive)','Let the gate be closed.','Passive form of an imperative.')]),
 ('narration','Narration','Reported statements and questions change pronouns and, when a past reporting verb requires it, often backshift tense. Commands use “told/asked + object + to”.',[
 ('Rina said, “I am preparing a poster.” (Indirect)','Rina said that she was preparing a poster.','Past reporting verb; am preparing → was preparing.'),
 ('He said to me, “Where do you live?” (Indirect)','He asked me where I lived.','Use statement word order in the reported question.'),
 ('The teacher said, “Do not waste paper.” (Indirect)','The teacher told us not to waste paper.','Negative instruction: told + object + not to.'),
 ('She said that she had finished her work. (Direct)','She said, “I have finished my work.”','One valid reconstruction; exact original wording cannot be recovered.')]),
 ('preposition','Preposition','Learn phrases in context: interested in, pride in, superior to, responsible for, insist on.',[
 ('He takes pride ___ his work.','in','“Take pride in” is the fixed phrase.'),
 ('She is interested ___ history.','in','“Interested in” is the fixed phrase.'),
 ('The team insisted ___ an explanation.','on','“Insist on” takes on.'),
 ('We are responsible ___ the library books.','for','“Responsible for” is the fixed phrase.'),
 ('This route is superior ___ the older one.','to','“Superior to,” not “superior than”.')]),
 ('transformation','Transformation of sentences','Change the structure without changing meaning; more than one answer can be valid.',[
 ('He was too tired to continue. (Use “so … that”)','He was so tired that he could not continue.','Too … to corresponds to so … that + cannot/could not.'),
 ('Although it rained, they played. (Use “despite”)','Despite the rain, they played.','Despite needs a noun phrase or -ing form.'),
 ('As soon as she arrived, the programme began. (Use “no sooner”)','No sooner had she arrived than the programme began.','No sooner + had + subject + past participle + than.'),
 ('Only Rima can solve this problem. (Begin “No one”)','No one except Rima can solve this problem.','Exclusive meaning preserved.')]),
]
WRITING = [
 ('notice','Notice','Give the institution/issuing authority, NOTICE, date, specific heading, essential what/when/where/how and name/designation. Follow the question’s word limit.', 'Your literary club is collecting student poems for its annual magazine. Draft a notice in about 50 words.', 'HILL VIEW SCHOOL · NOTICE<br>12 August 2026<br><strong>Poems for the School Magazine</strong><p>Original poems by students are invited for the annual magazine. Submit a typed copy with your name and class to the library desk by 22 August. Selected entries will be edited for publication. For queries, contact the undersigned.</p>Rina Das<br>Literary Club Secretary'),
 ('poster','Poster','Use a large headline, a memorable call to action, two or three actionable points and an issuer/contact. Keep copy short and readable.', 'Make a poster encouraging students to save paper.', '<strong>SAVE PAPER. KEEP TREES STANDING.</strong><p>Print only what you need · Use both sides · Recycle clean paper</p><p>Bring old notebooks to the collection box outside the library every Friday.</p>Green Club, Hill View School'),
 ('advertisement','Advertisement','For a classified ad, use a category headline, concise description, relevant location, contact and any necessary identification. Do not publish sensitive document numbers.', 'You have lost a blue folder between Guwahati and Nalbari. Draft a classified ad in under 50 words.', '<strong>LOST DOCUMENTS</strong><p>Blue file folder lost while travelling from Guwahati to Nalbari on 10 August 2026. Contains academic certificates and notes. Finder may contact Rina at 9XXXXXXXXX. Reward offered. Please do not misuse the documents.</p>'),
 ('letter','Letter to the editor','Use sender address, date, recipient, subject, salutation, a factual problem and a clear request, followed by a suitable closing and signature.', 'Write to the editor about unsafe pedestrian crossings near schools.', '12, Station Road<br>Guwahati, Assam<br>12 August 2026<br><br>The Editor<br>The Assam Tribune<br>Guwahati<br><br><strong>Subject: Safer crossings near schools</strong><p>Sir/Madam,</p><p>Through your newspaper, I wish to draw attention to unsafe crossings near schools. Heavy traffic during arrival and dispersal puts children at risk, especially where signs and pedestrian markings are missing.</p><p>I request the traffic authorities to mark crossings clearly, enforce speed limits and arrange safe crossing support at peak hours.</p><p>Yours faithfully,<br>Rina Das</p>'),
]

def source_link(book, start, end):
    return f'{book}, supplied textbook PDF pp. {start}–{end} (page numbers counted from first PDF page)'

def answer_card(q,a,why=''):
    return '<details class="ep-question"><summary>'+escape(q)+'</summary><div class="ep-answer"><strong>Suggested answer</strong><p>'+escape(a)+'</p>'+('<small>'+escape(why)+'</small>' if why else '')+'</div></details>'

def build():
    style = '''<style>.ep-index{display:flex;gap:8px;flex-wrap:wrap;margin:24px 0 38px}.ep-index a{padding:9px 13px;border:1px solid #d9d0c5;background:white;border-radius:30px;color:#3a3834;text-decoration:none;font-size:14px}.ep-index a:hover,.ep-index a:focus-visible{border-color:#a34822;color:#a34822}.ep-section{margin:50px 0;scroll-margin-top:18px}.ep-section h2{font:700 clamp(26px,4vw,38px) Georgia,serif;line-height:1.14;margin:0 0 12px}.ep-label{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#9c431c;font-weight:700}.ep-summary{max-width:73ch;font-size:17px;line-height:1.65}.ep-source{font-size:13px;color:#565752}.ep-source a{color:#8a3c1d}.ep-section h3{font-size:17px;margin:24px 0 10px}.ep-question{border-top:1px solid #dcd4ca;background:#fff}.ep-question:last-of-type{border-bottom:1px solid #dcd4ca}.ep-question summary{cursor:pointer;padding:15px 30px 15px 15px;line-height:1.5;font-weight:600;position:relative;list-style:none}.ep-question summary::-webkit-details-marker{display:none}.ep-question summary:after{content:'+';position:absolute;right:13px;color:#9c431c}.ep-question[open] summary:after{content:'−'}.ep-answer{padding:1px 15px 15px;color:#373630;line-height:1.6}.ep-answer strong{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#9c431c}.ep-answer p{margin:6px 0}.ep-answer small{color:#60615e}.ep-model{padding:17px;background:#fff;border:1px solid #ded6cb;border-radius:8px;line-height:1.6;max-width:70ch}.ep-model p{margin:9px 0}.ep-board{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:20px 0}.ep-board div{padding:15px;background:#fff;border:1px solid #e3d8cc;border-radius:8px}.ep-board strong{display:block;font-size:23px;font-family:Georgia,serif}.ep-board small{color:#5d5d58}.ep-divider{height:1px;background:#ded6cb;margin:50px 0}@media(max-width:650px){.ep-board{grid-template-columns:repeat(2,1fr)}.ep-question summary{padding:14px 30px 14px 12px}}</style>'''
    content = '''<div class="crumb"><a href="index.html">All subjects</a> / <a href="english.html">English</a> / Preparation</div><section class="subject-hero"><p class="eyebrow">School half-yearly scope · 2026</p><h1>English · syllabus study desk</h1><p>Read the lesson → test your recall → check the suggested answer. The 2026 paper is used here only to identify the types of questions that were actually asked; all practice prompts below are original.</p></section><aside class="note"><strong>Source distinction:</strong> The nine lessons and nine language/writing topics come from the syllabus you supplied. Textbook locations below refer to the Flamingo and Vistas PDFs you supplied. This guide was assembled after reading the supplied 2026 OCR paper; it is retrospective practice, not a pre-exam prediction, and its answers are not official.</aside>'''+style
    content += '<div class="ep-board"><div><strong>8</strong><small>Unseen passage</small></div><div><strong>10</strong><small>Writing</small></div><div><strong>9</strong><small>Grammar</small></div><div><strong>23</strong><small>Textbook</small></div></div><p class="ep-source">These marks are from the supplied 2026 paper, not a promise about future exams. <a href="english-paper-2026.html">Read that paper and the unofficial worked discussion →</a></p>'
    content += '<nav class="ep-index" aria-label="Jump to guide sections"><a href="#literature">Literature</a><a href="#grammar">Grammar</a><a href="#writing">Writing</a><a href="#reading">Unseen passage</a><a href="#sources">Sources</a></nav><h2 id="literature">Read the nine set lessons</h2><p>Each summary is a revision aid, not a substitute for the source text. Page references identify locations in the two textbooks supplied for this project.</p>'
    for slug,title,book,start,end,author,summary,qs in CHAPTERS:
        content += f'<section class="ep-section" id="{slug}"><p class="ep-label">{book} · {escape(author)}</p><h2>{escape(title)}</h2><p class="ep-summary">{escape(summary)}</p><p class="ep-source">Textbook: {escape(source_link(book,start,end))} · Original practice, not printed paper questions.</p><h3>Check your recall</h3>'+''.join(answer_card(*q) for q in qs)+'</section>'
    content += '<div class="ep-divider"></div><h2 id="grammar">Grammar practice</h2><p>The actual 2026 paper used tense, preposition, voice and narration. Sentence transformation remains in the user-supplied scope even though it was not a printed question on that paper.</p>'
    for slug,title,rule,qs in GRAMMAR:
        content += f'<section class="ep-section" id="{slug}"><p class="ep-label">Grammar · original practice</p><h2>{escape(title)}</h2><p class="ep-summary">{escape(rule)}</p>'+''.join(answer_card(*q) for q in qs)+'</section>'
    content += '<div class="ep-divider"></div><h2 id="writing">Writing practice</h2><p>The paper offered notice or advertisement, and factual description or a letter. Poster is in your syllabus but did not appear as a direct choice in the supplied paper. These models use invented institutions, dates and people; change them to fit the task.</p>'
    for slug,title,rule,q,model in WRITING:
        content += f'<section class="ep-section" id="{slug}"><p class="ep-label">Writing · original model</p><h2>{escape(title)}</h2><p class="ep-summary">{escape(rule)}</p><h3>Practice prompt</h3><p>{escape(q)}</p><details class="ep-question"><summary>Reveal one possible model</summary><div class="ep-answer ep-model">{model}</div></details></section>'
    content += '<section class="ep-section" id="factual"><p class="ep-label">Paper-specific extra</p><h2>Factual description</h2><p>The 2026 paper offered an exhibition-cum-sale description as an alternative to the letter. Report verifiable sequence: what happened, where, when, who participated, what was displayed and how it ended. Do not invent facts about a real event; in a practice answer, label imaginary details as a model. <a href="english-paper-2026.html#section-3">See the model response to Q3 →</a></p></section>'
    content += '<section class="ep-section" id="reading"><p class="ep-label">Paper-specific extra</p><h2>Unseen passage</h2><p>In the actual paper, the passage on recycling carried 8 marks. Read it first, mark the exact sentence supporting each answer, then paraphrase in your own words; a vocabulary question may ask for a word used in the passage. <a href="english-paper-2026.html#section-1">Try the 2026 comprehension questions →</a></p></section>'
    content += '<section class="ep-section" id="sources"><h2>Sources and use</h2><p>The lesson references above point to the two user-supplied books: Flamingo_XII_Flamingo-Single.pdf and Vistas_XII_all-pages.pdf (not redistributed on this public archive). <a href="english-paper-2026.pdf">Supplied 2026 English OCR paper (PDF)</a> is provided here.</p><p>Writing-format cross-check: <a href="https://cbseacademic.nic.in/web_material/SQP/ClassXII_2025_26/EnglishCore-SQP.pdf" target="_blank" rel="noopener noreferrer">CBSE sample paper 2025–26</a> and <a href="https://cbseacademic.nic.in/web_material/SQP/ClassXII_2025_26/EnglishCore-MS.pdf" target="_blank" rel="noopener noreferrer">its marking scheme</a>. The CBSE sample is a reference for writing conventions, not the Kamrup half-yearly marking scheme; the supplied local paper controls our paper analysis.</p></section>'
    content += '<a class="back" href="english.html">← Back to English resources</a>'
    (ROOT/'english-preparation.html').write_text(layout('English syllabus preparation',content,'english'),encoding='utf8')
    print('generated English preparation:',len(CHAPTERS),'lessons,',len(GRAMMAR),'grammar topics,',len(WRITING),'writing topics')

if __name__=='__main__':build()
