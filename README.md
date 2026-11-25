# HBM Anomaly Research

**Which accelerators might contain more HBM than their advertised capacity? A public, explicitly speculative comparison of hardware, product history and production cohorts.**

[日本語](README.ja.md) · [Current ranking](docs/current-ranking.md) · [Capacity constraints](docs/capacity-constraints.md) · [Manufacturing causes](docs/manufacturing-causality.md) · [Sources](docs/sources.md)

**v0.8.0 — 2026-11-26. Desk research; no original hardware measurements.** We explain what looks suspicious, the physical construction required, the ordinary alternative, and the information that would change the prediction. Physical population, healthy capacity and usable capacity are evaluated separately.

This edition identifies **which explanations fail and which conditions the remaining explanations require**. We derive a conditional stack-count lower bound from active width and separate inactive-channel capacity from unexposed capacity inside active channels under stated density assumptions. The rank tiers stay unchanged; the next documentary questions become more specific.

## Current shortlist

Ranks are **tied qualitative tiers of the specificity of a physical-excess hypothesis**. They are not recovery probabilities. All 11 new predictions remain unconfirmed; even the first tier is weak.

| Rank tier / category | Candidates | Why they belong here |
| --- | --- | --- |
| **1 — leading hypotheses, tied** | **H100 SXM5 64 GB HBM2e; CMP 100-200 (~6 GB)** | A specific same-family 64/94 GB HBM2e comparison; or a low-capacity mining configuration and external CMP capacity-control analogies. |
| **2 — weak package/density hypotheses, tied** | A30; PG199 / DRIVE A100; **AMD MI50 16 GB**; A800 40 GB Active; H100 SXM5 80 GB | Concrete population/density questions, but ordinary constructions already explain the nominal capacities. |
| **3 — additional assumptions, tied** | AMD RX Vega 56/64 8 GB; CMP 100-210; AMD/XFX BC-160; A30X | Further compatibility, transfer or topology assumptions are required; some apparent clues concern performance rather than capacity. |
| **Documented physical reference** | **Intel GPU Max 1100** | Four HBM stacks physically present, three enabled 16 GB stacks; one permanently disabled. The fourth density and health remain unestablished [S39]. |
| **Watchlist** | H20A/H20; AMD MI308/MI308X; B200/B300 capacity labels; GB300 Desktop; Intel Max 1350; Ascend 910B4 | Supply events, SKU/accounting discrepancies or missing topology need to be linked to an actual physical variant before promotion. |

**[Read the complete current ranking, conditional capacities, counterarguments and rank-change conditions →](docs/current-ranking.md)**

Intel's documented disabled stack does not make it the best recovery prospect. A 64 GB physical total assumes that its fourth stack is also 16 GB. External CMP 170HX/CMP 100-100 reports and the historical AMD RX 480 GDDR5 case are separate references, not discoveries by this project. We make no current-inventory or price-rise claim. All source IDs are in the [source register](docs/sources.md).

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
| [Current ranking](docs/current-ranking.md) / [CSV](data/current_ranking.csv) | One current comparison: 11 predictions plus references and watches; 25 entries |
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
