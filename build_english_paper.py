"""Build the supplied English 2026 OCR paper and unofficial suggested answers."""
from pathlib import Path
from html import escape
from build import ROOT, layout

SOURCE = Path('C:/Users/debas/AppData/Local/hermes/cache/documents/doc_736a65004694_English_2026_OCR.pdf')
PDF = ROOT/'english-paper-2026.pdf'
PASSAGE = '''The next time you take printouts unnecessarily or you throw a paper into the bin, think for a minute as to how many trees have been felled to manufacture something you use so often every day.
Can you take out some time from your everyday routine and devote it to starting a simple recycling programme at your school or your neighbourhood? Not only you would save our planet from the torture of felling greenery, but also you would reduce generation and dumping of waste into the environment.
Using recycled papers conserves natural resources. As our population grows, the strain on these resources becomes even greater. You can drastically reduce the number of trees cut down for manufacturing paper. In addition to saving landfill space, you cut down on your expenses of trash-disposal. There is a reduction in air pollution caused by incineration. Making papers from discards instead of trees not only saves forest, but it also reduces energy used by up to three quarters and requires less than half as much water. Items that are made of paper and may be recycled are called the loose paper, a few examples are paper bags, magazines, newspapers, cardboard and egg-trays.
Working on a paper recycling plant demonstrates the concept of recycling waste into 'wealth'. Recycling paper will help to keep the environment green. If we keep our minds focused on the desire to be friendly to our earth and its resources, recycling will become important. Parents can teach their children the importance of recycled paper by bringing about simple changes in their lifestyle. Schools can also train up students to make paper products like folders, penholders, TLMS and various paper crafts.'''
Q1 = [
 ('a','What do you need to think before you take printouts unnecessarily?','Think of how many trees must be felled to make the paper and whether the printout is really necessary.'),
 ('b','Name some of the products that can be obtained from recycled paper.','Folders, penholders, teaching-learning materials (TLMs) and paper crafts are examples named in the passage.'),
 ('c','How does recycled paper conserve natural resources?','It reduces the need to cut trees and, according to the passage, uses less energy and water than making paper from trees.'),
 ('d','Give the antonym of conserve.','Waste (or <em>use up</em>).'),
 ('e','Find a word in the passage which means “the destruction of something, especially waste material by burning”.','Incineration.'),
]
Q2 = [
 ('main','You are the editor of your school/college magazine. Write a notice for your school/college notice board inviting articles for the school/college magazine. (Word limit – 50)', '''<div class="eng-writing"><strong>Pandu College · NOTICE</strong><br>6 October 2026<br><strong>Contributions for the College Magazine</strong><p>Students are invited to submit original articles, poems and short stories for the upcoming college magazine. Send typed entries with your name, class and contact number to the editorial desk by 20 October. Selected contributions will be published.</p>Debashish Thakuria<br>Student Editor</div><p>Sample only: replace institution, editor and dates with your own details. Keep within 50 words as directed.</p>'''),
 ('or','You are Rima/Rajiv, a resident of Tinsukia. You have lost your file folder containing important documents while travelling from Tinsukia to Jorhat. Draft an advertisement in not more than 50 words for publication in an English Daily giving details.','''<div class="eng-writing"><strong>LOST DOCUMENTS</strong><p>A blue file folder containing personal documents was lost while travelling from Tinsukia to Jorhat on 5 October 2026. The finder is requested to contact Rajiv, Tinsukia, at 9XXXXXXXXX. A suitable reward will be offered. Kindly do not misuse the documents.</p></div><p>Sample advertisement; replace the date and contact details with real information.</p>'''),
]
Q3 = [
 ('main','Write a factual description of the exhibition-cum-sale programme organised by the school recently.','''<div class="eng-writing"><strong>Exhibition-cum-Sale at Our School</strong><p>Our school organised an exhibition-cum-sale in its auditorium on 2 October 2026. The principal inaugurated the event at 10 a.m. Students from different classes displayed handmade crafts, paintings, science models and recycled-paper products. Teachers supervised the stalls and explained the exhibits to visitors. Parents and local residents attended throughout the day and bought many of the student-made items. The proceeds were set aside for the school library. The programme concluded at 4 p.m. after the principal thanked the participants. It gave students practical experience in teamwork, presentation and handling sales.</p></div><p>Model description: the date, venue, exhibits and proceeds are illustrative, not verified facts about a real school event.</p>'''),
 ('or','Write a letter to the Editor of “The Assam Tribune” highlighting the rising prices of essential commodities and their impact on common people, with the aim of drawing the attention of the concerned authorities.','''<div class="eng-writing">From<br>A Concerned Citizen<br>Guwahati, Assam<br>6 October 2026<br><br>To<br>The Editor<br>The Assam Tribune<br>Guwahati<br><br><strong>Subject: Rising prices of essential commodities</strong><p>Sir/Madam,</p><p>Through your newspaper, I wish to draw attention to the rising prices of food grains, vegetables, cooking oil and other daily necessities. Families with limited incomes are finding it difficult to meet basic expenses. Students and elderly people are also affected.</p><p>I request the authorities to monitor prices, prevent hoarding and improve the supply of essential goods. Publishing regular market-price information would help consumers.</p><p>Yours faithfully,<br>A Concerned Citizen</p></div>'''),
]
Q4 = [
 ('a','The boy (sleep), don’t disturb him.','The boy <strong>is sleeping</strong>; don’t disturb him.'),
 ('b','Perhaps it (rain) yesterday.','Perhaps it <strong>rained</strong> yesterday. (“Perhaps it might have rained yesterday” is possible in a different context, but simple past is the direct fill.)'),
 ('c','We reached the station after the train (leave).','We reached the station after the train <strong>had left</strong>.'),
 ('d','If I (be) you, I would not do that.','If I <strong>were</strong> you, I would not do that.'),
 ('e','He (work) here since 2009.','He <strong>has been working</strong> here since 2009. “Has worked” also works if the employment continues.'),
]
Q5 = [
 ('a','What is the time ____ your watch?','What is the time <strong>by</strong> your watch?'),
 ('b','She takes pride ____ his wealth.','She takes pride <strong>in</strong> his wealth. The pronoun “his” is in the supplied paper.'),
 ('c','I am very much interested ____ your story.','I am very much interested <strong>in</strong> your story.'),
 ('d','Man is superior ____ animal.','Man is superior <strong>to</strong> animal. More idiomatic: “Human beings are superior to animals”; the original sentence is retained above.'),
 ('e','The police ran ____ the thief.','The police ran <strong>after</strong> the thief.'),
]
Q6 = [
 ('a','My umbrella has been broken.','Someone has broken my umbrella. (The agent is unspecified; “Someone” is a supplied placeholder.)'),
 ('b','They laughed at us.','We were laughed at by them.'),
 ('c','Shut the window.','Let the window be shut. (An imperative-passive form.)'),
 ('d','Who discovered America?','By whom was America discovered?'),
 ('e','The coach is training the players.','The players are being trained by the coach.'),
]
Q7 = [
 ('a','My friend told me that he was very thirsty and requested me to give him a glass of water.','My friend said to me, “I am very thirsty. Please give me a glass of water.” The exact direct-speech wording may vary while preserving the meaning.'),
 ('b','One day Mukesh said to me, “I will be a motor mechanic and leave Firozabad.” I said to him, “Do you know anything about car?”','One day Mukesh told me that he would be a motor mechanic and leave Firozabad. I asked him whether he knew anything about cars. The source says “car” in the direct quote; “cars” in the indirect version is a grammatical adjustment.'),
]
# Textbook answers are separate editorial content; original passage excerpts remain in the question.
Q8 = [
 ('a','Why did Gandhi visit Lucknow in 1916?','He attended the annual convention of the Indian National Congress in Lucknow.'),
 ('b','Where is Champaran situated?','Champaran is a district in Bihar, near the border with Nepal.'),
 ('c','Where did Gandhi and Shukla board a train to?','They travelled by train to Patna. From there Gandhi later travelled towards Muzaffarpur and Champaran.'),
 ('d','What does the author of “Lost Spring” find Saheb doing every morning?','She finds Saheb searching for valuable things in garbage dumps.'),
 ('e','Where was the original home of Saheb’s family?','Their original home was Dhaka, in Bangladesh.'),
 ('f','What are mahseers?','Mahseers are large freshwater fish, known as game fish.'),
 ('g','Who is the Chota Sahib in “Memoirs of a Chota Sahib”?','John Rowntree, the author and British forest officer.'),
]
Q9 = [
 ('a','“Garbage to them is gold”. What does “garbage” mean to the elders and children, according to Anees Jung?','For adults, garbage is a means of survival: the scraps they sell provide food and income. For children, it also offers excitement and hope of finding a coin or something valuable among the rubbish.'),
 ('b','Why was Gandhi impressed with Shukla?','Rajkumar Shukla persisted in seeking Gandhi’s help for the Champaran sharecroppers. Although poor and illiterate, he followed Gandhi to different places and waited until Gandhi agreed to visit.'),
 ('c','What information does the author give us about Manas Wild Life Sanctuary?','In “Memoirs of a Chota Sahib,” John Rowntree describes the wildlife of the Manas area on the north bank of the Brahmaputra, including rhinoceroses. The sanctuary figures in his account of travel through Assam’s wild country.'),
 ('d','How was Gandhi able to influence the lawyers? Give instances.','Gandhi asked the lawyers what they would do if he were jailed. They initially intended to return home, but, ashamed to abandon the peasants while an outsider risked imprisonment, they pledged to stay and court arrest too.'),
 ('e','What is the irony inherent in Saheb’s full name?','Saheb-e-Alam means “lord of the universe,” yet Saheb is a poor, barefoot ragpicker with little control over his life. His grand name contrasts sharply with his circumstances.'),
 ('f','What is Firozabad famous for and why?','Firozabad is famous for its glass-bangle industry. Generations of families, including children in the account, work in its glass furnaces and bangle-making units, often under hazardous conditions.'),
]
Q10I = [
 ('a','How long does the poet want to stay still?','For a brief moment—while counting to twelve.'),
 ('b','Why does he ask us to keep still and not use any language?','He wants people to pause their activity and divisions, experience a shared silence and reflect on themselves and their actions.'),
 ('c','What does the poet mean by “not move our arms so much”?','He asks us to stop restless and potentially harmful actions for a moment and remain still.'),
]
Q10II = [
 ('a','Where was the speaker driving to?','She was driving to Cochin (now Kochi), specifically towards the airport in the poem.'),
 ('b','What did she notice when her mother sat beside her?','Her mother was dozing with her mouth open; her face looked pale and lifeless.'),
 ('c','Find two words from the passage that mean “sleep lightly” and “a dead body”.','<strong>Doze</strong> and <strong>corpse</strong>.'),
 ('d','Why was her mother’s face like that of a corpse?','She was old and looked pale and ashen while asleep, making the speaker confront the fear of losing her.'),
]
Q11 = [
 ('a','What is the “sadness” that the poet refers to in “Keeping Quiet”?','It is the sadness of never understanding ourselves because we are always busy and caught up in destructive pursuits. The poet hopes a moment of stillness will help us reflect.'),
 ('b','What is the “childish longing” that the poet refers to? Why is it “vain”?','The roadside-stand owners long for passing motorists to stop and buy something. Their hope is vain because most travellers ignore them or stop only to ask directions or for other reasons.'),
 ('c','How did the travellers on the highways react to the roadside stand?','They mostly drove past without stopping. Some complained that the stand spoiled the scenery; those who did stop often asked for directions or fuel rather than buying its produce.'),
 ('d','What childhood fear did Kamala Das refer to in “My Mother at Sixty-Six”? How did she hide it?','She feared losing her mother to death or separation. At the airport she concealed her anxiety by smiling and repeatedly telling her mother, “See you soon.”'),
]
Q12 = [
 ('a','What did the astrologer predict about the Tiger King?','The astrologers predicted that the prince would die because of a tiger. Later the warning centred on the hundredth tiger.'),
 ('b','Who is the Tiger King? Why did he get that name?','He is the Maharaja of Pratibandapuram, Jilani Jung Jung Bahadur. He became known as the Tiger King because he obsessively hunted tigers in an effort to escape the prediction of his death.'),
 ('c','How did the Tiger King celebrate the killing of the hundredth tiger?','He ordered the tiger’s body carried through the town in a procession and buried it. A tomb was built over the burial spot. In fact, he had only wounded the tiger; his hunters killed it afterward.'),
]

def card(num, letter, question, answer):
    return f'<article class="eng-q" id="q{num}{letter}"><p class="eng-id">{num}({letter})</p><h3>{question}</h3><div class="eng-answer"><strong>Suggested answer</strong>{answer}</div></article>'

def section(num, name, detail, groups):
    return '<section class="eng-section" id="section-'+str(num)+'"><h2>'+name+'</h2><p>'+detail+'</p>'+''.join(card(num,*row) for row in groups)+'</section>'

def build():
    if not PDF.is_file(): raise FileNotFoundError(f'Copy supplied source to {PDF} first')
    content = '''<div class="crumb"><a href="index.html">All subjects</a> / <a href="english.html">English</a></div><section class="subject-hero"><p class="eyebrow">Kamrup · HS second year · 2026</p><h1>English · question paper and suggested answers</h1><p>Full marks: 50 · Pass marks: 17 · Time: 2 hours · Supplied OCR PDF: 5 pages</p></section>
    <aside class="note"><strong>Source and answer status:</strong> The questions and passage below are from the supplied OCR PDF. Suggested answers are editorial, not an official marking scheme. The PDF contains a nearly blank fourth page. Every printed option is answered here, even where you were asked to attempt only a selection. Verify any OCR errors, especially the wording of grammar questions, against the PDF and your textbook.</aside>
    <div class="resource-list"><a href="english-paper-2026.pdf"><span>Download the supplied OCR question paper (PDF)</span><span aria-hidden="true">↗</span></a></div>
    <style>.eng-section{margin:40px 0}.eng-section>h2{font:700 clamp(24px,3vw,32px) Georgia,serif;margin:0 0 5px}.eng-section>p{color:#5d6571;margin:0 0 18px}.eng-q{background:#fff;border:1px solid #e0d9cf;border-radius:13px;padding:22px;margin:13px 0;scroll-margin-top:20px}.eng-id{font-size:12px;color:#9c431c;text-transform:uppercase;letter-spacing:.1em;font-weight:700;margin:0 0 8px}.eng-q h3{font-size:17px;line-height:1.45;margin:0 0 15px}.eng-answer{background:#f8f6f2;border-radius:8px;padding:14px 16px;line-height:1.6}.eng-answer>strong{display:block;color:#9c431c;font-size:12px;text-transform:uppercase;letter-spacing:.08em;margin-bottom:7px}.eng-answer p{margin:7px 0}.eng-writing{background:white;padding:14px;border:1px solid #e0d9cf;border-radius:7px;margin:8px 0}.eng-passage{padding:20px;background:white;border:1px solid #e0d9cf;border-radius:11px;white-space:pre-line;line-height:1.7}.eng-answer code{background:#ece9e1;padding:1px 4px;border-radius:4px}@media(max-width:620px){.eng-q{padding:16px}.eng-answer{padding:12px}}</style>'''
    content += '<section class="eng-section" id="section-1"><h2>Section A · Unseen passage</h2><p>Question 1 · 8 marks (2+2+2+1+1)</p><div class="eng-passage">'+escape(PASSAGE)+'</div>'+''.join(card(1,*row) for row in Q1)+'</section>'
    content += section(2,'Section B · Advanced writing skills','Question 2 · 5 marks. Choose one option in the exam; both models are shown here.',Q2)
    content += section(3,'Section B · Advanced writing skills','Question 3 · 5 marks. Choose one option in the exam; both models are shown here.',Q3)
    content += section(4,'Section C · Correct verb forms','Question 4 · answer any three of five (3 marks).',Q4)
    content += section(5,'Section C · Prepositions','Question 5 · answer any two of five (2 marks).',Q5)
    content += section(6,'Section C · Change of voice','Question 6 · answer any two of five (2 marks).',Q6)
    content += section(7,'Section C · Narration','Question 7 · answer any one of two (2 marks).',Q7)
    content += section(8,'Section D · Textbook quick answers','Question 8 · answer any five of seven (5 marks).',Q8)
    content += section(9,'Section D · Short answers','Question 9 · answer any three of six in 30–40 words (6 marks).',Q9)
    content += '<section class="eng-section" id="section-10"><h2>Section D · Poetry extract</h2><p>Question 10 · 4 marks. Both alternatives are solved below.</p><div class="eng-passage">(i) “Now we will count to twelve\nand we will all keep still,\nFor once on the face of the Earth\nlet’s not speak in any language,\nlet’s stop for one second,\nand not move our arms so much.”</div>'+''.join(card('10i',*row) for row in Q10I)+'<div class="eng-passage">Or (ii) “Driving from my parent’s\nhome to Cochin last Friday\nmorning, I saw my mother,\nbeside me,\ndoze, open mouthed,\nashen like that of a corpse...”</div>'+''.join(card('10ii',*row) for row in Q10II)+'</section>'
    content += section(11,'Section D · Poetry short answers','Question 11 · answer any two of four (4 marks).',Q11)
    content += section(12,'Section D · The Tiger King','Question 12 · answer any two of three (4 marks).',Q12)
    content += '<a class="back" href="english.html">← Back to English resources</a>'
    (ROOT/'english-paper-2026.html').write_text(layout('English paper and suggested answers',content,'english'),encoding='utf8')
    print('generated English paper with',*[len(x) for x in (Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10I,Q10II,Q11,Q12)],'answers')

if __name__=='__main__': build()
