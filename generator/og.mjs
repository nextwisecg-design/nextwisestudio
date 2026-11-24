// Imaginile de previzualizare (1200x630) pentru linkurile trimise pe WhatsApp, LinkedIn etc.
// Rulare: node og.mjs  (după python3 prod.py), apoi din nou python3 prod.py ca să le copieze în out/.
import { chromium } from 'playwright';
import path from 'path'; import { fileURLToPath } from 'url';
const here = path.dirname(fileURLToPath(import.meta.url));
const b = await chromium.launch({ executablePath: process.env.CHROME || undefined, args: ['--no-sandbox', '--allow-file-access-from-files'] });
for (const [lang, file] of [['ro', 'out/index.html'], ['en', 'out/en/index.html']]) {
  const p = await b.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  await p.addInitScript(() => { try { sessionStorage.setItem('nw_in', '1'); } catch (e) {} });
  await p.goto('file://' + path.join(here, file));
  await p.addStyleTag({ content: '.nav .links a:not(.btn),.nav .links .lang,.nav .btn{display:none!important}.hero::after{display:none!important}.hero{min-height:630px!important;padding:90px 0 40px!important}.hero h1{font-size:76px!important}.hero .sub{font-size:20px!important}' });
  await p.waitForTimeout(6000);
  await p.screenshot({ path: path.join(here, 'static', `og-${lang}.jpg`), type: 'jpeg', quality: 86 });
  await p.close();
}
await b.close();
