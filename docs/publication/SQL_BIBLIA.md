# SQL Biblia publication repository

`SQL_Biblia` is a private, read-only GitHub projection of the validated publication subset of `steinily/SQL_Glossary`.

## Repository setup

Create the target repository as private and do not add collaborators who should not see the material. In the canonical repository configure an Actions secret named `SQL_BIBLIA_TOKEN`. The token must have the minimum fine-grained repository permission needed to write `steinily/SQL_Biblia` contents. Never commit the token or put it into generated artifacts.

The workflow `.github/workflows/publish-sql-biblia.yml` then:

1. validates the canonical repository;
2. exports the 385 eligible documents without YAML front matter;
3. preserves each stable `DBKB-ID` in an HTML comment;
4. replaces the target projection and pushes only when content changes.

The target repository is generated output. Changes must be made in `SQL_Glossary`, then published by workflow. The canonical repository remains the source for research, metadata, QA, metrics and release evidence.

## First synchronization

After the private repository exists and `SQL_BIBLIA_TOKEN` is configured:

1. Open **Actions → Publish SQL Biblia projection** in `SQL_Glossary`.
2. Select **Run workflow** on `main`.
3. Confirm that the target repository receives the generated snapshot.

The same workflow also runs on relevant `main` pushes. If the secret is not configured, the workflow intentionally cannot publish; the source repository remains unaffected.

Until the secret is configured, the workflow still succeeds and uploads a `sql-biblia-<commit-sha>` artifact. That artifact is the same generated projection and can be downloaded manually.
