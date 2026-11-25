# HBM Anomaly Research

**Which accelerators might contain more HBM than their advertised capacity? A public, explicitly speculative comparison of hardware, product history and production cohorts.**

[日本語](README.ja.md) · [Current ranking](docs/current-ranking.md) · [Theory](docs/inference-refinement.md) · [Sources](docs/sources.md)

**v0.7.0 — 2026-11-26. Desk research; no original hardware measurements.** We explain what looks suspicious, the physical construction required, the ordinary alternative, and the information that would change the prediction. Physical population, healthy capacity and usable capacity are evaluated separately.

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

Two different mechanisms deserve different questions: a higher-density stack could expose only part of its address space; or a physically populated stack/channel could be disabled. Micron's HBM2E addressing description and Intel's physical-stack documentation ground those mechanisms, without proving either is reversible on a candidate [S01,S39].

A shortage can motivate substitution only at a relevant manufacturing stage and with qualified, economically usable material. A later sale date does not date the HBM assembly. H20's disclosed material reuse does not identify HBM or a destination SKU [S65].

**No price-based ranking adjustment.** Comparable transaction series are missing. Our own publication could affect attention and prices, so a later price response is not independent technical corroboration. Reposts and circular citations do not create additional original observations.

## Research materials

| Read | Purpose |
| --- | --- |
| [Current ranking](docs/current-ranking.md) / [CSV](data/current_ranking.csv) | One current comparison: 11 predictions plus references and watches; 25 entries |
| [New deductions](docs/inference-refinement.md) | Address-space versus disabled-stack mechanisms, process-stage logic and inference limits |
| [Physical model](docs/theory.md) | Variables, units, derivations and why specifications do not identify the physical population |
| [Manufacturing history](docs/lot-history.md) / [Market evidence](docs/market.md) | Conditional substitution economics, dated context and price confounders |
| [Data dictionary](data/README.md) / [Sources](docs/sources.md) | Provenance and the distinction between observations and predictions |
| [Participation](docs/call-for-participants.md) / [X introduction drafts](docs/outreach.md) | Specific evidence requests and a shareable project introduction |
| [Optional owner protocol](docs/validation.md) / [Study design](docs/study-design.md) | Interpreting actual hardware evidence; not a prerequisite for theoretical contributions |

The offline screen checks nominal geometry only; it does not compute the ranking or a success probability. Python 3.10+, standard library, no GPU or network:

```sh
python3 tools/screen.py --input data/devices.csv
python3 -m unittest discover -s tests -v
```

## History and license

Earlier analyses remain readable as **historical snapshots**: [v0.4](docs/candidates.md), [v0.5 cross-vendor](docs/cross-vendor-ranking.md), [v0.6 historical leads](docs/historical-trigger-screen.md). Their different ordinal meanings are superseded by the current table; see [changelog](CHANGELOG.md).

Original documentation and code use the [MIT license](LICENSE). External material retains its own rights. This is independent research; share sources and observations you are entitled to publish, with personal identifiers removed.
