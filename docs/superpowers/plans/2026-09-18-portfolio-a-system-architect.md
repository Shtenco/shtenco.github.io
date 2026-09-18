# Portfolio A System Architect Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild `Shtenco/shtenco.github.io` into a data-driven bilingual creator portfolio that represents the verified Shtenco repository estate as a governed system-of-systems rather than a flat list of technologies.

**Architecture:** Keep GitHub Pages zero-build and framework-free. Split the current ~100 KB monolithic HTML into semantic `index.html`, one CSS file, one JS controller, and one repository data file. Repository counts, lifecycle filters, visibility, flagship cards and lineage must be rendered from data instead of duplicated in HTML.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, JSON, Python 3 standard library for static validation.

**Spec:** `docs/superpowers/specs/2026-09-18-portfolio-a-system-architect-design.md`

## Global Constraints

- Work only on `feat/portfolio-system-2026`.
- Do not merge into `main` without explicit human authorization.
- Current verified GitHub inventory is 59 repositories: 14 public and 45 private.
- Repository totals are data-derived, never hard-coded into visible content.
- Lifecycle enum is exactly `CANONICAL | CANDIDATE | R&D | LEGACY | ARCHIVE`.
- Public repositories may expose exact GitHub URLs; private repositories must not expose fake public source links.
- Keep RU/EN language switching.
- Preserve black/white/neon-green visual identity without retaining layered CSS patch debt.
- No historical backtest claim becomes a present verified performance claim.
- No research hypothesis becomes a confirmed scientific claim.
- No alpha/candidate component is described as production-ready.
- Core content must remain readable when JavaScript is unavailable.
- Respect `prefers-reduced-motion`.
- Main GitHub identity is `https://github.com/Shtenco`.

---

### Task 1: Repository Dataset Contract

**Files:**
- Create: `data/repositories.json`
- Create: `tests/test_portfolio_data.py`

**Interfaces:**
- Consumes: verified GitHub inventory plus Federation V5 lifecycle classification.
- Produces: JSON object `{"schema":"shtenco.portfolio-repositories/v1","as_of":"2026-09-18","repositories":[...]}`.

- [ ] **Step 1: Write failing data tests**

Tests load `data/repositories.json` and require:

```python
ALLOWED = {"CANONICAL","CANDIDATE","R&D","LEGACY","ARCHIVE"}

assert data["schema"] == "shtenco.portfolio-repositories/v1"
assert len(names) == len(set(names))
assert all(repo["lifecycle"] in ALLOWED for repo in repos)
assert all(repo["role_ru"] and repo["role_en"] for repo in repos)
assert all(repo["claim_boundary_ru"] and repo["claim_boundary_en"] for repo in repos)
assert all(repo["public_url"] is None for repo in repos if repo["visibility"] == "private")
assert all(repo["public_url"].startswith("https://github.com/Shtenco/") for repo in repos if repo["visibility"] == "public")
```

The test must also assert known modern boundaries: `midas_ai` is canonical trading intelligence, `synergy_agi_trader` is R&D, `synergy_messenger` is not presented as production-ready, and `shhts` is ARCHIVE.

- [ ] **Step 2: Run and verify RED**

Run:

```bash
python -m unittest -v tests.test_portfolio_data
```

Expected: FAIL because `data/repositories.json` does not exist.

- [ ] **Step 3: Create full verified dataset**

Include every currently verified repository with:

```json
{
  "name": "midas_ai",
  "visibility": "private",
  "lifecycle": "CANONICAL",
  "kind": "DOMAIN_SERVICE",
  "domain": "TRADING",
  "role_ru": "Канонический институциональный торговый интеллект",
  "role_en": "Canonical institutional trading intelligence",
  "flagship": true,
  "product": false,
  "public_url": null,
  "canonical_successor": null,
  "claim_boundary_ru": "Продвижение компонентов требует OOF/forward evidence; backtest не является реализованной прибылью.",
  "claim_boundary_en": "Component promotion requires OOF/forward evidence; backtest equity is not realized profit."
}
```

- [ ] **Step 4: Verify GREEN**

```bash
python -m unittest -v tests.test_portfolio_data
```

- [ ] **Step 5: Commit**

```bash
git add data/repositories.json tests/test_portfolio_data.py
git commit -m "feat: add verified portfolio repository dataset"
```

---

### Task 2: Static Portfolio Structure

**Files:**
- Replace: `index.html`
- Create: `tests/test_portfolio_html.py`

**Interfaces:**
- Consumes: `assets/portfolio.css`, `assets/portfolio.js`, `data/repositories.json`.
- Produces: semantic static shell with fallback content and dynamic mount points.

- [ ] **Step 1: Write failing HTML contract test**

The test must assert:

```python
required_ids = {
  "hero","architecture","flagships","lineage","research",
  "products","registry","principles","contacts"
}
```

and verify:

- stylesheet reference is `assets/portfolio.css`;
- module/controller reference is `assets/portfolio.js`;
- no primary `github.com/koshtenko` CTA remains;
- `https://github.com/Shtenco` is present;
- repository totals are not hard-coded as visible `59 repositories` / `60 repositories`;
- architecture boundary text is present;
- fallback flagship cards exist in HTML for no-JS readability.

- [ ] **Step 2: Verify RED**

```bash
python -m unittest -v tests.test_portfolio_html
```

Expected: FAIL against current monolithic index.

- [ ] **Step 3: Replace index with semantic shell**

Required page order:

```text
nav
hero
repository estate metrics
system architecture
flagship systems
trading lineage
frontier research
products
full registry
principles
contact/collaboration
footer
```

Hero copy must position Evgeniy Koshtenko as:

```text
SYSTEM ARCHITECT · QUANT · AI · FINTECH · DISTRIBUTED SYSTEMS
```

Use RU/EN text spans or data attributes without duplicating repository cards manually.

- [ ] **Step 4: Verify GREEN**

```bash
python -m unittest -v tests.test_portfolio_html
```

- [ ] **Step 5: Commit**

```bash
git add index.html tests/test_portfolio_html.py
git commit -m "feat: rebuild portfolio information architecture"
```

---

### Task 3: Visual System

**Files:**
- Create: `assets/portfolio.css`
- Create: `tests/test_portfolio_css.py`

**Interfaces:**
- Consumes: semantic class names from `index.html`.
- Produces: responsive black/white/neon-green presentation.

- [ ] **Step 1: Write failing CSS contract test**

Require the CSS to define:

```text
:root
.site-nav
.hero
.metric-grid
.system-map
.card-grid
.repo-card
.status-badge
.filter-bar
.registry-grid
.principles-grid
.contact-panel
@media
prefers-reduced-motion
:focus-visible
```

- [ ] **Step 2: Verify RED**

```bash
python -m unittest -v tests.test_portfolio_css
```

- [ ] **Step 3: Implement consolidated visual system**

Use:

- black background;
- white text;
- `#00e664` accent;
- `Manrope`, `DM Mono`, `Bebas Neue`, `Instrument Serif` with system-font fallbacks;
- bordered panels instead of excessive glassmorphism;
- lifecycle badge text in addition to color;
- 1-column mobile and responsive 2–4-column desktop grids;
- architecture map that collapses vertically below tablet width;
- reduced motion.

- [ ] **Step 4: Verify GREEN**

```bash
python -m unittest -v tests.test_portfolio_css
```

- [ ] **Step 5: Commit**

```bash
git add assets/portfolio.css tests/test_portfolio_css.py
git commit -m "feat: add Portfolio A visual system"
```

---

### Task 4: Repository Registry Controller

**Files:**
- Create: `assets/portfolio.js`
- Create: `tests/test_portfolio_js.py`

**Interfaces:**
- Consumes: `data/repositories.json`.
- Produces:
  - `loadRepositories()`;
  - `deriveMetrics(repositories)`;
  - `filterRepositories(repositories, state)`;
  - `renderRepositoryCard(repo)`;
  - `renderRegistry(repositories)`;
  - `renderFlagships(repositories)`;
  - `renderDomainCollections(repositories)`.

- [ ] **Step 1: Write failing controller contract tests**

Static tests must require:

- fetch of `data/repositories.json`;
- counts derived from `repositories.length`;
- no literal portfolio total used as truth;
- lifecycle filter state;
- domain filter state;
- visibility filter state;
- text search;
- RU/EN switching;
- private card renderer omits public source link;
- public card renderer uses `public_url`;
- filter buttons set `aria-pressed`.

- [ ] **Step 2: Verify RED**

```bash
python -m unittest -v tests.test_portfolio_js
```

- [ ] **Step 3: Implement controller**

Filtering state:

```js
const state = {
  lifecycle: "ALL",
  domain: "ALL",
  visibility: "ALL",
  search: "",
  flagshipOnly: false,
  lang: "ru"
};
```

Metrics are always computed:

```js
const metrics = {
  total: repositories.length,
  public: repositories.filter(r => r.visibility === "public").length,
  private: repositories.filter(r => r.visibility === "private").length,
  canonical: repositories.filter(r => r.lifecycle === "CANONICAL").length
};
```

- [ ] **Step 4: Verify GREEN**

```bash
python -m unittest -v tests.test_portfolio_js
```

- [ ] **Step 5: Commit**

```bash
git add assets/portfolio.js tests/test_portfolio_js.py
git commit -m "feat: add interactive repository registry"
```

---

### Task 5: Flagships, Lineage, Research and Product Rendering

**Files:**
- Modify: `assets/portfolio.js`
- Modify: `index.html`
- Create: `tests/test_portfolio_collections.py`

**Interfaces:**
- Consumes repository flags/domain/lifecycle.
- Produces distinct rendered collections without changing lifecycle truth.

- [ ] **Step 1: Write failing collection tests**

Require the data/JS contract to surface:

Flagships:

```text
synergy_system
synergy_financial_os
synergy_pay_system
midas_ai
agi_nexus
agi_autopilot
synergy_ai_company
synergy_eurasian
nexus_science_agent
shttps
synergynet
synergy_meta_os
turbo_linux
synergy_ai_blockchain
ai_compress
ai_language
synergy_messenger
synergy_app
```

Trading lineage must include `synergy_agi_trader` but display it as R&D and point its canonical successor to `midas_ai`.

Research collection must include at least `binary_quantum_theory`, `cold_nuclear`, `dlp_solver`, `motherboard_xpu_xml`, `qr_compress`, `agi_olga`.

Products must include SINERGY Finance, SYNERGY Messenger, AI Language Pro and SYNERGYCHAIN presentation/control surface.

- [ ] **Step 2: Verify RED**

```bash
python -m unittest -v tests.test_portfolio_collections
```

- [ ] **Step 3: Implement collection rendering**

Use the same repository objects; no second status database.

- [ ] **Step 4: Verify GREEN**

```bash
python -m unittest -v tests.test_portfolio_collections
```

- [ ] **Step 5: Commit**

```bash
git add index.html assets/portfolio.js tests/test_portfolio_collections.py
git commit -m "feat: surface flagship product and research lineages"
```

---

### Task 6: SEO, Metadata and Accessibility

**Files:**
- Modify: `index.html`
- Modify: `assets/portfolio.css`
- Modify: `assets/portfolio.js`
- Create: `tests/test_portfolio_quality.py`

**Interfaces:**
- Produces machine-readable identity and accessible controls.

- [ ] **Step 1: Write failing quality test**

Require:

- canonical URL `https://shtenco.github.io/`;
- updated title and description;
- Open Graph metadata;
- JSON-LD Person object;
- `lang="ru"` default;
- nav landmark;
- main landmark;
- button-based filters;
- search input label;
- visible `:focus-visible`;
- reduced-motion CSS;
- external public links use `rel="noopener noreferrer"`.

- [ ] **Step 2: Verify RED**

```bash
python -m unittest -v tests.test_portfolio_quality
```

- [ ] **Step 3: Implement metadata/accessibility**

JSON-LD must describe the person and public portfolio URL without pretending private repos are public source code.

- [ ] **Step 4: Verify GREEN**

```bash
python -m unittest -v tests.test_portfolio_quality
```

- [ ] **Step 5: Commit**

```bash
git add index.html assets/portfolio.css assets/portfolio.js tests/test_portfolio_quality.py
git commit -m "feat: harden portfolio SEO and accessibility"
```

---

### Task 7: Full Static Verification and PR

**Files:**
- Create: `scripts/check_portfolio.py`
- Create: `.github/workflows/portfolio.yml`
- Modify: `README.md` only if one exists or create a concise repository README if absent.

**Interfaces:**
- Produces one local command: `python scripts/check_portfolio.py`.

- [ ] **Step 1: Write checker around unittest suite**

`check_portfolio.py` must:

1. run the six portfolio test modules;
2. parse repository JSON;
3. print derived counts;
4. fail if expected files are missing;
5. fail on stale hard-coded repository total strings;
6. return non-zero on any contract failure.

- [ ] **Step 2: Run full verification**

```bash
python scripts/check_portfolio.py
```

Expected: PASS with derived counts from the JSON data.

- [ ] **Step 3: Add GitHub Actions workflow**

Workflow executes only stdlib Python:

```yaml
- run: python scripts/check_portfolio.py
```

- [ ] **Step 4: Verify repository diff and secret hygiene**

Ensure no credentials, private source URLs or accidental private repository content beyond names/roles are exposed.

- [ ] **Step 5: Open PR**

PR base: `main`  
PR head: `feat/portfolio-system-2026`

PR description must report actual local/static verification and distinguish it from hosted CI status.

Do not merge.

## Plan Self-Review

- Spec coverage: full registry, dynamic counts, lifecycle separation, system map, flagships, lineage, frontier research, products, principles, RU/EN, claim safety, public/private handling, SEO, accessibility and no-merge boundary are all mapped to tasks.
- Placeholder scan: no implementation step depends on TBD/TODO.
- Type consistency: repository data fields and JS filtering state are stable across all tasks.
- Scope: one static portfolio application; no unrelated repository refactors.
