# Romanprojekt: Mannen i korridoren

Detta är projektarkivet för romanen **Mannen i korridoren – Ingenstans är nog långt borta** av **Erland Lindmark**.

## Rekommenderat arbetsflöde

1. Planera romankärnan: huvudperson, mål, hinder, insats och förändring.
2. Skapa synopsis, kapitelplan, romanbibel och stilguide.
3. Skriv ett kapitel i taget i chatten.
4. Justera kapitlet tills kapitlet är godkänt.
5. Uppdatera projektfilerna och projektstatus.
6. Fortsätt med nästa kapitel eller revision.

## Viktiga filer

- `projektstatus.md` visar nuvarande fas, senaste godkända kapitel och nästa rekommenderade steg.
- `roman-bibel.md` innehåller projektets centrala fakta.
- `synopsis.md` sammanfattar hela handlingen.
- `kapitelplan.md` är färdplanen för romanen.
- `stilguide.md` håller språk, ton och perspektiv konsekvent.
- `tidslinje.md` håller ordning på händelser.
- `kontinuitetsanteckningar.md` fångar fakta som inte får motsägas.
- `revisionsonskemal.md` samlar planerade förbättringar.
- `arbetslogg.md` visar vad som har gjorts.
- `kapitel/` innehåller kapitelutkast och godkända kapitel.
- `omslag/` innehåller skapad omslagsbild/framsida.
- `exports/apple-books-metadata.md` innehåller kort och lång baksidestext samt publiceringsmetadata.

## Grundprincip

Romanen skrivs kapitelvis. Ny text visas först i chatten och sparas i projektpaketet först när den är godkänd.

## Aktuell status

- Första manusutkast komplett: 28 kapitel.
- Omslagsbild skapad och sparad i `omslag/`.
- Pass 1 struktur och logik genomfört 2026-05-22.
- Pass 2 karaktär och relation genomfört 2026-05-22.
- Pass 3 språk, tempo och cliffhangers genomfört 2026-05-22.
- Slutputs och exportförberedelse genomförd 2026-05-22.
- Nästa rekommenderade steg: skapa PDF/EPUB eller göra en sista manuell provläsning.

## Exportberedskap

Romanen är exportförberedd från de faktiska kapitelfilerna `kapitel/kapitel-01.md` till `kapitel/kapitel-28.md` i numerisk ordning. Titel, undertitel, författare och omslagsstatus är synkade i projektets kanoniska filer.



## Omslag för publicering

Högupplösta omslagsfiler har lagts till i `omslag/`: PNG och JPG i 1800 × 2700 px.


## Publiceringsklar kapitelstruktur

Kapitelfilerna i `kapitel/kapitel-XX.md` innehåller endast läsartext. Tidigare kapitelnoteringar har sparats separat i `kapitel/kapitelnoteringar.md` som arbetsmaterial och ska inte ingå i EPUB/PDF-export.

## Senaste Apple Books-export

- EPUB-fil: `mannen_i_korridoren_apple_books.epub`
- Skapad: 2026-05-23 med Pandoc 3.1.11.1
- Inkluderar kapitel 1–28 och högupplöst omslag.
- Validera med EPUBCheck innan uppladdning till Apple Books.



## Apple Books EPUB-fix

Senaste korrigerade EPUB: `exports/mannen_i_korridoren_apple_books_final.epub`.

Fixar: ifyllt publisher-fält, borttagen dubblerad titelsida och TOC markerad som icke-linjär lässida.
## GitHub Actions och publicering

Projektet innehåller nu en `.github/`-katalog i repositoryts rot, på samma nivå som `README.md`.

Workflow-filer:

- `.github/workflows/01-validate.yml` – validerar projektstruktur och kapitelfiler vid pull request och push till `main`.
- `.github/workflows/02-build-preview.yml` – manuell preview-build som skapar EPUB och PDF som ett gemensamt GitHub Actions-artifact.
- `.github/workflows/03-release.yml` – release-build som triggas av `v*`-taggar och laddar upp EPUB/PDF som release assets.

Bygg- och valideringslogik ligger i `scripts/` och publiceringsinställningar ligger i `publishing/`.

