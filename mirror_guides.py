"""Copy only published study-site assets into this archive, retaining their layouts."""
from pathlib import Path
from html import escape
import shutil
from site_copy import CAUTION, CREDIT

ROOT = Path(__file__).resolve().parent
HOME = ROOT.parent
SOURCES = {
    'physics': HOME / 'asseb-half-yearly-study-plan-2026',
    'alte': HOME / 'alte-harmony-revision',
    'computer-science': HOME / 'Documents' / 'computer-exam-study-site',
}


def mirror():
    for name, source in SOURCES.items():
        if not source.is_dir():
            raise FileNotFoundError(source)
        dest = ROOT / name
        dest.mkdir(exist_ok=True)
        if name == 'physics':
            files = [p for p in source.iterdir() if p.is_file() and (p.name.startswith('physics-') and p.suffix == '.html' or p.name in {'physics.html','physics-guide.css','katex-fonts.css','KATEX-LICENSE.txt'})]
            files += list((source / 'fonts').glob('*.woff2'))
        elif name == 'computer-science':
            files = [source / 'original.html', source / 'index.html']
        else:
            files = [p for p in source.iterdir() if p.is_file() and p.suffix in {'.html','.css','.js','.pdf'}]
        for file in files:
            rel = file.relative_to(source)
            out = dest / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            if file.suffix == '.html':
                html = file.read_text(encoding='utf8')
                if name == 'physics':
                    html = html.replace('href="index.html"','href="../index.html"')
                home = '<div class="archive-return"><a href="../index.html">← Kamrup half-yearly archive</a></div>'
                caution = '<aside class="archive-caution" role="note"><strong>Please note:</strong> '+escape(CAUTION)+'</aside>'
                credit = '<footer class="archive-credit">'+escape(CREDIT)+'</footer>'
                css = '<style>.archive-return,.archive-caution,.archive-credit{position:relative;z-index:99;font:600 13px/1.5 system-ui,sans-serif}.archive-return{padding:11px 18px;background:#172436;color:#fff}.archive-return a{color:#fff;text-decoration:underline;text-underline-offset:3px}.archive-return a:focus-visible{outline:2px solid #fff;outline-offset:3px}.archive-caution{padding:12px 18px;background:#fff8ec;color:#3f3427;border-bottom:1px solid #e6d9c5}.archive-credit{margin-top:36px;padding:20px 18px;text-align:center;background:#172436;color:#fff}</style>'
                html = html.replace('</head>',css+'</head>',1).replace('<body>','<body>'+home+caution,1).replace('</body>',credit+'</body>',1)
                out.write_text(html,encoding='utf8')
            else:
                shutil.copy2(file,out)
        print(name, len(files),'source assets copied')


if __name__ == '__main__':
    mirror()
