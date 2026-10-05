"""Render the supplied Computer Science paper with unofficial worked solutions."""
from pathlib import Path
from html import escape
from build import ROOT, layout

SOURCE = Path('C:/Users/debas/AppData/Local/hermes/cache/documents/doc_0f56b20a769d_Computer_Science_and_Application_2026_OCR.pdf')
PDF = ROOT / 'computer-science-paper-2026.pdf'

# Transcribed from the user's three-page OCR PDF. Q3(e) has a visually awkward
# mark allocation in the supplied text; keep the printed question wording.
Q1 = [
 ('a','What is a database?','A database is an organised collection of related data, stored so that it can be accessed and managed efficiently.'),
 ('b','What is a field?','A field (attribute/column) is a named property of a record in a table, such as Roll_No or Name.'),
 ('c','State the use of break statement in a switch-case statement.','break ends the current switch statement and transfers control to the statement after it; it prevents execution from falling through to subsequent cases.'),
 ('d','What is a character constant in C++?','A character constant represents one character, written in single quotes, such as <code>\'A\'</code> or <code>\'7\'</code>. Double-quoted <code>"A"</code> is a string literal.'),
]
Q2 = [
 ('a','Write the differences between DML and DDL.','<strong>DDL</strong> (Data Definition Language) creates or changes database structure: <code>CREATE TABLE</code>, <code>ALTER TABLE</code>, <code>DROP TABLE</code>. <strong>DML</strong> (Data Manipulation Language) changes stored rows: <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>. Some curricula group <code>SELECT</code> under DML, while others call it DQL.'),
 ('b','Write the use of the %= operator with an example.','<code>%=</code> is remainder-assignment for integer operands. <code>x %= y</code> means <code>x = x % y</code>. For <code>int x = 17; x %= 5;</code>, x becomes 2.'),
 ('c','Rewrite the following statement using an if-else statement: x = ((y &lt; z) ? y : z);','<pre>if (y &lt; z)\n    x = y;\nelse\n    x = z;</pre>Both forms assign the smaller of y and z to x (and z when they are equal).'),
 ('d','What is meant by testing and debugging in a program?','<strong>Testing</strong> runs a program on chosen inputs and compares actual with expected results. <strong>Debugging</strong> locates the cause of a fault and fixes it, then retests the program.'),
 ('e','Differentiate between while and do-while loop.','<code>while</code> checks the condition before the body and may execute zero times. <code>do-while</code> checks afterward and executes its body at least once. A do-while statement ends with a semicolon.'),
 ('f','What is a flowchart? Give one example.','A flowchart is a diagram representing an algorithm with standard symbols and arrows. Example: Start → input n → decision n % 2 == 0? → print “even” if yes, otherwise “odd” → End.'),
 ('g','Differentiate between i++ and ++i.','Both increase i by 1. <code>i++</code> (post-increment) yields the old value in an expression, then increments. <code>++i</code> (pre-increment) increments first, then yields the new value. With i = 4, <code>a = i++</code> sets a = 4; starting again at i = 4, <code>a = ++i</code> sets a = 5.'),
 ('h','What is operator in C++? Explain briefly.','An operator is a symbol that performs an operation on one or more operands. Examples: <code>+</code> adds values (<code>3 + 2</code> is 5); <code>==</code> compares for equality; <code>&amp;&amp;</code> combines boolean conditions.'),
]
PRIME_CODE = '''#include <iostream.h>
#include <conio.h>

void main()
{
    int first, last, n, divisor, prime, temp;
    clrscr();
    cout << "Enter the start and end of the range: ";
    cin >> first >> last;
    if (first > last)
    {
        temp = first;
        first = last;
        last = temp;
    }
    cout << "Prime numbers: ";
    for (n = first; n <= last; n++)
    {
        if (n < 2)
            continue;
        prime = 1;
        for (divisor = 2; divisor <= n / divisor; divisor++)
        {
            if (n % divisor == 0)
            {
                prime = 0;
                break;
            }
        }
        if (prime == 1)
            cout << n << " ";
    }
    getch();
}'''
CONSTRUCTOR_CODE = '''#include <iostream.h>
#include <conio.h>

class Student
{
    int roll;
public:
    Student(int r)
    {
        roll = r;
    }
    void show()
    {
        cout << "Roll number: " << roll;
    }
};

void main()
{
    clrscr();
    Student s(12);
    s.show();
    getch();
}'''
Q3 = [
 ('a','Define data type. What are the different data types used in C++?','A <strong>data type</strong> specifies the kind of value a variable may store and the operations allowed. Fundamental types include <code>int</code> (whole numbers), <code>char</code> (characters), <code>float</code> and <code>double</code> (real numbers), <code>bool</code> (true/false) and <code>void</code> (no value). Derived types include arrays and pointers; user-defined types include classes and enumerations. Example: <code>int age = 17; char grade = \'A\'; float price = 12.5;</code>'),
 ('b','What is constructor? Explain with an example.','A <strong>constructor</strong> is a class member with the same name as its class and no return type, automatically called when an object is created. It commonly initialises members. In this Turbo C++ example, <code>Student s(12)</code> calls the constructor to set roll to 12.'),
 ('c','Explain the different types of errors in programming.','<ul><li><strong>Syntax / compile-time error:</strong> breaks a language rule, such as omitting a semicolon; the compiler reports it.</li><li><strong>Runtime error:</strong> occurs when the program executes, such as an invalid operation or accessing invalid memory.</li><li><strong>Logical error:</strong> the program runs but gives an incorrect result, such as using addition instead of multiplication.</li></ul>Testing with known inputs and debugging help find and correct these errors.'),
 ('d','Write a program in C++ to display all prime numbers within a given range.','The program reads two limits and inspects each integer in the inclusive interval. It skips numbers below 2 and looks for a divisor; a value with no such divisor is printed. It also swaps reversed endpoints. Example: input <code>10 20</code> prints <code>11 13 17 19</code>.'),
 ('e','What is a variable? Why is a variable called symbolic variable? What is meant by dynamic initialization of a variable? Give example.','A <strong>variable</strong> is a named storage location whose value can change. It is <strong>symbolic</strong> because its meaningful name represents the location and value instead of requiring a raw address. <strong>Dynamic initialisation</strong> gives a variable its initial value from an expression evaluated at run time: <code>int a, b; cin &gt;&gt; a &gt;&gt; b; int sum = a + b;</code>. Here sum depends on the input.'),
 ('f','What is the role of comments and indentation in a program?','<strong>Comments</strong> document purpose, assumptions and non-obvious decisions; the compiler ignores them. C++ uses <code>//</code> for a line and <code>/* ... */</code> for a block. <strong>Indentation</strong> visually groups code inside blocks, making loops and conditions easier to read, maintain and debug. It does not itself change the meaning of properly braced C++ code. Example: indent the body of an <code>if</code> inside its braces, and comment why a special case such as n &lt; 2 is excluded in a prime test.'),
 ('g','What are data types in MySQL? Name some common data types and their uses.','A <strong>data type</strong> specifies what kind of value a table column can hold. Examples: <code>INT</code> stores whole numbers (quantity); <code>DECIMAL(6,2)</code> stores exact decimal values (price); <code>CHAR(n)</code> stores fixed-length text (a fixed code); <code>VARCHAR(n)</code> stores variable-length text (a name); <code>DATE</code> stores a calendar date; <code>TIME</code> stores a time. MySQL also has <code>DATETIME</code> for date and time.'),
 ('h','What is Typecasting? Mention the use of sizeof operator.','<strong>Typecasting</strong> explicitly converts a value to another data type. For example, <code>float result = (float)5 / 2;</code> gives 2.5 rather than the integer-division result 2. <code>sizeof</code> tells the size in bytes of an object or data type, e.g. <code>sizeof(int)</code> or <code>sizeof(result)</code>. The number of bytes for <code>int</code> can vary by compiler; do not assume a modern compiler and Turbo C++ report the same number.'),
]

def card(group, letter, question, answer):
    extra = ''
    if group == 3 and letter == 'b': extra = '<pre class="cs-code">'+escape(CONSTRUCTOR_CODE)+'</pre>'
    if group == 3 and letter == 'd': extra = '<pre class="cs-code">'+escape(PRIME_CODE)+'</pre>'
    return (f'<article class="cs-question" id="q{group}{letter}"><p class="cs-number">Question {group}({letter})</p>'
            f'<h3>{question}</h3><div class="cs-answer"><strong>Suggested answer</strong>{answer}{extra}</div></article>')

def build():
    if not PDF.is_file():
        raise FileNotFoundError(f'Copy supplied paper to {PDF} first')
    intro = '''<div class="crumb"><a href="index.html">All subjects</a> / <a href="computer-science.html">Computer Science</a></div>
    <section class="subject-hero"><p class="eyebrow">Kamrup · HS second year · 2026</p><h1>Computer Science and Application</h1>
    <p>Full marks: 50 · Pass marks: 17 · Time: 2 hours · Supplied OCR paper: 3 pages</p></section>
    <aside class="note"><strong>Source and answer status:</strong> Questions below are transcribed from the supplied OCR PDF. Answers are independently written suggestions, not an official marking scheme; check the PDF and your prescribed textbook for exact wording. Q3 asks for any six of eight; all eight are answered here. The original pre-exam guide is preserved separately from the later expanded study desk.</aside>
    <div class="resource-list"><a href="computer-science-paper-2026.pdf"><span>Download the supplied OCR paper (PDF)</span><span aria-hidden="true">↗</span></a><a href="computer-science/original.html"><span>Original pre-exam preparation</span><span aria-hidden="true">↗</span></a><a href="computer-science/index.html"><span>Expanded study desk (post-exam revision)</span><span aria-hidden="true">↗</span></a></div>
    <style>.cs-section{margin:40px 0}.cs-section>h2{font:700 clamp(23px,3vw,32px) Georgia,serif;margin:0 0 5px}.cs-section>p{color:#5d6571;margin:0 0 18px}.cs-question{background:#fff;border:1px solid #e0d9cf;border-radius:13px;padding:22px;margin:13px 0;scroll-margin-top:20px}.cs-number{font-size:12px;color:#9c431c;text-transform:uppercase;letter-spacing:.1em;font-weight:700;margin:0 0 8px}.cs-question h3{font-size:17px;line-height:1.4;margin:0 0 15px}.cs-answer{background:#f8f6f2;border-radius:8px;padding:14px 16px;line-height:1.6}.cs-answer>strong{display:block;color:#9c431c;font-size:12px;text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px}.cs-answer code{background:#ece9e1;border-radius:4px;padding:1px 4px}.cs-answer pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#e9e7e1;border-radius:7px;padding:12px;margin:10px 0 0;font:14px/1.5 Consolas,monospace}.cs-answer pre.cs-code{white-space:pre;overflow-x:auto;overflow-wrap:normal;background:#182b26;color:#ecf8ef;padding:16px}.cs-answer ul{margin:8px 0 0;padding-left:20px}.cs-answer li{margin:5px 0}@media(max-width:620px){.cs-question{padding:16px}.cs-answer{padding:12px}}</style>'''
    sections = [
        (1,'Short answers','1 mark each · 4 questions',Q1),
        (2,'Explain briefly','2 marks each · 8 questions',Q2),
        (3,'Extended answers','5 marks each · answer any six of eight in the exam',Q3),
    ]
    content = intro + ''.join(f'<section class="cs-section" id="section-{num}"><h2>Section {num} · {name}</h2><p>{desc}</p>' + ''.join(card(num,*row) for row in rows)+'</section>' for num,name,desc,rows in sections)
    content += '<a class="back" href="computer-science.html">← Back to Computer Science resources</a>'
    (ROOT/'computer-science-paper-2026.html').write_text(layout('Computer Science paper and suggested solutions',content,'computer-science'),encoding='utf8')
    print('generated paper page with',*[len(rows) for _,_,_,rows in sections],'answers')

if __name__ == '__main__': build()
