# HBM Anomaly Research

**Forecasting unexposed HBM by asking whether ordinary parts can simultaneously explain a device's capacity, bandwidth and physical constraints.**

[日本語](README.ja.md) · [Current assessment](docs/current-ranking.md) · [Inference and proof](docs/diagnostic-inference.md) · [Part constraints](data/hbm_part_constraints.csv) · [Sources](docs/sources.md)

**v0.11.0 — 2026-11-26. Public-source research; no original hardware measurements.**

## Historical investigation: specific pathways and comparison groups

**v0.11 adds 18 source entries connecting market changes, capacity-variant introductions and supply plans to particular hypotheses.** Existing documents can predict which package or configuration differences should appear across a transition, without our owning the hardware.

| Investigation focus | What became more specific |
| --- | --- |
| **Later GA100 / A800 products** | NVIDIA disclosed China Data Center-related inventory charges and alternative A800 sales in late 2022. This supplies a specific motive to investigate qualified-package reassignment; the memory content and manufacturing stage of the inventory remain unknown [S96,S99] |
| **MI50 16 / 32 GB variants** | An attributable 2019 AMD statement explains adding the 32 GB product. Compare factory-16 GB cohorts with dated capacity-variant packages; ordinary 4 GB parts and a legitimate 32 GB sales outlet remain alternatives [S103,S104,S101] |
| **RX Vega, late 2017–2018** | Samsung's high-density expansion plan and SK hynix's HBM2 supply plan define a useful interval for supplier/package comparison. Neither surplus high-density stock nor a target implementation change is established [S47,S100] |

Conversely, A30X already had a product plan in 2021, and ordinary 8 GB comparison products for BC-160 existed in 2020. Later shortages or repurposing do not require hidden higher-density memory [S97,S105,S109]. These findings update manufacturing-pathway plausibility and comparison groups; an excess-capacity ranking still needs target-specific capacity, throughput or part evidence.

[Full historical analysis](docs/historical-context.md) · [11-candidate update CSV](data/history_assessments.csv) · [Events with distinct date types](data/supply_events.csv)

## The v0.10 correction

The previous tiers 1–3 primarily ranked similarity of product purpose, architecture and historical precedents. They did not establish which target observation was better explained by excess memory than by an ordinary assembly. **We withdraw the tiers for all 11 novel hypotheses.** Earlier values remain in `v09_recurrence_tier` and Git history.

A concrete counterexample is SK hynix's 2016 presentation listing **2 GB, 1024-data-lane HBM2 with speeds up to 2.0 Gb/s** [S93]. Three such parts provide an ordinary capacity model for the approximately 6 GB CMP 100-200 report [S05]. Excluding 2 GB parts and calling 6 GB anomalous because it is not a sum of 4 GB parts would ignore this evidence. The document does not establish qualification or adoption on the target card.

## What makes a candidate suspicious?

**Which target-specific observation becomes difficult to explain if the card contains only its ordinary advertised memory capacity?**

| Case | Present assessment |
| --- | --- |
| **CMP 170HX: conditional historical reference** | The 2023 review's 8 GiB-class capacity, 4096 lanes and high measured throughput are difficult to satisfy together with the published low-density parts at their stated rates. A larger assembly with partial exposure has an explanatory role [S87,S93] |
| **CMP 100-200, PG199, H100 64 GB** | Target part, width or bandwidth inputs are incomplete. Small capacity or a shared family does not establish an excess-memory ordering |
| **A30X, MI50 16 GB, RX Vega, BC-160, A30, A800 Active, CMP 100-210** | Ordinary capacity, rate or population models remain. A30X and MI50 specifically have simultaneous capacity-and-bandwidth models using manufacturer-described part classes [S01,S90] |
| **H100 80 GB** | The sixth site's material is the unresolved topology question. Appearance and full-die design do not identify extra DRAM |
| **Intel Max 1100: documented physical reference** | The vendor describes four physical stacks, three enabled 16 GB stacks, and one permanently disabled stack. Health and recovery are separate claims [S39] |

These categories are not success probabilities. **Current evidence does not support ordering the 11 new hypotheses by likelihood of hidden capacity.** We separate ordinary fits, missing inputs and a topology question rather than filling the gaps with resemblance. Forecasting remains the objective: specify observations and counterexamples that distinguish the competing explanations.

## Why the 170HX comparison is different

The owner review reports clpeak throughput of 1165.79–1355.40 GB/s across vector widths [S87]. Four 2 GB, 2.0 Gb/s parts explain an 8 GB-class capacity and 4096 lanes but reach only a calculated 1024 GB/s [S93]. Four faster 8 GB-class parts can instead support the throughput with more physical capacity [S01].

This is a mismatch relative to a declared public part set. Unlisted fast low-density parts, operation above published ratings and benchmark accounting remain alternatives. The [inference document](docs/diagnostic-inference.md) includes a sensitivity case allowing a research-reported 2.4 Gb/s rate on 2 GB parts, measurement-condition gaps, exact units and the conditional capacity lower-bound proof. This comparison does not select 32 versus 64 GB or establish healthy, recoverable memory.

By contrast, MI50's 16 GB and roughly 1 TB/s fit four ordinary 4 GB, 256 GB/s HBM2 parts of the class announced in production in 2016. A30X's 24 GB and 1223 GB/s also fit a model using three 8 GB, 3.2 Gb/s HBM2E parts described in 2021 [S90,S01,S38,S10]. **A larger bandwidth/capacity ratio than another GPU is not sufficient evidence of an anomaly.**

## Next documentary investigation

First, look for **part, active-width and bandwidth records tied to the same approximately 6 GB CMP 100-200 unit**. A width of 3072 lanes alone would still fit three ordinary 2 GB parts. It must be assessed together with throughput or the part's speed grade. This is a documentary investigation choice, not an excess-capacity probability ranking.

History, cohorts and supply conditions still matter. Link them to compatible parts, the manufacturing stage at which a decision remained possible, a supported time window and a reason substitution would be preferable to ordinary assembly. A shared generation, a general shortage, or an unspecified alternative lot is not enough to elevate a candidate. Normal specifications also do not prove the absence of additional inactive parts; that branch needs its own population evidence.

No price-based adjustment is applied: comparable transaction histories are insufficient. Post-publication price changes or reposts are not independent technical corroboration.

## Participate and read

Hardware ownership is optional. Original specifications, existing reviews, part identities and ordinary counterexamples all help.

- [Submit evidence, a counterexample or a correction](https://github.com/Unjuno/hbm-anomaly-research/issues/new?template=quick-evidence.md)
- [Participation guide](docs/call-for-participants.md) · [Contributing](CONTRIBUTING.md)
- [Individual assessments and references](docs/current-ranking.md) · [Current CSV](data/current_ranking.csv)
- [Proof and falsification conditions](docs/diagnostic-inference.md) · [Part capacities and speeds](data/hbm_part_constraints.csv)
- [Historical performance records](docs/performance-gap.md) · [Observation ledger](data/performance_gap_observations.csv)
- [Capacity and width constraints](docs/capacity-constraints.md) · [Manufacturing causes](docs/manufacturing-causality.md)
- [Historical hypotheses](docs/recurrence-hypotheses.md) · [Lot history](docs/lot-history.md) · [Market evidence](docs/market.md)
- [Data dictionary](data/README.md) · [Sources](docs/sources.md) · [Changelog](CHANGELOG.md)

The existing `tools/screen.py` is a descriptive nominal-ratio tool. It is not the new constraint test and does not calculate predictions or rankings. Python 3.10+, standard library only; no GPU or network required.

```sh
python3 tools/screen.py --input data/devices.csv
python3 -m unittest discover -s tests -v
```

Original writing and code use the [MIT license](LICENSE). External material retains its original rights. Participation does not require buying hardware, disassembly or firmware changes.
