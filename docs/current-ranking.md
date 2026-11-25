# Current ranking of HBM hypotheses

[日本語](current-ranking.ja.md) · [Home](../README.md) · [Capacity constraints](capacity-constraints.md) · [Manufacturing causes](manufacturing-causality.md) · [Sources](sources.md) · [CSV](../data/current_ranking.csv)

**v0.8.0 — 2026-11-26. Desk research; no original hardware measurements.**

## 1. What this ranking means

We predict which named accelerator configurations could contain ordinary-data HBM beyond their advertised capacity, and explain the construction that would make that prediction true. The eventual question is whether any excess is healthy and usable. Those additional claims currently lack direct evidence for every new prediction below.

**Ranks 1–3 are tied, qualitative tiers of how specifically the current evidence motivates a physical-excess hypothesis.** They are our comparative judgment, not measured likelihoods, availability, buying recommendations or recovery success rates. Within a tier the evidence does not support a finer order. A rank-1 hypothesis is still weak. If one requires evidence of *healthy* excess before ordering candidates, the novel hypotheses cannot presently be ranked by that criterion.

The judgment favors a capacity-specific lead or an identifiable same-family comparison over a generic shortage story, and favors a concrete package/density mechanism over an unspecified larger-memory possibility. Ordinary configurations, evidence quality and missing compatibility assumptions count against a hypothesis. This is not a points formula. The reasons below make the judgment reviewable.

**Why v0.8 preserves the tiers:** the new deductions are necessary conditions for existing specifications and explicitly assumed parts to coexist. They do not identify a candidate's actual parts or a new production cohort. The mechanism section below and CSV `mechanism_constraint` field make the hypotheses more specific; mathematical narrowing is not an increase in discovery probability.

| Evidence question | Status for all 11 new predictions |
| --- | --- |
| Extra ordinary-data HBM physically populated on the target lower-capacity variant? | Not established |
| Some extra capacity healthy under stated conditions? | Not established |
| Extra capacity accessible and reliably usable? | Not established |
| A favorable production cohort or its prevalence identified? | Not established |
| Ranking affected by a validated price trend? | No |

Nominal GB-class scenarios below are **conditional total constructions**, not measured totals, recoverable quantities, expected values or maxima. A source supports the stated input, not our forecast. Reference densities are not universal minimum part sizes.

## 2. Unified prediction table

| Rank tier | Candidate and baseline | Why the hypothesis is concrete | Conditional construction | Strongest ordinary explanation | One fact that would change the assessment |
| ---: | --- | --- | --- | --- | --- |
| 1 | **H100 SXM5 64 GB HBM2e** — 64 GB | Official 64 and 94 GB HBM2e partner-cooled board configurations make a specific same-family comparison possible. [S60,S61,S62,S64] | 80/96 GB class only if five/six real 16 GB-class stacks are present; neither population is established. | Four 16 GB-class stacks can explain 64 GB normally; extra sites could be absent, dummy or defective. | A vendor/OEM package population map or existing owner evidence distinguishing four real stacks from five/six; not a virtual 64 GB allocation. |
| 1 | **CMP 100-200** — ~6 GB class | A low-capacity Volta mining configuration plus external CMP capacity-restriction precedents motivates a capacity-specific analogy. [S02,S04a,S05,S32,S36] | 12 GB class if a larger compatible assembly was actually populated and partly exposed. | Actual width and density are unknown. Low-density HBM or partial channels can explain the report; 12 GB TITAN V is not proof of a shared package. | Memory part/density and population evidence tied to the same identified ~6 GB board; another copy of the stock log adds no independent observation. |
| 2 | **A30** — 24 GB | A reduced GA100 derivative permits a completed-package reuse or disabled-region hypothesis. [S06,S34,S35] | 32/40 GB class if one/two additional 8 GB-class regions are populated. | Three active 8 GB-class stacks explain the official 24 GB / 3072-lane configuration. Compute-block recovery did not establish extra HBM. | Reliable actual memory population beyond the ordinary three-stack model, with dummy parts and repair history resolved. |
| 2 | **DRIVE A100 / PG199** — 32 GB class reported | OEM-specific GA100 packaging leaves a concrete density/reassignment question, but no extra part has been identified. [S12,S35] | 64 GB class only if four 16 GB-class stacks are actually present. | For example, four 8 GB-class stacks already explain 32 GB; actual count and density remain unresolved. | An original OEM package/part mapping showing density on the reported 32 GB configuration. |
| 2 | **Instinct MI50 16 GB** — 16 GB | Both 16 and 32 GB same-family configurations are documented; this bounds a plausible density-substitution question. [S38,S42,S43,S44,S80] | 32 GB class if four 8 GB-class stacks were used while only 16 GB remained exposed. | Four 4 GB-class stacks suffice. Both official capacities share width and bandwidth, which is normal; a stale FRU label is not a capacity restriction. | HBM part identification on a traceable stock 16 GB unit, not a 16 GB name attached to a card already exposing 32 GB. |
| 2 | **A800 40 GB Active** — 40 GB | A late GA100 derivative after higher-capacity family members permits a reuse hypothesis; chronology alone does not establish reuse. [S25,S35,S60,S71] | 48 GB class if a sixth 8 GB-class region exists; 80 GB class requires five compatible 16 GB-class stacks and partial exposure. | Five 8 GB-class stacks fit the official 40 GB / 5120-lane specification. Higher-density HBM2e compatibility is unverified. | Package-part compatibility and population for the actual board; an 80 GB two-board NVLink total does not qualify. |
| 2 | **H100 SXM5 80 GB** — 80 GB | A six-interface full design and an external package-site report leave a question about the sixth site. [S62,S63,S64] | 96 GB class only if six real 16 GB-class HBM stacks are present. | Five active 16 GB-class stacks explain 80 GB. A sixth visible package/site need not be DRAM or healthy. | Identification of the sixth site as a real memory stack versus a spacer/dummy, then its density; health remains separate. |
| 3 | **RX Vega 56 / 64 8 GB** — 8 GB | Related 16 GB Frontier Edition and 2017 supply context motivate a qualified-package substitution question. [S45,S46,S47,S48,S49] | 16 GB class if two 8 GB-class stacks were populated with partial exposure. | Two 4 GB-class stacks explain 8 GB; board analysis reports different soldered packages despite shared PCB. High-density parts were also seeing rising demand; their surplus availability for substitution is not established. | A factory-origin RX package with higher-density memory identification; PCB similarity alone is insufficient. |
| 3 | **CMP 100-210** — 16 GB class | Distinct board families permit cohort hypotheses, while reported gains so far concern performance rather than additional capacity. [S04,S08,S14,S33] | 32 GB class only for an independently identified higher-density assembly. | An ordinary V100-derived 16 GB assembly explains the known configuration. | Actual high-density memory parts on an identified 16 GB variant, rather than extra compute units or link speed. |
| 3 | **XFX BC-160** — 8 GB reported | HBM-equipped mining derivative fits the product-segmentation mechanism in principle. [S50,S51,S52] | 16 GB class only if two compatible 8 GB-class stacks were populated. | Ordinary 8 GB / 2048-lane configurations exist; a shipped 16 GB Navi 12 counterpart has not been established in the reviewed evidence. | A compatible higher-density production part/package reference tied to BC-160. |
| 3 | **A30X** — 24 GB | A special HBM2e converged product permits a density substitution hypothesis, but the width is not sourced. [S01,S10,S11] | 48 GB class if three compatible 16 GB-class stacks exist with partial exposure. | Three 8 GB-class stacks and faster signaling can explain the capacity/bandwidth; that is a model, not a measured topology. | Sourced effective width plus actual memory part/population; bandwidth alone does not identify density. |

### Mechanisms narrowed in v0.8

These are conditional consequences of the [channel-partition model](capacity-constraints.md). They require common capacity units, ordinary-data versus reservation accounting, and assumptions about payload per channel. The densities are not identified parts on candidate units.

| Candidate | Explanation narrowed | Most useful next documentary input |
| --- | --- | --- |
| A30 [S06] | A uniform 8 GB-class model exposes all 24 GB behind its active width, so excess in that model belongs to inactive regions. A 16 GB-class model needs partial exposure within active regions. Native ECC alone cannot explain a 32-to-24 GB payload reduction under the product's stated accounting. | A package mapping establishing both count and density. |
| MI50 16 GB [S38,S80] | At 4096 lanes with uniform 8 GB-class density, whole-stack disable alone cannot produce 16 GB. A reduction within active regions is needed. A 4 GB-class density remains an ordinary explanation. | Original 16 GB package-part density; another mention of the normal 32 GB product is insufficient. |
| A800 40 GB Active [S71] | At 5120 lanes, an 8 GB-class density fits full exposure. A 16 GB-class hypothesis additionally requires partial exposure inside active regions and qualified compatibility. | Exact package/part identity, density and compatibility documentation. |
| RX Vega 64 8 GB [S45–S49] | A two-stack high-density hypothesis retaining the sourced 2048 lanes cannot be explained just by stopping one whole stack. Ordinary lower-density parts remain a competing model. Do not transfer an unverified width to a different Vega variant. | Parts on the original RX package, not parts imported from a Frontier Edition comparison. |
| H100 SXM5 64 GB, CMP 100-200, PG199, A30X | Missing same-configuration active width prevents assigning a depth-exposure fraction. Borrowed family widths produce conditional examples, not results for these devices. | Width and part documentation tied to the exact SKU. H100 NVL HBM3 specifications cannot be transferred to the 64/94 GB HBM2e configurations. |

Repeated specifications are not additional units with identified population. Capacity, width and their calculated ratio are also not three independent pieces of evidence.

### Why these tiers, and how they can change

**Tier 1:** H100 64 GB has independently traceable official 64/94 GB same-HBM-generation configurations. CMP 100-200 has a low-capacity owner observation and related CMP capacity-control precedents. These are different leads; neither proves extra parts. We do not decide that one has a higher success probability than the other.

**Tier 2:** A30, PG199, MI50, A800 Active and H100 80 GB each support a concrete package-population or density question. Their ordinary explanations already fit their advertised configurations. The available evidence cannot reliably order them. MI50's normal 16/32 GB products are a useful comparison, not an anomaly by themselves. Later introduction of A800 does not prove surplus-part reuse.

**Tier 3:** RX Vega, CMP 100-210, BC-160 and A30X require additional unsupported transfer or compatibility assumptions, or their apparent positive clues have more direct ordinary explanations. Different soldered Vega packages, capacity-neutral CMP performance changes and unsourced A30X width reduce the case. Mining branding alone does not raise BC-160 to the leading tier.

These tiers are sensitive to what evidence one values. Requiring direct population evidence collapses **all 11 into unconfirmed**. Giving no weight to product-line analogies largely removes the tier-1 preference. A verified part map can reverse any tier; a bigger hypothetical number cannot. A documented low-density population contradicts the excess construction for the identified unit, while a stock nominal-capacity display alone does not.

## 3. Documented and externally reported references

| Reference | What is supported | What is still unknown |
| --- | --- | --- |
| **Intel GPU Max 1100, 48 GB** [S39] | Manufacturer documents four physically present HBM stacks, three enabled at 16 GB each, and one permanently disabled. This is the strongest physical-extra-stack reference in this comparison. | The fourth stack's separate density and health. A 64 GB total assumes it is also 16 GB. Permanent disable is negative evidence for recovery; its mechanism is not identified here. |
| **CMP 170HX** [S03,S16,S19,S20] | External owner/community reports describe capacity changes on identified variants. | No reproduction by this project; variants, test coverage, population prevalence and current inventory cannot be generalized. |
| **CMP 100-100** [S04a] | External first-person capacity reports for particular GP100 units. | Not evidence that CMP 100-200 shares the same assembly, limitation or outcome. |
| **AMD RX 480 4 GB** [S53–S55] | Historical first-person GDDR5 overpopulation/capacity-use report; contemporary sourcing explanation. | It is not HBM, not every lot, and not an audited causal procurement record. |

Intel is deliberately **outside the novel prediction tiers**. A physical fact should not be presented as an unconfirmed prediction, and a permanently disabled stack should not be marketed as the best recovery prospect. Its documented 0/FF sensor readings do not test DRAM health; its 64 GB BAR is an address aperture, not independent capacity evidence [S39].

## 4. Watchlist and ordinary comparisons

| Case | Current treatment | Evidence required to promote it |
| --- | --- | --- |
| **H20A 96 GB / H20 141 GB** [S64–S67,S77] | Supply watch. Product-specific inventory/material reuse is documented, but the material and destination are not. HBM3 versus HBM3e is an additional compatibility gap. The conditional 144 GB construction remains a historical scenario, not a current top-ranked forecast. | A part/package change tied to an actual 96 GB variant and its production stage. A post-April-2025 sale date is insufficient. |
| **AMD MI308 / MI308X** [S68–S70] | Supply watch. An inventory disruption is documented; MI308X operating reports already say 192 GB. No generic 96-to-192 GB claim. | Exact lower-capacity SKU, if one exists, with independently sourced baseline and population. |
| **B200 180/192 GB and B300 270/288 GB** [S64,S73,S74,S79,S81] | Specification/accounting watch. Current MIG documentation lists B200 180 GB and B300 288 GB; the marketing MIG table still labels 270 GB as preliminary. Exact SKU, revision, profile and capacity convention are unresolved. | Same physical SKU/board matched to both descriptions plus actual ordinary-data population. Neither ECC nor a reversible restriction is established as the explanation. |
| **GB300 Desktop / DGX Station 252 GB** [S74,S75,S79] | Topology watch. Seven 36 GB-class stacks could explain 252 GB; the server design has eight. The desktop's eighth memory stack has not been identified. | A real eighth stack and its part identity on the exact desktop package. Coherent CPU memory is separate. |
| **Intel Max 1350** [S56] | Historical product watch; announcement/withdrawal coverage does not establish a supply of production cards or physical HBM count. | Actual production-unit provenance and population information. |
| **Ascend 910B4** [S57] | Cross-vendor NPU watch based on a research synthesis, outside the GPU ranking. Proportional 32/64 GB and 800/1600 GB/s differences permit an ordinary active-interface explanation. | Primary SKU/topology documentation and a specific extra-population clue. |
| **H100 NVL 94 GB** [S72,S82] | Geometry reference. If 6016 lanes is actual active data width and each stack supplies at most 1024, at least six real stacks supply the width. If each full native interface is exactly 1024 lanes, a whole-stack-only on/off model is impossible. Density, a 96 GB physical total and healthy excess remain unestablished. | Part density, population and candidate-specific channel mapping. Standard channel width does not establish GPU disable controls. |
| **AMD MI300A/MI300X and Alveo U280/U50/U55C** [S58,S59,S76] | Ordinary density or allocation-policy comparisons. The default MI300A allocation limit does not create memory beyond the advertised total. | An anomaly on an identified physical lower-capacity product, not different SKU specifications. |

We remain vendor-neutral. Intel has a direct physical reference, AMD has useful density and historical manufacturing comparisons, and NVIDIA has more identified derivative leads in this evidence set. That distribution is not a conclusion that only NVIDIA could use the mechanism.

## 5. Define the scope before accepting a result

| Candidate | Current scope / missing cohort definition |
| --- | --- |
| H100 SXM5 64 GB HBM2e | Exact partner-cooled 64 GB board and package revision; production cohort not identified. Support listing does not establish shipment quantity. |
| CMP 100-200 | The reported ~6 GB variant, identified by exact board and device IDs; no favorable production lot established. |
| A30 | Authentic A30 package/board part-number groups; no dated substitution cohort established. |
| DRIVE A100 / PG199 | Original OEM modules separated from rebadged/reworked PCIe boards; cohort not identified. |
| Instinct MI50 16 GB | Original 16 GB OEM cohorts separated from repaired or aftermarket assemblies; no specific high-density cohort established. |
| A800 40 GB Active | Authentic single A800 Active boards; no candidate-specific shortage or substitution date identified. |
| H100 SXM5 80 GB | Exact 80 GB SXM package revision; do not extrapolate an early sample photograph to every shipped card. |
| RX Vega 56 / 64 8 GB | Original RX Vega packages identified by memory part and manufacturing stage; no favorable early/late lot identified. |
| CMP 100-210 | Separate the documented device-ID and board families; do not combine them as a single reproducible variant. |
| XFX BC-160 | Identified original BC-160 packages; marketing and resale labels alone do not establish a production cohort. |
| A30X | Exact converged module and package part; no favorable cohort identified. |

A first report can identify a unit without defining an entire cohort. Do not invent production dates from firmware dates, sales dates or similar serial formats. An ordinary unit narrows that unit's hypothesis; it does not disprove every other lot. Conversely, repeated escape to a new unnamed lot after each negative report is not a testable prediction. Preserve the old claim and name a new scoped hypothesis when new evidence warrants one.

## 6. Revision record

This table supersedes the three different ranking meanings in v0.4–v0.6. Those documents and CSVs remain historical snapshots, with a current-version notice. The new schema separates categories, tiers and evidence status.

- Intel moves from research-priority number 1 to a documented-disabled reference.
- H20 moves from historical-new-lead number 2 to supply watch until a physical transfer is identified.
- Blackwell label differences move to specification/accounting watch; a shared fractional difference is not evidence of a common recoverable block.
- The fragile A30/PG199 ordering is removed. MI50, A800 and H100 80 GB are kept in the same weak comparative tier.
- The fourth Intel stack is no longer described unconditionally as 16 GB in the historical table/CSV; the density remains conditional.
- No new owner result, recovery probability or price-based promotion is added.

[Contribute one source, observation or counterexample](call-for-participants.md). The [physical theory](theory.md) and [new deductions](inference-refinement.md) explain why these distinctions matter.

## ERROR CHECK

All novel scenarios are conditional; no actual favorable lot is claimed. Source repetitions are not independent experiments. Healthy, accessible and useful remain separate from populated. The main tiers expose comparative assumptions and ties instead of a calibrated probability. Prices have not changed the ranking.
