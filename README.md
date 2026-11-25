# HBM Anomaly Research

**A public, explicitly speculative ranking of GPUs that may contain additional healthy HBM beyond their advertised capacity.**

[日本語](README.ja.md) · [Detailed ranking](docs/candidates.md) · [Ranking method](docs/ranking-method.md) · [Physical theory](docs/theory.md) · [Manufacturing history](docs/lot-history.md) · [Sources](docs/sources.md)

**v0.4.0 — 2026-11-25. Desk research; no original hardware measurements.** Our main output is a reasoned prediction: what looks suspicious, why, what ordinary explanation competes with it, and what would change the order. Hardware ownership is not required to contribute a better hypothesis or source.

## Current hypothesis ranking

The ranked hypothesis is that **some units already contain ordinary-data HBM beyond the nominal capacity, with some additional capacity still healthy but unexposed**. Software accessibility, stable application use, market prevalence and purchase value are separate questions. All candidates remain unconfirmed; first place is relative, not high confidence.

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
