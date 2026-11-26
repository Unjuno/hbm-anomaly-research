# Current ranking of HBM hypotheses

[日本語](current-ranking.ja.md) · [Home](../README.md) · [Recurrence forecasts](recurrence-hypotheses.md) · [Capacity constraints](capacity-constraints.md) · [Manufacturing causes](manufacturing-causality.md) · [Sources](sources.md) · [CSV](../data/current_ranking.csv)

**v0.9.1 — 2026-11-26. Desk research; no original hardware measurements.**

**Complementary v0.9.1 screen:** [performance gaps](performance-gap.md) restores the historical 2023 170HX bandwidth/compute observations and compares existing candidates. The recurrence tiers below are unchanged; performance anomalies and historical recurrence are separate evaluation axes, not a numerical probability.

## 1. What the forecast ranks

This research predicts recurrence of capacity restrictions, shared assemblies and manufacturing substitutions across generations and production cohorts. The target is ordinary-data HBM beyond a named advertised baseline; units sharing a product name are not assumed to share one bill of materials.

**Ranks 1–3 compare the closeness of the historical-mechanism link behind each recurrence forecast.** Product purpose, part/package lineage, period context and ordinary-model feasibility are considered together. Candidates within a tier are tied. A forecast can be published and revised without hardware ownership; documentary history and mechanism evidence can change its ordering. These are not numerical success rates or prevalence estimates.

**Explicit v0.9 lens change:** recurrence across product lineages and cohorts becomes the main criterion, replacing v0.8's physical-hypothesis specificity ordering. Old values remain in CSV `v08_specificity_tier`. This judgment change is distinct from a new hardware finding. See [recurrence hypotheses](recurrence-hypotheses.md) and the [precedent date ledger](../data/capacity_precedents.csv).

| Question | Current treatment |
| --- | --- |
| Forecast order | Compare historical mechanism links and candidate-specific cohort predictions |
| Population, health and access for 11 novel predictions | All remain unestablished; these statuses are separate from forecast ranks |
| Favorable actual lot or market prevalence | Not identified; cohort selectors below are predicted targets, not discovered favorable lots |
| Price-based rank change | None; comparable validated transaction series remain missing |

Ordinary explanations also have evidence levels: **identified target parts, documented family configuration, catalog geometry, arithmetic-only construction, or unresolved inputs**. A hypothetical low-density part that fits the numbers is not equivalent to an identified compatible assembly. Conversely, an incomplete search does not establish that an ordinary part does not exist. CSV `ordinary_model_evidence` retains the candidate-specific distinction.

GB-class constructions are conditional totals, not observations or expected values. Sources support inputs or external reports, not manufacturer endorsement of our forecasts.

## 2. Unified prediction table

| Rank tier | Candidate and baseline | Why the hypothesis is concrete | Conditional construction | Strongest ordinary explanation | One fact that would change the assessment |
| ---: | --- | --- | --- | --- | --- |
| 1 | **CMP 100-200** — ~6 GB class | A low-capacity Volta mining configuration plus external CMP capacity-restriction precedents motivates a capacity-specific analogy. [S02,S04a,S05,S32,S36] | 12 GB class if a larger compatible assembly was actually populated and partly exposed. | Actual width and density are unknown. Low-density HBM or partial channels can explain the report; 12 GB TITAN V is not proof of a shared package. | Memory part/density and population evidence tied to the same identified ~6 GB board; another copy of the stock log adds no independent observation. |
| 2 | **H100 SXM5 64 GB HBM2e** — 64 GB | Official 64 and 94 GB HBM2e partner-cooled board configurations make a specific same-family comparison possible. [S60,S61,S62,S64] | 80/96 GB class only if five/six real 16 GB-class stacks are present; neither population is established. | Four 16 GB-class stacks can explain 64 GB normally; extra sites could be absent, dummy or defective. | A vendor/OEM package population map or existing owner evidence distinguishing four real stacks from five/six; not a virtual 64 GB allocation. |
| 2 | **A30** — 24 GB | A reduced GA100 derivative permits a completed-package reuse or disabled-region hypothesis. [S06,S34,S35] | 32/40 GB class if one/two additional 8 GB-class regions are populated. | Three active 8 GB-class stacks explain the official 24 GB / 3072-lane configuration. Compute-block recovery did not establish extra HBM. | Reliable actual memory population beyond the ordinary three-stack model, with dummy parts and repair history resolved. |
| 2 | **DRIVE A100 / PG199** — 32 GB class reported | OEM-specific GA100 packaging leaves a concrete density/reassignment question, but no extra part has been identified. [S12,S35] | 64 GB class only if four 16 GB-class stacks are actually present. | For example, four 8 GB-class stacks already explain 32 GB; actual count and density remain unresolved. | An original OEM package/part mapping showing density on the reported 32 GB configuration. |
| 2 | **Instinct MI50 16 GB** — 16 GB | Both 16 and 32 GB same-family configurations are documented; this bounds a plausible density-substitution question. [S38,S42,S43,S44,S80] | 32 GB class if four 8 GB-class stacks were used while only 16 GB remained exposed. | Four 4 GB-class stacks suffice. Both official capacities share width and bandwidth, which is normal; a stale FRU label is not a capacity restriction. | HBM part identification on a traceable stock 16 GB unit, not a 16 GB name attached to a card already exposing 32 GB. |
| 2 | **A800 40 GB Active** — 40 GB | A late GA100 derivative after higher-capacity family members permits a reuse hypothesis; chronology alone does not establish reuse. [S25,S35,S60,S71] | 48 GB class if a sixth 8 GB-class region exists; 80 GB class requires five compatible 16 GB-class stacks and partial exposure. | Five 8 GB-class stacks fit the official 40 GB / 5120-lane specification. Higher-density HBM2e compatibility is unverified. | Package-part compatibility and population for the actual board; an 80 GB two-board NVLink total does not qualify. |
| 2 | **CMP 100-210** — 16 GB class | Distinct board families permit cohort hypotheses, while reported gains so far concern performance rather than additional capacity. [S04,S08,S14,S33] | 32 GB class only for an independently identified higher-density assembly. | An ordinary V100-derived 16 GB assembly explains the known configuration. | Actual high-density memory parts on an identified 16 GB variant, rather than extra compute units or link speed. |
| 3 | **H100 SXM5 80 GB** — 80 GB | A six-interface full design and an external package-site report leave a question about the sixth site. [S62,S63,S64] | 96 GB class only if six real 16 GB-class HBM stacks are present. | Five active 16 GB-class stacks explain 80 GB. A sixth visible package/site need not be DRAM or healthy. | Identification of the sixth site as a real memory stack versus a spacer/dummy, then its density; health remains separate. |
| 3 | **RX Vega 56 / 64 8 GB** — 8 GB | Related 16 GB Frontier Edition and 2017 supply context motivate a qualified-package substitution question. [S45,S46,S47,S48,S49] | 16 GB class if two 8 GB-class stacks were populated with partial exposure. | Two 4 GB-class stacks explain 8 GB; board analysis reports different soldered packages despite shared PCB. High-density parts were also seeing rising demand; their surplus availability for substitution is not established. | A factory-origin RX package with higher-density memory identification; PCB similarity alone is insufficient. |
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

**Tier 1 — CMP 100-200:** capacity-control reports exist on the Pascal and Ampere sides of the same mining-oriented CMP line. Recurrence of a similar product decision in the low-capacity Volta variant is the closest analogy [S02,S04a,S19]. This is a historical/product-purpose forecast. The target width remains unresolved, so it is not called a measured bandwidth anomaly.

**Tier 2 — A30, PG199, A800 Active, CMP 100-210, MI50, H100 64 GB:** shared GA100 lineage, shared CMP purpose, or documented same-family capacity variants give concrete bridges to package/cohort predictions. CMP 100-210 moves 3→2 because the board-family split and the normal V100 16/32 GB comparison provide a cohort/density axis [S08,S14,S33]; known performance gains have not become capacity results. H100 64 GB's official 64/94 GB comparison remains useful but is a less direct recurrence bridge than the same-purpose CMP precedent, moving it to tier 2.

**Tier 3 — H100 80 GB, RX Vega, BC-160, A30X:** the H100 80 GB sixth-site question concerns population/grading rather than a demonstrated recurring depth cap, with a five-active-stack construction and structural-support alternative [S62,S63]. Distinct RX/Frontier packages, missing qualified high-density BC-160 packages and missing A30X width make transfer of precedent more indirect. The hypotheses remain; new production-path evidence can change the forecast.

**Documentary evidence alone can revise a forecast.** Compatibility, period availability, common parts, grading or reassignment evidence can strengthen or weaken the recurrence link. Physical-confirmation fields change only when their own claims gain support. Neither an unconfirmed status nor a larger hypothetical capacity determines the forecast tier by itself.

## 3. Documented and externally reported references

| Reference | What is supported | What is still unknown |
| --- | --- | --- |
| **Intel GPU Max 1100, 48 GB** [S39] | Manufacturer documents four physically present HBM stacks, three enabled at 16 GB each, and one permanently disabled. This is the strongest physical-extra-stack reference in this comparison. | The fourth stack's separate density and health. A 64 GB total assumes it is also 16 GB. Permanent disable is negative evidence for recovery; its mechanism is not identified here. |
| **CMP 170HX** [S03,S16,S19,S20] | External owner/community reports describe capacity changes on identified variants. | No reproduction by this project; variants, test coverage, population prevalence and current inventory cannot be generalized. |
| **CMP 100-100** [S04a] | External first-person capacity reports for particular GP100 units. | Not evidence that CMP 100-200 shares the same assembly, limitation or outcome. |
| **P104-100, GDDR5X** [S17,S84,S85] | A 2018 ASUS owner post claims 8 GB installed with half disabled; separate 2019 owner discussions include capacity changes and problems. | Not ASUS endorsement, a result for every unit, or an internal causal record. The GIGABYTE 4 GB baseline does not identify the ASUS unit's parts. |
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

## 5. Cohort-specific predictions

These are **forecasts of where differences would cluster if the precedent recurs**. Part and revision identifiers are selection criteria, not already discovered favorable lots.

| Candidate | Cohort selector | Predicted pattern if recurrence occurs |
| --- | --- | --- |
| CMP 100-200 | Original ~6 GB units separated by device ID, board PN and package family | A subgroup retains greater part capacity or a distinct capacity setting |
| A30 | Package PN and HBM-part changes within the 24 GB SKU | Some groups retain extra inactive regions or denser parts while keeping 24 GB advertised |
| PG199 | Original OEM platform, module PN and revision; separate later conversions | A specific 32 GB group uses denser parts, with original lineage traceable despite later resale |
| A800 40 GB Active | Genuine single Active boards grouped by package lineage | A subgroup maps to a greater-capacity GA100 package family |
| CMP 100-210 | Keep reported device-ID and PG500 board families separate | One group pairs denser population with 16 GB exposure; compute/link-only changes remain separate observations |
| MI50 16 GB | Original 16 GB OEM package, part and revision groups | A group retains 16 GB / 4096 lanes while using parts associated with a 32 GB-class construction |
| H100 64 GB HBM2e | Exact partner-cooled 64 GB PN/package groups | Part commonality with greater capacity, or capacity-setting/grading differences, clusters in a group |
| H100 80 GB | 80 GB SXM package revisions and sixth-site material | A group has real density-identifiable HBM at the sixth position |
| RX Vega 8 GB | Original RX 56/64 package and HBM-part groups | A specific 8 GB group contains denser parts; shared PCB alone does not define it |
| BC-160 | Original XFX/Navi 12 board/package groups | A qualified denser production package is identified and some units retain 8 GB exposure |
| A30X | Exact converged-module PN/package groups | A group uses denser parts while maintaining the 24 GB baseline |

A durable product-segmentation cap predicts a different time pattern from a temporary substitution. Do not assume early or late units are universally favorable. Match the prediction to the relevant population, configuration or sale date as explained in [recurrence hypotheses](recurrence-hypotheses.md).

Identified ordinary parts weaken the excess forecast for that defined group. Do not move repeatedly to an unnamed new lot after every negative report. Preserve the original forecast and the documentary reason for any later scope revision.

## 6. v0.9 revision record

| Candidate | v0.8 | v0.9 | Reason |
| --- | ---: | ---: | --- |
| CMP 100-200 | 1, tied | 1, sole | Same-purpose CMP capacity-control precedents across generations receive the closest recurrence link |
| H100 64 GB | 1 | 2 | Same-family capacity variants are a more indirect bridge than repeated same-purpose capacity restriction |
| CMP 100-210 | 3 | 2 | Shared CMP purpose, distinct board families and the normal V100 16/32 GB comparison define a cohort/density axis |
| H100 80 GB | 2 | 3 | Separate sixth-site population/grading from recurring depth restriction; retain the ordinary five-stack and structural-support alternatives |

Other tiers are retained. Prior meanings and values remain in the CSV; this explicit criterion change is distinguished from new observations. P104 is added as a historical GDDR5X reference, giving 11 predictions and 26 total entries. The [precedent ledger](../data/capacity_precedents.csv) separates architecture, manufacture and report dates. No new hardware measurement or price-based rank change is claimed.

[Sources and counterexamples are welcome](call-for-participants.md). Hardware ownership is optional: compatible ordinary parts and manufacturing history can change a forecast.

## ERROR CHECK

All novel scenarios are conditional; no actual favorable lot is claimed. Source repetitions are not independent experiments. Healthy, accessible and useful remain separate from populated. The main tiers expose comparative assumptions and ties instead of a calibrated probability. Prices have not changed the ranking.
