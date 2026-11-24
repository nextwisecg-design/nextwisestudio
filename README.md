# nextwise.studio

Site-ul NEXTWISE, din 24.11.2026: o pagină statică, în română (`/`) și în engleză (`/en/`).

| Folder | Ce e |
|---|---|
| `site/` | Ce se publică pe nextwise.studio. Netlify îl ia ca atare, fără build. |
| `generator/` | Scripturile Python din care iese `site/`. |
| `legacy/` | Site-ul vechi (variante pe piețe, diagnosticul AI, audituri). Nu se mai publică. |

## Cum schimbi ceva

Nu edita `site/index.html` de mână: are 240 KB, cu fonturile încorporate. Schimbi sursa și regenerezi.

```
cd generator
npm install            # o singură dată, pentru fonturi
python3 v5.py          # pagina de lucru, în română (v5.html)
python3 prod.py        # out/index.html și out/en/index.html, cu titlu, meta și comutator de limbă
cp out/index.html ../site/ && cp out/en/index.html ../site/en/
```

| Ce vrei să schimbi | Unde |
|---|---|
| Module, pași, principii | `common.py` |
| Proiectele din portofoliu și fișele tehnice | `v2data.py` (Casa Alesia, Grupul Schiorilor, Cosmina), `v5legal.py` (NEXTWISE HQ) |
| Datele firmei, contactul, paginile legale, secțiunea de site-uri | `v5legal.py` |
| Planeta (departamente, programe, sateliți) și introul | `v5.py` |
| Traducerea în engleză | `ro_strings.txt` și `en_strings.txt` (aceeași linie = aceeași frază), plus `prod.py` pentru texte noi |

`prod.py` se oprește dacă rămâne un text netradus în pagina engleză și îți spune care.

## De știut

- Pagina nu folosește cookie-uri și nu încarcă nimic de la terți.
- Textele legale nu au fost verificate de un avocat.
- Pictogramele ANPC din subsol sunt tăiate dintr-o captură. Când aveți fișierele originale de pe anpc.ro, înlocuiți-le în `anpc_b64.py`.
- Introul apare o singură dată pe sesiune; la schimbarea limbii se intră direct în site.
