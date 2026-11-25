# HBM Anomaly Research

**A public, explicitly speculative ranking of GPUs that may contain additional healthy HBM beyond their advertised capacity.**

[日本語](README.ja.md) · [Detailed ranking](docs/candidates.md) · [Ranking method](docs/ranking-method.md) · [Physical theory](docs/theory.md) · [Manufacturing history](docs/lot-history.md) · [Sources](docs/sources.md)

**v0.5.0 — 2026-11-26. Desk research; no original hardware measurements.** Our main output is a reasoned prediction: what looks suspicious, why, what ordinary explanation competes with it, and what would change the order. Hardware ownership is not required to contribute a better hypothesis or source.

> **v0.5.0 (2026-11-26) — expanded cross-vendor lead ranking.** The previous NVIDIA-only ranking suffered from selection bias. Intel Max 1100 has manufacturer-documented physically present disabled HBM; AMD RX 480 provides a historical, non-HBM supply/lot precedent. [Expanded analysis](docs/cross-vendor-ranking.md) · [日本語](docs/cross-vendor-ranking.ja.md) · [CSV](data/cross_vendor_leads.csv). Investigation priority is not the probability of healthy extra memory or software recovery.

| Priority | Candidate | Nominal capacity | Conditional total / physical finding | Why suspicious | Strongest alternative / limitation |
| ---: | --- | --- | --- | --- | --- |
| 1 | Intel GPU Max 1100 | 48 GB | 64 GB if fourth stack is 16 GB; 16 GB inactive | Official datasheet identifies four physical stacks, three enabled 16 GB stacks; inactive position varies. | Permanent disable and possible yield harvesting; no evidence of a healthy or recoverable fourth stack. |
| 2 | NVIDIA CMP 100-200 | ~6 GB class | 12 GB class if larger assembly exists | Low-capacity Volta mining SKU and prior CMP capacity-limit precedent. | Actual width/density unknown; normal low-density or partially active assembly. |
| 3 | NVIDIA A30 | 24 GB | 32 or 40 GB class if additional 8 GB-class regions populated | Reduced GA100 memory configuration permits shared-package hypothesis. | Ordinary 24 GB population or defective excluded regions; compute recovery is not memory recovery. |
| 4 | NVIDIA DRIVE A100 / PG199 | 32 GB class reported | 64 GB class if four 16 GB-class stacks populated | OEM-specific GA100 configuration and possible package reuse. | Ordinary four-by-8 GB assembly; count/density unverified. |
| 5 | AMD Instinct MI50 16 GB | 16 GB | 32 GB class if four 8 GB-class stacks populated | Vendor lists 16 and 32 GB MI50 with the same 4096-bit interface and 1 TB/s bandwidth; known 32 GB assembly in same SKU family. | Ordinary 4 GB stacks explain 16 GB; FRU-name mismatch is not a stock access restriction; refurbished boards may differ. |
| 6 | AMD RX Vega 56 / 64 8 GB | 8 GB | 16 GB class if two 8 GB-class stacks populated | Common PCB with 16 GB Vega Frontier Edition; 2017 documented HBM2 production expansion and reported supply/yield difficulties. | Teardown reports different soldered packages; normal two-by-4 GB assembly; high-density HBM also scarce. |
| 7 | NVIDIA CMP 100-210 | 16 GB class | 32 GB class only if higher-density assembly exists | Distinct board/firmware families provide a concrete cohort axis. | Investigated 1df4 unit has ordinary 16 GB V100 origin; performance improvement is not capacity gain. |
| 8 | AMD / XFX BC-160 | 8 GB | 16 GB class only if two 8 GB-class stacks populated | 2021 Navi 12 HBM2 mining product; relevant market context. | 8 GB / 2048-bit ordinary; official V520 comparator also 8 GB; no verified shipping 16 GB Navi 12 counterpart in reviewed sources. |
| 9 | NVIDIA A30X | 24 GB | 48 GB class if three 16 GB-class stacks and partial exposure | Special converged HBM2e SKU and hypothetical density substitution. | Ordinary 8 GB-class HBM2e explains capacity/bandwidth; width/density not established. |

The Intel case has a documented physical surplus; the fourth stack's 16 GB size is a conditional inference, and Intel describes it as permanently disabled. The other rows remain unverified predictions. See the expanded analysis for sources, ordinary alternatives and watchlist. No price-based adjustment.

## Historical NVIDIA-only hypothesis ranking (v0.4.0)

The ranked hypothesis is that **some units already contain ordinary-data HBM beyond the nominal capacity, with some additional capacity still healthy but unexposed**. Software accessibility, stable application use, market prevalence and purchase value are separate questions. All five historical NVIDIA predictions remain unconfirmed; first place is relative, not high confidence.

Capacity scenarios below are **conditional nominal total-capacity classes**, not measured capacities, expected values or ceilings.

| Rank | Candidate | Our prediction | Conditional total capacity | Strongest ordinary explanation |
| ---: | --- | --- | --- | --- |
| **1** | **CMP 100-200** | Some roughly 6 GB-class Volta mining units may expose only part of a larger HBM configuration | **12 GB class**, if the actual assembly contains that capacity | Unknown width/density; lower-density parts, partial channels or defect harvesting can explain the stock capacity |
| **2** | **A30** | Some GA100-derived packages may retain additional healthy memory regions outside the advertised 24 GB | **32 GB**, then **40 GB class**, if one or two additional 8 GB-class regions exist | Official 24 GB / 3072-bit geometry is ordinary; extra parts may be absent or defective |
| **3** | **PG199 / DRIVE A100** | Some OEM cohorts may use higher-density HBM while retaining a 32 GB-class configuration | **64 GB class** if four 16 GB-class stacks are actually populated | An ordinary four-by-8 GB configuration fits; both actual stack count and high density are unverified |
| **4** | **CMP 100-210** | Different board families leave a weak possibility of higher-density cohorts | **32 GB class** only if a higher-density assembly is established | The studied 1df4 unit has an ordinary V100 16 GB origin; compute/link/clock gains are not capacity gains |
| **5** | **A30X** | A particular HBM2e part/cohort might contain higher-density memory restricted to 24 GB | **48 GB class** if three 16 GB-class stacks and partial exposure are present | Ordinary 8 GB-class HBM2e and faster signaling explain the bandwidth; width is not sourced |

**A30 and PG199 belong to the same weak tier; ranks 2 and 3 can readily reverse.** The detailed cards separate vendor facts, owner observations, our inference, required assumptions, lot scenarios, counterarguments and rank-change conditions. Main sources: CMP 100-200 [S02,S05,S32,S33]; A30 [S06,S34,S35]; PG199 [S12]; CMP 100-210 [S04,S14,S33]; A30X [S01,S10]. See the [source register](docs/sources.md).

CMP 170HX and CMP 100-100 are **external reported controls**, not new predictions in this ranking [S03,S04a,S16]. Ordinary A100, P100/V100 and AMD MI50/MI60 configurations are comparison/watchlist cases. Read the [full candidate cards and watchlist](docs/candidates.md) or the [Japanese ranking](docs/ranking.ja.md).

## Why this order?

We compare capacity-specific clues, a concrete pathway to partial exposure or package reuse, the strength of ordinary configurations, and the number of unverified assumptions. We publish pairwise reasoning instead of an arbitrary points total or an invented success probability. The current ordering is an analyst judgment that can be challenged with a different weighting of the same evidence.

CMP 100-200 combines a capacity-specific low-capacity report with related 12 GB Volta configurations and the prior-generation CMP capacity-control analogy. A30 and PG199 rely more heavily on unverified package or density hypotheses. CMP 100-210's reported gains concern performance, while A30X's bandwidth is readily explained without extra capacity. The [ranking method](docs/ranking-method.md) explains these comparisons, including why the A30/A100 distinction is judgment-dependent.

## Physical and manufacturing background

Capacity and bandwidth are not interchangeable. Different HBM densities can share the same external width and signaling rate [S01]. A small capacity-per-width proxy can motivate a hypothesis, but ordinary low-density parts or partial channels may explain it. A normal proxy does not disprove extra physical memory. The [physical model](docs/theory.md) includes variables, units, derivations and a constructive non-identifiability proof.

Supply constraints can make an available, qualified higher-capacity package economical to reuse, even while keeping the original SKU specification. Compatibility, qualification cost and the value of using that package elsewhere matter. Corporate shortages alone do not identify a particular BOM substitution or distinguish two candidates [S21,S22]. The [lot-history model](docs/lot-history.md) separates dates, mechanisms and evidence. The [Japanese framework](docs/research-framework.ja.md) connects the theory to the predictions.

**Price-based rank adjustment: none in this release.** Comparable transaction time series are missing. A single ask, sold counter or listing disappearance cannot establish a price trend or private capacity discovery. See [market evidence](docs/market.md).

## Read or reuse the analysis

- [Detailed English hypothesis ranking](docs/candidates.md) / [日本語の予想ランキング](docs/ranking.ja.md)
- [Ranking method and sensitivity](docs/ranking-method.md)
- [Hypotheses as CSV](data/hypotheses.csv): predictions, assumptions, alternatives and revision conditions
- [Sourced configuration data](data/devices.csv) and [data dictionary](data/README.md)
- [Source register](docs/sources.md) and [release history](CHANGELOG.md)

The offline script checks nominal geometry only. It does **not** calculate the hypothesis ranking or a success probability. Python 3.10+, standard library, no GPU or network required:

```sh
python3 tools/screen.py --input data/devices.csv
python3 -m unittest discover -s tests -v
```

## Contribute a source or a better prediction

Use the **New candidate / prediction / source correction** issue template to challenge a reason, propose a candidate or supply a missing document. State what is observed and what you infer. A good contribution can be a normal low-density explanation, a part-number mapping, a historical catalog or a better reason to change two ranks. See [contributing](CONTRIBUTING.md).

Existing hardware owners can optionally contribute observations using the [validation protocol](docs/validation.md), [study design](docs/study-design.md) and other issue templates. These are supporting resources for testing predictions; completing a hardware study is not a prerequisite for publishing a reasoned hypothesis. See the [participation page](docs/call-for-participants.md).

Original code and documentation are [MIT-licensed](LICENSE); external material retains its own rights. This is independent research. Public evidence should omit personal identifiers, proprietary firmware and operational security-bypass details.
