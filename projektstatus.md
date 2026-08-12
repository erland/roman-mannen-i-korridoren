# Projektstatus

## Nuvarande fas

Baksidestexter och Apple Books-metadata är skapade efter användarens senaste manusversion. Romanen är redo för ny PDF/EPUB-export och publiceringsförberedelse.

## Senast godkända kapitel eller del

- Senast godkända: Kapitel 28 – Utomlands
- Senast ändrad: Sista mikroputs av språk, upprepningar och kapitelövergångar

## Nästa rekommenderade steg

Skapa ny export i önskat format: PDF, EPUB eller båda. Exporten ska utgå från de faktiska kapitelfilerna i `kapitel/` i numerisk ordning.

## Viktiga öppna beslut

- Ska slutbilden med mannen i ljus linnekavaj vara en verklig fortsättningskrok eller Martins paranoia? Nuvarande version lämnar detta medvetet öppet.
- Ska Elin/Helenas öde lämnas öppet, förklaras i epilog eller sparas som möjlig fortsättning? Nuvarande version lämnar det öppet.
- Ska romanen exporteras till PDF, EPUB eller båda?
- Ska den korta eller långa baksidestexten användas som primär butikstext?

## Risker att bevaka vid eventuell sista provläsning

- Slutet ska vara bitterljuvt, inte kännas som att berättelsen saknar avslut.
- Martins paranoia ska kännas begriplig men inte göra varje yttre hot osäkert.
- Klara ska behålla sin egen agens genom slutet.
- Romance-spåret med Elin ska ha emotionell verkan trots hennes försvinnande.
- Alla sätt de kriminella hittar Martin måste ha rimliga orsaker.

## Kontinuitet som är kontrollerad inför export

- Titel: Mannen i korridoren
- Undertitel: Ingenstans är nog långt borta
- Författare: Erland Lindmark
- Kapitel: 1–28 finns i `kapitel/`
- Baksidestexter: Kort och lång version skapade i `synopsis.md` och `exports/apple-books-metadata.md`
- Omslagsbild: Skapad – original samt högupplösta PNG/JPG 1800×2700 finns i `omslag/` och sparad som `omslag/omslag_mannen_i_korridoren.png`
- Senaste manusfas: Pass 3 genomfört, slutputs/exportförberedelse genomförd och sista mikroputs gjord efter användarens manuella ändringar

## Användarens aktuella önskemål

- Nära psykologisk känsla för vad personerna tänker.
- Tydlig cliffhanger eller krok i slutet av varje kapitel.
- Thriller med romance-inslag, vuxen målgrupp.


## Slutputs 2026-05-23

- Kapitelnoteringar har flyttats från kapitelfilerna till `kapitel/kapitelnoteringar.md`.
- Kapitelfilerna är nu renare för Apple Books/EPUB/PDF-export.
- Nästa rekommenderade steg: skapa ny Apple Books-anpassad EPUB från den rena versionen.

## Apple Books EPUB

- Senaste Apple Books-EPUB: `mannen_i_korridoren_apple_books.epub`
- Skapad: 2026-05-23
- Källa: rena kapitelfiler, kapitel 1–28
- Omslag: `omslag/mannen_i_korridoren_cover_1800x2700.jpg`, inbäddat i EPUB
- EPUBCheck: ej körd i denna miljö; rekommenderas före uppladdning.



## Senaste Apple Books-export

- Korrigerad Apple Books-EPUB skapad: `mannen_i_korridoren_apple_books_final.epub`.
- `dc:publisher` är ifyllt med `Erland Lindmark`.
- Dubblerad titelsida från kapitelflödet är borttagen.
- Navigations-TOC är markerad som icke-linjär i läsordningen.


## Senaste exportjustering

- Apple Books-EPUB uppdaterad: författarnamnet visas endast en gång på titelbladet och copyrighttexten lyder ”Alla rättigheter reserverade”.
## GitHub Actions/publicering

- GitHub Actions är infört enligt publiceringskitets koncept.
- `.github/` ligger i projektroten på samma nivå som `README.md`.
- Validering, preview-build och release-build finns i `.github/workflows/`.
- Byggscript och publiceringsmetadata finns i `scripts/` respektive `publishing/`.
- Nästa tekniska steg: lägg upp projektet i ett GitHub-repository och kör workflowt **Validate** samt en manuell **Build Preview**.



## Teknisk publiceringsstatus

- 2026-08-12: PDF-mallen i `publishing/pdf-template.tex` är uppdaterad för att undvika tom sida före omslag och innehållsförteckning i GitHub Actions-bygget.
