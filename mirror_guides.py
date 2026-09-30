"""Copy only published study-site assets into this archive, retaining their layouts."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
HOME = ROOT.parent
SOURCES = {
    'physics': HOME / 'asseb-half-yearly-study-plan-2026',
    'alte': HOME / 'alte-harmony-revision',
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
                css = '<style>.archive-return{position:relative;z-index:99;padding:11px 18px;background:#172436;color:#fff;font:600 13px/1.4 system-ui,sans-serif}.archive-return a{color:#fff;text-decoration:underline;text-underline-offset:3px}.archive-return a:focus-visible{outline:2px solid #fff;outline-offset:3px}</style>'
                html = html.replace('</head>',css+'</head>',1).replace('<body>','<body>'+home,1)
                out.write_text(html,encoding='utf8')
            else:
                shutil.copy2(file,out)
        print(name, len(files),'source assets copied')


if __name__ == '__main__':
    mirror()
