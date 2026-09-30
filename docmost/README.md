# Docmost adapter

Az adapter csak validált canonical dokumentumokból készít publishing tervet. Az identity a
stable document ID; útvonalváltozás `MOVE`, tartalomváltozás `UPDATE`, új dokumentum
`CREATE`. Hiányzó local fájl nem eredményez automatikus törlést: alapértelmezésben
`ARCHIVE_REVIEW_REQUIRED` drift jelenik meg.

A dry run nem végez hálózati vagy Docmost-módosítást:

```bash
.venv/bin/python scripts/docmost_adapter.py --remote-state docmost/fixtures/empty-state.json
```

Live publishing nincs konfigurálva, ezért az állapot explicit
`BLOCKED_CREDENTIALS_OR_API_NOT_CONFIGURED`.

## API nélküli import

API key nélkül a támogatott Docmost útvonal a Markdown ZIP import. A GitHub Actions
`Build Docmost import bundle` workflow validálás után artifactként készíti el a
`docmost-import.zip` és `docmost-import-manifest.json` fájlokat. A teljes kézi folyamatot
a [NO_API_RUNBOOK.md](NO_API_RUNBOOK.md) dokumentálja.

Lokális bundle készítés:

```bash
.venv/bin/python scripts/docmost_bundle.py --output-dir generated/docmost-import
# vagy
make docmost-bundle
```
