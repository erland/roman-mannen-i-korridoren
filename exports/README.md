# Exporter

Denna katalog innehåller metadata om genererade exporter. Exporter är inte romanens kanoniska källtext. De kan återskapas från `kapitel/kapitel-XX.md`.

## Exportförberedelse

- Exportunderlag: `kapitel/kapitel-01.md` till `kapitel/kapitel-28.md`
- Sortering: numerisk kapitelordning
- Titel: Mannen i korridoren
- Undertitel: Ingenstans är nog långt borta
- Författare: Erland Lindmark
- Omslagsbild: `omslag/omslag_mannen_i_korridoren.png`
- Status: Slutputsad och exportförberedd
- Senast kontrollerad: 2026-05-22

## Rekommenderade exportformat

- PDF för utskrift och delning som färdig läsfil.
- EPUB för e-boksläsare och flexibel textstorlek.



## Exportunderlag

Kapitelfilerna är nu rensade från kapitelnoteringar. Export ska utgå från `kapitel/kapitel-01.md` till `kapitel/kapitel-28.md` i numerisk ordning.
## GitHub Actions

Framtida exporter kan byggas via GitHub Actions med `scripts/build_book.py`. Preview-build laddas upp som Actions-artifact och release-build publicerar EPUB/PDF som GitHub Release assets.


## PDF-fix

2026-08-12: Nästa PDF-export från GitHub Actions ska inte innehålla extra tom sida före omslag eller innehållsförteckning.
