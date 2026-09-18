# Evgeniy Koshtenko Portfolio A — System Architect Portfolio Design

**Date:** 2026-09-18  
**Repository:** `Shtenco/shtenco.github.io`  
**Branch:** `feat/portfolio-system-2026`  
**Status:** APPROVED DESIGN / SPECIFICATION  
**Owner:** Evgeniy Koshtenko

## 1. Purpose

Rebuild `https://shtenco.github.io/` from a technology showcase into a maintainable creator portfolio for the full Shtenco repository estate.

The portfolio must communicate one core idea:

> Evgeniy Koshtenko is the creator and system architect of a federated technology estate spanning quantitative trading, AI/agents, financial infrastructure, distributed systems, cryptographic trust, compression, scientific research and end-user applications.

The site must not present all repositories as equally mature or equally authoritative.

## 2. Source-of-truth rule

The portfolio may describe repositories only from evidence actually present in the GitHub estate or from explicit owner-supplied profile facts.

Repository existence does not imply:

- production readiness;
- profitability;
- scientific confirmation;
- financial authority;
- blockchain authority;
- deployment status;
- public source availability.

The site therefore uses the same lifecycle vocabulary as Federation V5:

```text
CANONICAL
CANDIDATE
R&D
LEGACY
ARCHIVE
```

System kind is separate from lifecycle status.

## 3. Current audited inventory

Two independent GitHub inventory paths currently return **59 repositories** under `Shtenco`.

Current visibility split:

```text
14 public
45 private
59 total observed
```

The user expects 60 repositories. The site must not invent repository #60. The implementation will render the verified current inventory and keep the data model count-dynamic so an additional repository can be added without redesign.

The inventory changed recently when `synergy_agi_trader` appeared. This confirms that repository totals must be data-derived, not hard-coded.

Current Federation V5 lifecycle classification:

```text
CANONICAL  22
CANDIDATE  10
R&D        10
LEGACY     12
ARCHIVE     5
TOTAL      59
```

## 4. Positioning

### Primary identity

Russian:

```text
ЕВГЕНИЙ КОШТЕНКО
SYSTEM ARCHITECT · QUANT · AI · FINTECH · DISTRIBUTED SYSTEMS
```

English:

```text
EVGENIY KOSHTENKO
SYSTEM ARCHITECT · QUANT · AI · FINTECH · DISTRIBUTED SYSTEMS
```

Primary positioning statement:

```text
Создатель федерации специализированных систем,
где интеллект, рынки, платежи, бухгалтерия,
криптографический trust, сеть и приложения
разделены по полномочиям и соединены проверяемыми контрактами.
```

The message must emphasize architecture, research depth and engineering breadth rather than unsupported performance claims.

## 5. Information architecture

### 5.1 Hero

The hero must immediately show:

- Evgeniy Koshtenko;
- system architect positioning;
- verified repository estate count;
- public/private split;
- lifecycle distribution;
- primary domains;
- links to repository catalog, flagship systems and contacts.

Metrics are rendered from repository data rather than duplicated manually.

### 5.2 Repository Estate

Interactive status controls:

```text
ALL
CANONICAL
CANDIDATE
R&D
LEGACY
ARCHIVE
```

Domain controls:

```text
AI / AGENTS
TRADING
FINANCE / PAYMENTS
BLOCKCHAIN / TRUST
INFRASTRUCTURE
SCIENCE / RESEARCH
COMPRESSION
APPLICATIONS
ENGINEERING
REAL ECONOMY
```

Each repository card shows:

- repository name;
- short human-readable role;
- lifecycle;
- system kind;
- domain;
- visibility;
- canonical successor where applicable;
- public GitHub link only when repository is public;
- `PRIVATE / INTERNAL` treatment for private repositories;
- concise claim boundary.

Private source URLs must not be exposed as fake public source links.

### 5.3 SYNERGY System Map

The website must explain the architecture as a system of systems.

Top-level conceptual flow:

```text
User / Business
    ↓
Applications / Messenger / Portal
    ↓
AutoCompany / Autopilot / NEXUS
    ↓
MIDAS / MetaPay / Eurasian Project Factory
    ↓
Financial OS
    ↓
Evidence / Audit / Blockchain Commitments
```

Infrastructure underneath:

```text
SHTTPS
  ↓
SynergyNet
  ↓
Meta-OS
  ↓
TURBO Linux
```

Critical boundary statement:

```text
Repository
  != federation principal
  != trusted node
  != capability
  != authority
```

### 5.4 Flagship Systems

Prominent cards should be reserved for modern canonical or high-value systems, including:

- `synergy_system` — architecture and governance root;
- `synergy_financial_os` — canonical accounting / HardNAV authority;
- `synergy_pay_system` — payment routing and settlement;
- `midas_ai` — canonical institutional trading intelligence;
- `agi_nexus` — reasoning / inference / memory core;
- `agi_autopilot` — bounded business execution;
- `synergy_ai_company` — business orchestration / company control plane;
- `synergy_eurasian` — Real Economy OS / project factory;
- `nexus_science_agent` — evidence-oriented scientific workflow;
- `shttps` — post-quantum trust/session/RPC plane;
- `synergynet` — P2P/data-plane target;
- `synergy_meta_os` — runtime node orchestration;
- `turbo_linux` — host/capability substrate;
- `synergy_ai_blockchain` — commitment/provenance/blockchain trust layer;
- `ai_compress` — canonical compression technology;
- `ai_language` — repository-aware coding and semantic traceability;
- `synergy_messenger` — secure P2P messenger;
- `synergy_app` — SINERGY Finance store-release application.

These cards must show status and claim boundary, not marketing language that erases maturity differences.

### 5.5 Trading Research Lineage

Older trading repositories remain visible as provenance and R&D lineage feeding `midas_ai`.

Lineage includes:

- `quantum-trading_metatrader5`;
- `computer_vision_trading_metatrader_5`;
- `swap_arbitrage_metatrader_5`;
- `cross_forex_arbitrage_trading_metatrader_5`;
- `global_liquidity_dataminer`;
- `3D_bars_market_structure`;
- `multi_threaded_trading_robot_with_machine_learning_python`;
- `midas_ai_trading_system`;
- `midas_lite`;
- `ai_trade_terminal`;
- `algotrading_graph_system`;
- `crypto_pump`;
- `synergy_agi_trader`.

The site must explicitly distinguish historical/backtest claims from current canonical evidence.

No historical performance figure is promoted into a present-tense verified claim merely because it exists in an old README.

### 5.6 Frontier Research

Dedicated research section for high-uncertainty/high-upside work:

- `binary_quantum_theory`;
- `cold_nuclear`;
- `dlp_solver`;
- `motherboard_xpu_xml`;
- `qr_compress`;
- `synergy_graph_print_money`;
- `agi_olga`;
- `synergy_agi_trader`;
- `synergy_matrix_sota`;
- selected financial/AMM research lineage.

Research vocabulary:

```text
implemented
measured
reproduced
modeled
candidate
hypothesis
legacy
```

The site must not turn hypotheses into confirmed science.

### 5.7 Products / Applications

Separate product-facing systems from research:

- SINERGY Finance;
- SYNERGY Messenger;
- AI Language Pro;
- SYNERGYCHAIN portal/control surface;
- public presentation sites.

Application cards must state actual release maturity where known, e.g. Messenger alpha rather than production-ready.

### 5.8 Principles

A compact section must expose the engineering constitution:

```text
One authority per fact.
Evidence before authority.
AI proposes; deterministic policy constrains.
Internal movement is not external wealth.
Blockchain proves; it does not invent truth.
Presentation is not a second ledger.
No performance claim without reproducible evidence.
```

### 5.9 Full Repository Registry

All currently verified repositories appear in a searchable/filterable registry.

The registry is not optional.

It must support:

- text search;
- lifecycle filtering;
- domain filtering;
- public/private filtering;
- flagship-only filtering;
- canonical-successor lineage.

No repository is silently omitted because it is legacy, private or archival.

## 6. Technical architecture

The current single-file ~100 KB `index.html` has accumulated many appended `<style>` blocks and patch layers.

Portfolio A should remain a zero-build static GitHub Pages site but split responsibilities:

```text
index.html
assets/
  portfolio.css
  portfolio.js
data/
  repositories.json
docs/
  superpowers/
    specs/
      2026-09-18-portfolio-a-system-architect-design.md
```

No frontend framework is required.

Reasons:

- GitHub Pages remains trivial to deploy;
- repository data can evolve independently from layout;
- 60th/61st repository additions do not require editing HTML cards;
- status counts become computed values;
- filters/search stay data-driven;
- CSS becomes maintainable instead of layered overrides.

## 7. Repository data contract

Each repository record will include at least:

```json
{
  "name": "midas_ai",
  "visibility": "private",
  "lifecycle": "CANONICAL",
  "kind": "DOMAIN_SERVICE",
  "domain": "trading",
  "role_ru": "Канонический институциональный торговый интеллект",
  "role_en": "Canonical institutional trading intelligence",
  "flagship": true,
  "public_url": null,
  "canonical_successor": null,
  "claim_boundary_ru": "...",
  "claim_boundary_en": "..."
}
```

Counts are always derived with JavaScript from this dataset.

## 8. Visual system

Retain current identity:

- black background;
- white typography;
- neon green accent;
- monospace technical labels;
- large editorial display typography;
- subtle grid;
- restrained glow;
- bilingual RU/EN switch;
- motion with `prefers-reduced-motion` support.

Improve:

- fewer decorative patches;
- stronger information hierarchy;
- calmer hero;
- denser repository cards;
- clear status colors/patterns without making status solely color-dependent;
- mobile-first registry controls;
- architecture diagram that remains readable on narrow screens.

No visual redesign should make the portfolio look like a generic crypto landing page.

## 9. Claim-safety rules

The public portfolio must never silently promote:

- backtest result -> realized profit;
- internal AMM mark -> external wealth;
- research architecture -> production deployment;
- modeled throughput -> measured throughput;
- synthetic benchmark -> universal compression result;
- hypothesis -> scientific confirmation;
- private repository -> open-source project;
- test count -> security audit;
- alpha release -> production readiness.

Where the source repository itself contains stronger historical claims, the portfolio uses conservative summary language and points to the project lineage/status rather than repeating headline claims.

## 10. Link hygiene

Fix the current GitHub identity mismatch.

The portfolio repository estate is under:

```text
https://github.com/Shtenco
```

Do not keep a main portfolio CTA pointing to `github.com/koshtenko` unless separately verified as an intended second account.

Public repo cards link to their exact public repositories.

Private repos receive no fake public source link.

## 11. SEO / metadata

Update:

- title;
- meta description;
- Open Graph title/description;
- canonical URL;
- JSON-LD Person/CreativeWork or Person/SoftwareSourceCode graph where appropriate.

SEO language should focus on:

```text
Evgeniy Koshtenko
system architect
quantitative systems
AI agents
financial infrastructure
distributed systems
blockchain
post-quantum security
algorithmic trading
```

Do not put unsupported superlatives into metadata.

## 12. Accessibility and performance

Required:

- semantic landmarks;
- keyboard-accessible filters;
- visible focus states;
- `aria-pressed`/proper controls;
- reduced-motion support;
- sufficient text contrast;
- no interaction that depends only on hover;
- no heavy framework bundle;
- no remote image requirement for core page rendering;
- graceful rendering if JavaScript fails: hero, principles and key systems remain readable.

## 13. Testing

At minimum, add static verification that checks:

1. repository JSON parses;
2. repository names are unique;
3. current observed count is derived;
4. lifecycle is within the closed enum;
5. public repositories have valid GitHub URLs;
6. private repositories do not expose fake public-source URLs;
7. all repository records have RU/EN role text;
8. every flagship exists in the registry;
9. all filter values correspond to actual data;
10. page contains no hard-coded stale repository total;
11. old `github.com/koshtenko` primary link is removed or intentionally documented;
12. page HTML references the new data and asset files correctly.

## 14. Branch / merge rule

Implementation remains isolated on:

```text
feat/portfolio-system-2026
```

The site must not be merged into `main` without explicit human authorization.

A PR may be created after implementation and verification.

## 15. Success criteria

Portfolio A is complete when:

- all currently verified repositories are represented;
- counts are derived, not hard-coded;
- maturity/status is visible;
- flagship systems explain the modern architecture;
- legacy and R&D remain visible as lineage;
- the system map makes the federation understandable to a technical outsider;
- public/private handling is accurate;
- historical performance/science claims are not overstated;
- RU and EN both work;
- desktop and mobile layouts remain usable;
- repository data can absorb repository #60 without structural page changes.
