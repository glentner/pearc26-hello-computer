# GitHub Pages publishing source

This folder is the source for the project's GitHub Pages site:

**<https://glentner.github.io/pearc26-hello-computer/>**

- **`index.html`** — a generated, **byte-for-byte copy** of
  [`.agents/factory/getting-started.html`](../.agents/factory/getting-started.html),
  the canonical, self-contained interactive walkthrough that travels with the
  portable `.agents/` factory tree. **Do not edit this copy** — edit the
  canonical file and run `make pages` to regenerate it, then ship to `main`.
- **`.nojekyll`** — disables Jekyll so the self-contained HTML (no build step,
  no external assets) is served verbatim.

GitHub Pages is configured to **deploy from the `main` branch, `/docs` folder**.
Pushing an updated `docs/index.html` to `main` redeploys the site automatically.
