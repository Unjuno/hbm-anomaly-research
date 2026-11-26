# HBM Anomaly Research

**Forecasting where earlier capacity restrictions and shared-part manufacturing decisions may recur across accelerator generations and production cohorts.**

[日本語](README.ja.md) · [Current ranking](docs/current-ranking.md) · [Recurrence hypotheses](docs/recurrence-hypotheses.md) · [Capacity constraints](docs/capacity-constraints.md) · [Sources](docs/sources.md)

**v0.9.0 — 2026-11-26. Documentary forecasts; no original hardware measurements.** Precedents are positive inputs to candidate selection. Shared product purposes, part lineages and manufacturing incentives identify cohorts where similar decisions may have recurred. Forecast ranks and confirmed population, health or access remain separate fields.

## What we predict from precedents

A P104-100 owner described 8 GB installed with half disabled in 2018 [S84]. Pascal-based CMP 100-100 also has a later capacity-change report [S04a,S86]. The RX 480 retail experiment [S54] and CMP 170HX external research [S19] provide further references. **Recurrence of manufacturing and product-configuration decisions is a starting hypothesis for this research.** Architecture dates, board manufacturing dates and report dates are separate in the [precedent ledger](data/capacity_precedents.csv).

| Decision predicted to recur | Expected cohort pattern |
| --- | --- |
| Common parts with capacity set by product segment | Capacity settings cluster within compatible package/part lineages; recurrence need not be limited to a short shortage window |
| Temporary substitution of denser parts or completed packages | Part or revision groups differ physically while retaining the same advertised capacity |
| Grading already assembled packages into lower products | Shared assembly lineages differ in enabled regions or product grade |

These are forecasts, not established internal decisions by each manufacturer. Shared purpose, parts and applicable manufacturing conditions make the transfer from a precedent more concrete.

## Current forecast ranking

Tiers compare **how closely historical precedents support recurrence of capacity restriction or assembly substitution**. Candidates within a tier are tied. All 11 novel physical-population claims remain unconfirmed, while historical and mechanism evidence can still change their forecast ordering. Tiers are not recovery success rates or prevalence estimates.

| Tier / category | Candidates | Forecast rationale |
| --- | --- | --- |
| **1 — leading recurrence forecast** | **CMP 100-200 (~6 GB)** | External capacity-control reports exist on both the Pascal and Ampere sides of the same mining-oriented CMP line; recurrence in a Volta cohort is the closest product-purpose analogy |
| **2 — traceable product/part lineages, tied** | **A30; PG199 / DRIVE A100; A800 40 GB Active; CMP 100-210; AMD MI50 16 GB; H100 SXM5 64 GB HBM2e** | Shared architecture, product purpose or same-family capacity variants motivate concrete package/revision cohort predictions |
| **3 — additional transfer assumptions, tied** | H100 SXM5 80 GB; AMD RX Vega 56/64 8 GB; AMD/XFX BC-160; A30X | A different exclusion mechanism, distinct package, or unestablished high-density compatibility makes transfer from the precedents more indirect |
| **Documented physical reference** | **Intel GPU Max 1100** | Vendor documents four physical HBM stacks, three enabled 16 GB stacks and one permanently disabled; remaining density/health uncertainties are retained [S39] |
| **Watchlist** | H20A/H20; AMD MI308/MI308X; B200/B300; GB300 Desktop; Intel Max 1350; Ascend 910B4 | Link supply context, specification discrepancies and population evidence to a specific production pathway |

**[Read candidate-specific cohort predictions, competing explanations and rank-change conditions →](docs/current-ranking.md)**

v0.9 makes recurrence forecasting the main lens, replacing v0.8's physical-hypothesis specificity ordering. H100 64 GB moves 1→2, CMP 100-210 moves 3→2 and H100 80 GB moves 2→3. Prior values remain in CSV `v08_specificity_tier`. These are explicit judgment changes about historical transfer, not new capacity-recovery findings.

**Ordinary explanations have evidence levels too.** Identified target parts, documented family configurations and arithmetic-only constructions are different. A hypothetical low-density part does not erase a forecast merely because its capacity fits: rate, compatibility and period availability must also fit. Unseen ordinary constructions remain possible; an incomplete part search does not establish that they do not exist.

## Help narrow one hypothesis

**[Contribute one source, observation or counterexample →](docs/call-for-participants.md)**

Hardware ownership is optional. A manufacturer document, a memory-part mapping or a normal configuration that explains the figures can change the ranking. Existing owners can share an exact product/board identity and already-available memory information. Unknown fields are welcome.

- [Quick evidence / counterexample issue](https://github.com/Unjuno/hbm-anomaly-research/issues/new?template=quick-evidence.md)
- [Existing hardware observation](https://github.com/Unjuno/hbm-anomaly-research/issues/new?template=hardware-observation.md)
- [Contributing](CONTRIBUTING.md) · [Japanese participation guide](docs/call-for-participants.ja.md)

No purchase, disassembly or firmware change is needed to contribute. **A stock display matching the advertised capacity is inventory information, not a negative physical-capacity test.** Part-count/density evidence can instead support or contradict a specific unit's construction. Retain negative and uncertain results.

## What the theory adds

| Case | Sourced specification | Conditional deduction |
| --- | --- | --- |
| **A30** | 24 GB, 3072 data lanes [S06] | A uniform 8 GB-class model exposes the full capacity behind its active width. Extra capacity in that model would be behind inactive regions. A separate 16 GB-class model instead needs restricted capacity within active regions. |
| **AMD MI50 16 GB** | 16 GB, 4096 lanes; the normal 32 GB version has the same width [S38,S80] | A 4 GB-class density gives an ordinary explanation. An 8 GB-class assumption requires half exposure or another explanation within the active regions. Whole-stack disable alone cannot preserve this width while yielding 16 GB. |
| **H100 NVL** | 94 GB HBM3, 6016 lanes [S72] | With at most 1024 ordinary-data lanes per stack, at least six real stacks must supply the width. If each full native interface is exactly 1024 lanes, whole-stack-only on/off cannot produce this width. This does not establish 96 GB physically present [S82]. |

The densities above are **assumptions in construction models**, not identified parts on candidate units. Capacity conventions, reservations, per-channel payload and the meaning of active width must be matched. The [variables, derivations, countermodels and candidate constraints](docs/capacity-constraints.md) explain where each conclusion ceases to apply.

**The location of a supply constraint changes the prediction.** Substituting loose denser HBM does not automatically remove a bottleneck in the same packaging process. An already assembled compatible package might bypass that process. TSMC's 2023 statement distinguishes front-end supply from constrained CoWoS capacity; it does not document a particular GPU's reuse [S83]. Cohort explanations must distinguish when physical population, capacity configuration and commercial allocation became irreversible.

**No price-based ranking adjustment.** Comparable transaction series are missing. Publication itself could affect attention and prices, so later price responses, reposts and circular citations are not independent technical corroboration.

## Research materials

| Read | Purpose |
| --- | --- |
| [Current ranking](docs/current-ranking.md) / [CSV](data/current_ranking.csv) | One current comparison: 11 predictions plus references and watches; 26 entries |
| [Recurrence hypotheses](docs/recurrence-hypotheses.md) / [Precedent ledger](data/capacity_precedents.csv) | Historical cases, reusable decisions and cohort-specific forecasts |
| [Capacity constraints](docs/capacity-constraints.md) | Variable tables, conditional proofs, rejected construction models and candidate-specific implications |
| [Manufacturing causes](docs/manufacturing-causality.md) | Bottleneck location, irreversible decisions, defect grading versus commercial restrictions |
| [v0.7 deductions](docs/inference-refinement.md) | Background on address-space versus disabled-stack mechanisms and evidence |
| [Physical model](docs/theory.md) | Variables, units, derivations and why specifications do not identify the physical population |
| [Manufacturing history](docs/lot-history.md) / [Market evidence](docs/market.md) | Conditional substitution economics, dated context and price confounders |
| [Data dictionary](data/README.md) / [Sources](docs/sources.md) | Provenance and the distinction between observations and predictions |
| [Participation](docs/call-for-participants.md) | Contributing sources, counterexamples and existing observations |
| [Optional owner protocol](docs/validation.md) / [Study design](docs/study-design.md) | Interpreting actual hardware evidence; not a prerequisite for theoretical contributions |

The offline screen checks nominal geometry only; it does not compute the ranking or a success probability. Python 3.10+, standard library, no GPU or network:

```sh
python3 tools/screen.py --input data/devices.csv
python3 -m unittest discover -s tests -v
```

## History and license

Earlier analyses remain readable as **historical snapshots**: [v0.4](docs/candidates.md), [v0.5 cross-vendor](docs/cross-vendor-ranking.md), [v0.6 historical leads](docs/historical-trigger-screen.md). Their different ordinal meanings are superseded by the current table; see [changelog](CHANGELOG.md).

Original documentation and code use the [MIT license](LICENSE). External material retains its own rights. This is independent research; share sources and observations you are entitled to publish, with personal identifiers removed.
