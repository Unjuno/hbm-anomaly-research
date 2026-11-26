# Current assessment — test ordinary explanations first

[日本語](current-ranking.ja.md) · [Home](../README.md) · [Inference and proof](diagnostic-inference.md) · [Parts](../data/hbm_part_constraints.csv) · [CSV](../data/current_ranking.csv) · [Sources](sources.md)

**v0.10.0 — 2026-11-26. Documentary research; no original hardware measurements.**

## 1. Withdraw the previous ordering

v0.9 primarily ranked similarity to earlier product purposes and families. v0.9.1 added performance comparisons but retained that ordering. The ranking did not establish whether the target observations could be explained by ordinary parts.

**Withdraw tiers 1–3 for all 11 novel hypotheses.** `rank_tier` is blank; `v09_recurrence_tier` retains the old value. This is not a demand for hardware proof before making forecasts. It corrects an ordering that substituted resemblance for evidence distinguishing ordinary and excess-memory configurations.

The target claim is physical ordinary-data HBM beyond the advertised capacity. Healthy extra memory, software access, reversible restrictions and manufacturer intent are separate claims.

## 2. Reassessment of all 11 candidates

An ordinary fit means that a model is consistent with documented part capacity and performance. It does not identify the actual target bill of materials. Missing population information does not become positive evidence.

| Candidate | Assessment | Ordinary countermodel | Target evidence that would change it |
| --- | --- | --- | --- |
| **CMP 100-200, ~6 GB** | **Inputs missing; former first place withdrawn** | SK hynix listed 2 GB, 1024-lane, 2.0 Gb/s HBM2 in 2016. Three parts provide 6 GB-class capacity. 3072 lanes and 768 GB/s are predictions of that countermodel, not observed target specifications [S05,S93] | Width together with real DRAM throughput, or part density and speed grade, tied to the same unit. A width of 3072 alone does not eliminate ordinary 2 GB parts |
| **A30X, 24 GB** | **Ordinary capacity/rate fit** | Three Micron-described 8 GB, 1024-lane, 3.2 Gb/s-class parts provide 24 GB and up to 1228.8 GB/s, encompassing the specified 1223 GB/s. The A100X ratio does not require denser parts [S01,S10] | Target evidence of denser parts, or a concrete constraint excluding this ordinary part class from the target |
| **MI50 16 GB** | **Ordinary capacity/rate fit** | Four 4 GB, 256 GB/s-class HBM2 parts announced in production in 2016 provide 16 GB and 1024 GB/s, consistent with the advertised approximately 1 TB/s. A 32 GB sibling at the same bandwidth is not excess-memory evidence [S38,S80,S90] | Denser parts on a traceable unit actually operating as stock 16 GB. Stale FRU names and a 16 GB CPU-visible BAR do not meet this condition [S43,S44] |
| **RX Vega 56/64, 8 GB** | **Ordinary model and package counterevidence** | Vega 64's specified 8 GB/484 GB/s fits two 4 GB-class parts. A firsthand teardown describes common PCBs but different installed packages for RX and Frontier Edition. Do not copy the 64's numbers into a 56 measurement [S45,S46,S90] | Denser parts identified on an original RX assembly |
| **BC-160, reported 8 GB** | **Ordinary model; weak target provenance** | Reported 8 GB/2048 lanes fits two 4 GB-class parts. Official V520 8 GB/512 GB/s is an ordinary comparator, not a BC-160 measurement [S50,S51,S90] | BC-160-specific primary specifications, measurements or part records. Claimed support for 16 GB does not establish population |
| **A30, 24 GB** | **Ordinary capacity/width geometry** | Three 8 GB-class equivalents explain 24 GB/3072 lanes. Compute recovery does not require extra HBM; additional inactive positions are a separate hypothesis [S06,S34] | Target evidence of extra real HBM or denser parts behind the enabled interfaces |
| **A800 40 GB Active** | **Ordinary capacity/width geometry** | Five 8 GB-class equivalents explain 40 GB/5120 lanes. Later introduction and an 80 GB relative are not records of part reuse [S71,S35] | Target package-density/population changes or specific allocation records |
| **CMP 100-210, 16 GB class** | **Ordinary shipped-capacity model** | A normal V100-derived 16 GB assembly suffices. Compute, link and performance improvements do not require extra capacity [S08,S14,S33] | Part/population evidence supporting a larger physical capacity on the same 16 GB unit |
| **PG199 / DRIVE A100, reported 32 GB class** | **Inputs missing** | Four 8 GB-class parts provide a capacity model; target width and density remain unresolved. OEM use does not select a denser assembly [S12,S35] | Original OEM module-to-part mapping, width/bandwidth and provenance preceding repair or rework |
| **H100 SXM5 64 GB HBM2e** | **Inputs missing** | Four 16 GB-class parts fit capacity. Lists of supported 64/94 GB boards do not establish one assembly restricted into two SKUs [S60,S61,S64] | Width, bandwidth and parts for the physical 64 GB variant; separate virtual allocation and the 94 GB product |
| **H100 SXM5 80 GB** | **Sixth-site identity unresolved** | The vendor describes five active HBM3 stacks; a structural-support explanation exists for the sixth site. Full GH100's six interfaces do not identify extra DRAM [S62,S63] | Identify DRAM versus support material at that site. Health remains a separate question |

Half the capacity at the same width can be ordinary low-density memory. “If it uses denser parts, there is hidden capacity” assumes the desired result unless the denser parts are required by an observation or an independently supported constraint. See the [inference document](diagnostic-inference.md).

## 3. The target-specific constraint retained for 170HX

The 2023 firsthand review [S87] describes an 8 GiB-class product, a 7961 MB device report, 4096 lanes, a calculated peak of 1492.99 GB/s and clpeak results of 1165.79–1355.40 GB/s. Reported GPU clock: 1410 MHz; reported memory clock: 729 MHz; CUDA version: 12.20. The range is across vector widths, not a repeated-measurement uncertainty interval. Workload size, loaded clocks, temperatures and other missing conditions remain explicit in the [performance record](performance-gap.md).

| Countermodel | Nominal capacity class, lanes and calculated bandwidth | Relation to the review |
| --- | --- | --- |
| Four published 2 GB, 2.0 Gb/s parts [S93] | 8 GB class; 4096 lanes; at most 1024 GB/s | Capacity and width fit; reported throughput does not |
| Sensitivity case allowing the research-reported 2.4 Gb/s rate on 2 GB parts [S36] | 8 GB class; 4096 lanes; at most 1228.8 GB/s | Explains part of the measured range. The largest 1355.40 GB/s result is still higher, subject to traffic-accounting verification |
| Four fast 8 GB-class parts [S01] | 32 GB class; 4096 lanes; up to 1638.4 GB/s | Throughput fits. Partial exposure is an additional mechanism that can explain an 8 GB-class display |
| Four fast 16 GB-class parts [S01] | 64 GB class; 4096 lanes; up to 1638.4 GB/s | Also fits. Bandwidth does not choose between 32 and 64 GB |

These are conditional models, not identified populations. Unpublished fast low-density parts, operation above published ratings, reported-width errors and cached or otherwise inflated traffic accounting remain alternatives. The public catalog is not assumed complete. The research-speed sensitivity case deliberately exposes dependence on the selected part set.

FMA throttling and non-FMA improvement concern compute restrictions. Such restrictions can coexist with ordinary low-density HBM, so they are not an independent bonus for hidden memory. Later capacity-change reports are not inputs to this inference from 2023 evidence.

## 4. Documentary investigation order

1. **Match records for the same CMP 100-200 unit.** Tie its approximately 6 GB display to width, bandwidth and part speed grade. Width alone still leaves the 2 GB countermodel.
2. **Match existing target units to part records.** For MI50 or A30X, a density/speed/part identity can change the assessment; another ratio comparison of already ordinary specifications cannot.
3. **Investigate topology and manufacturing branches with evidence specific to those branches.** This includes H100's sixth site, actual GA100 derivative populations, original OEM modules and applicable part-change records.

This order concerns progress from a small amount of documentation, not hidden-capacity probability. Preserve missing data when a record cannot be found. Hardware purchase or ownership is not a prerequisite for updating a forecast.

## 5. How history, cohorts and prices enter

History connects a proposed causal mechanism to a target. Recurrence is possible, but the same vendor, generation or use case does not identify which part configuration was used.

| Historical observation | Required connection | Without that connection |
| --- | --- | --- |
| Shortage of low-density parts | Qualified substitute, availability window and manufacturing stage at which capacity decisions remained possible | Record background; do not increase an excess-memory ranking |
| Surplus completed packages | Target-compatible part/population identity and timing before/after reassignment | A common die or similar PCB does not establish reuse |
| Differences between production groups | Original part/revision/stage-defined cohorts and predicted differences | Do not invent favorable lots from sale dates or sellers |
| Price changes | Comparable configuration/condition time series and competing supply, demand and publicity explanations | Current transaction evidence is insufficient; no price adjustment |

Even an economic incentive for denser parts needs a link to available inventory, qualification and process timing. Memory-defect harvesting could predict physical surplus while weakening healthy-extra-capacity expectations. See [manufacturing causes](manufacturing-causality.md) and [historical hypotheses](recurrence-hypotheses.md).

## 6. References and watches remain

| Category | Scope |
| --- | --- |
| Vendor-documented physical reference | Intel Max 1100: four physical stacks, three enabled 16 GB stacks, one permanently disabled. Fourth-stack density, health and recovery are separate. A 64 GB BAR is not physical capacity [S39] |
| External capacity reports | CMP 170HX and CMP 100-100, limited to reported units/conditions; not independently reproduced here [S19,S04a] |
| Non-HBM precedents | RX 480 4 GB and P104-100: specific reports do not transfer density, cause or prevalence to HBM targets [S54,S84] |
| Supply/specification/topology watches | H20, MI308, B200/B300, GB300 Desktop, Max 1350 and Ascend 910B4. Supply events and inconsistent labels alone do not predict usable surplus |
| Geometry and ordinary comparators | H100 NVL, MI300 and Alveo. Stack-count lower bounds, density differences and allocation policies are distinct from recoverable capacity |

The CSV retains 26 entries, including 11 unranked hypotheses. Evidence for an established reference is not transferred into success probabilities for the new candidates.

**ERROR CHECK:** Old tiers withdrawn; the 2 GB primary counterexample included. Part existence and target adoption remain separate. Specifications, measurements, assumptions and later outcomes are distinguished. No new hardware results, favorable lot, prevalence or success probability is invented.
