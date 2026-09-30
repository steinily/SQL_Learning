# Docmost API nélküli feltöltési runbook

## Recommended path

A repository a `scripts/docmost_bundle.py` eszközzel csak a publishable, fully-verified és complete/mature dokumentumokból Markdown ZIP-et készít. A workflow ezt GitHub Actions artifactként állítja elő.

1. Nyisd meg a GitHub repository **Actions → Build Docmost import bundle** workflow-ját.
2. Válaszd a **Run workflow** műveletet, vagy használj egy olyan `main` push-t, amely contentet módosít.
3. A sikeres futásból töltsd le a `docmost-import-<commit-sha>` artifactet.
4. A Docmost cél-Space-ben nyisd meg a Pages menü `...` műveletét, válaszd az **Import pages** lehetőséget, majd az **Import zip file** opciót.
5. Töltsd fel a `docmost-import.zip` fájlt. A ZIP 385 publishable Markdown oldalt tartalmaz.
6. Tartsd meg a letöltött `docmost-import-manifest.json` fájlt release evidence-ként; ez tartalmazza az imported path, stable DBKB ID és SHA-256 mappinget.

Az import előtt és után futtasd a repository dry-run tervét:

```bash
.venv/bin/python scripts/docmost_adapter.py \
  --remote-state docmost/fixtures/empty-state.json \
  --output generated/docmost-dry-run.json
```

Ez a folyamat nem módosít remote oldalt, nem töröl oldalt, és nem igényel Docmost API key-t. A front matter nem kerül a page body-ba; minden oldal elején láthatatlan HTML comment őrzi a `DBKB-ID` stabil identity-t.

## API később

A Docmost REST API hivatalos dokumentáció szerint API key `Authorization: Bearer <token>` autentikációt használ, és a Docmost user guide API-fejezet Enterprise feature-ként jelöli. Ha lesz megfelelő licenc és token, külön API publisher adható a bundle mellé; a GitHub Actions secretet csak environment-szinten, minimum jogosultsággal szabad konfigurálni.

## Recovery and drift

- A GitHub repository marad a canonical source of truth.
- A Docmost import nem helyettesíti a dry-run identity/drift ellenőrzést.
- Hibás import esetén a Docmost oldalt ne töröld automatikusan; javítsd a bundle-t, importáld új Space-be vagy archív ellenőrzési Space-be, majd végezz kézi review-t.
- A bundle nem tartalmaz API tokent, jelszót vagy remote state-et.

## Authoritative references

- [Docmost Import & Export](https://docmost.com/docs/user-guide/import-export)
- [Docmost API](https://docmost.com/docs/user-guide/api)
- [Docmost API reference](https://docmost.com/api-docs)
- [GitHub Actions secrets](https://docs.github.com/en/actions/concepts/security/secrets)
- [GitHub Actions artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts)
