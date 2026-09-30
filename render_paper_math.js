// Pre-render accessible mathematical notation for the paper answer cards.
const fs = require('fs');
const katex = require('C:/Users/debas/asseb-half-yearly-study-plan-2026/node_modules/katex');
const source = JSON.parse(fs.readFileSync('paper-math.json','utf8'));
const rendered = {};
for (const [id, equations] of Object.entries(source)) {
  rendered[id] = equations.map(tex => katex.renderToString(tex, {
    throwOnError: true, strict: 'error', trust: false,
    output: 'htmlAndMathml', displayMode: true
  }));
}
process.stdout.write(JSON.stringify(rendered));
