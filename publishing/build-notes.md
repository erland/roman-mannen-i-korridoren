# Publiceringsbygge

Detta projekt innehåller GitHub Actions för automatisk validering, manuell preview-build och release-build.

## Struktur

- `.github/workflows/01-validate.yml` kör snabb projektvalidering vid pull request och push till `main`.
- `.github/workflows/02-build-preview.yml` kan köras manuellt och bygger EPUB + PDF som ett gemensamt Actions-artifact.
- `.github/workflows/03-release.yml` triggas av taggar `v*` och publicerar EPUB + PDF som release assets.
- `scripts/validate_project.py` kontrollerar projektstruktur, kapitelserie, metadata och att exportarbetsnoteringar inte ligger kvar i kapitelfilerna.
- `scripts/build_book.py` bygger EPUB/PDF från `kapitel/kapitel-XX.md` i numerisk ordning.
- `publishing/metadata.yaml` innehåller metadata för Pandoc.
- `publishing/epub.css` styr EPUB-sättningen.
- `publishing/pdf-template.tex` och `publishing/pdf-filter.lua` styr PDF-sättningen.

## Lokala kommandon

Validera projektet:

```bash
python3 scripts/validate_project.py .
```

Bygg EPUB och PDF med låst Pandoc-version:

```bash
python3 scripts/build_book.py --output-dir dist
```

Bygg bara EPUB:

```bash
python3 scripts/build_book.py --output-dir dist --formats epub
```

Bygg bara PDF:

```bash
python3 scripts/build_book.py --output-dir dist --formats pdf
```

## Versionskrav

Bygget är låst till Pandoc 3.1.11.1 för reproducerbar EPUB/PDF-export.
PDF-bygget kräver XeLaTeX och TeX Gyre Pagella-fonten.
