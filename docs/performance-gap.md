# Performance mismatch screening: the historical 170HX reference

[日本語](performance-gap.ja.md) · [Current ranking](current-ranking.md) · [Recurrence hypotheses](recurrence-hypotheses.md) · [Capacity constraints](capacity-constraints.md) · [Data](../data/performance_gap_observations.csv)

**v0.9.1, 2026-11-26. Documentary forecasts; no original measurements.** Restore the original discovery axis: discrepancies between advertised capacity, memory performance and the capabilities of the underlying parts. Historical recurrence and lot-specific incentives are complementary, not replacements.

## 1. A pre-recovery historical observation

The first-person CMP 170HX review dated October 25, 2023 and archived October 29, 2023 [S87] reports the following on an 8 GB-class card, before the later capacity-recovery reports used in this project:

| Quantity | Reported observation | Evidence type |
| --- | --- | --- |
| CUDA total global memory | 7961 MB (source notation) | Device report |
| Memory bus | 4096 bit | Device report |
| Peak bandwidth | 1492.99 GB/s | Tool-derived theoretical property |
| clpeak global memory | 1165.79–1355.40 GB/s | Measured across float to float16 vector widths |
| clpeak standard FP32 FMA | 394.77 GFLOPS | Measured |
| Modified clpeak FP32 without FMA | 6252.80–6294.30 GFLOPS | Measured with different instruction mix |

Hardware: CMP 170HX 8 GB class; source reports CUDA driver version 12.20, GPU clock 1410 MHz and memory clock 729 MHz in device query (not effective lane rate). Per-run load clocks, working-set size/batch, temperature and replicate variance are not established by the cited tables. Ranges are across vector widths, not confidence intervals. FMA and non-FMA use different instruction mixes; the ratio is not a general efficiency metric.

High memory throughput was a real observation, while selective compute restrictions were a concrete lead. This supports investigating deliberate resource configuration beyond simple low-end hardware design, not the inference that compute throttling proves extra memory. The mining product's preference for bandwidth over large capacity or general compute supplies a possible explanation. A 2021 report also paired 8 GB with 4096-bit width [S88]. We do not identify the first discovery date or attribute the original discoverer's reasoning.

## 2. Like-for-like published peaks and nominal capacity classes

| Product | Nominal GB class | Peak GB/s | Peak per nominal GB label | Basis |
| --- | ---: | ---: | ---: | --- |
| CMP 170HX 8 GB | 8 | 1492.99 | 186.62 | 2023 tool-derived peak [S87] |
| A100 40 GB | 40 | 1555 | 38.88 | Vendor [S09] |
| A100 80 GB SXM | 80 | 2039 | 25.49 | Vendor [S09] |
| A30 | 24 | 933 | 38.88 | Vendor [S06] |
| A30X | 24 | 1223 | 50.96 | Vendor [S10] |
| A100X | 80 | 2039 | 25.49 | Vendor [S10] |
| MI50 16 GB | 16 | 1000 | 62.50 | Vendor [S38] |
| MI50 32 GB | 32 | 1000 | 31.25 | Vendor [S80] |

The 8 GB 170HX has 20% of the nominal capacity and about 96% of the A100 40 GB theoretical bandwidth. Its nominal bandwidth-per-capacity ratio is 4.80 times that comparator. These are label ratios, not exact-byte calculations, estimated recovery multipliers or statistical significance.

| Symbol | Definition / meaning | Unit | Domain / assumptions | Type |
| --- | --- | --- | --- | --- |
| $B$ | Theoretical ordinary-data peak bandwidth | byte/s | Positive; matched convention | Scalar |
| $C$ | Advertised ordinary-data capacity | byte | Positive; resolved byte convention | Scalar |
| $B_*$ | Reference product peak bandwidth | byte/s | Positive | Scalar |
| $C_*$ | Reference product advertised capacity | byte | Positive | Scalar |
| $w$ | Active ordinary-data lane count | 1 | Positive integer, exact SKU | Scalar |
| $w_*$ | Comparator active lane count | 1 | Positive integer | Scalar |
| $G_B$ | Relative bandwidth-to-capacity mismatch | 1 | Positive, formula below | Scalar |
| $G_w$ | Relative width-to-capacity mismatch | 1 | Positive, formula below | Scalar |

$$G_B=\frac{B/B_*}{C/C_*},\qquad G_w=\frac{w/w_*}{C/C_*}.$$

Each ratio divides like units and is dimensionless. $G_B$ includes signaling-rate differences; $G_w$ removes them but does not identify physical density. Using the documented nominal 4096/5120 lane counts and 8/40 GB labels [S19,S35,S87] yields width retention 80% and capacity retention 20%, hence $G_w=4$. This is the same information as 2 vs 8 GB per 1024-lane equivalent, not independent evidence. For exact-byte models and bounds see [capacity constraints](capacity-constraints.md).

## 3. Apply the two lenses to current candidates

| Lead | Performance-side assessment | Historical/manufacturing search |
| --- | --- | --- |
| CMP 100-200 | ~6 GB report is a capacity clue; reliable same-unit width, bandwidth and benchmark remain missing. A hypothetical 3072-bit interface gives 2 GB per width equivalent, but that is not a measured target width. | Same-purpose CMP recurrence; seek original review/log/part provenance. |
| A30X | 30% of A100X capacity and about 60% of its peak bandwidth; nominal mismatch about 2x. Same nominal capacity as A30 with ~31% higher bandwidth. Ordinary fast 8 GB-class HBM2e is an alternative; width unknown. | Qualified module parts and availability of lower- and higher-density variants. |
| MI50 16 GB | Same documented width, bandwidth and compute peaks as 32 GB; a nominal 2x contrast. Normal density choices suffice. | Compare original same-family part inventories and cohorts. |
| A30 / A800 40 GB Active | Near-normal bandwidth/capacity against A100 40 GB; no large 170HX-style signal. | Reused packages, inactive regions or a retained product specification remain separate leads. |
| H100 64 GB / PG199 / CMP 100-210 | Resolve same-variant width/bandwidth and benchmark semantics; compute recovery alone is not a capacity observation. | Package lineage, original revisions, higher-capacity comparators. |

A mismatch is a deviation from a declared comparator, not an established statistical outlier. The known 170HX positive reference is retrospective, not independent validation of the detector. Missing measurements remain missing rather than disqualifying a candidate.

## 4. Keep the two evidence axes

The performance/part axis uses capacity, width, effective rate, theoretical versus measured memory throughput, and instruction-class performance. The history/cohort axis uses precedent, purpose, part lineage, contemporary supply and the production/configuration decision. Prioritize their intersection, without assuming probabilistic independence or adding arbitrary scores. The v0.9 recurrence tiers remain visible; this is a complementary screen, not a new ordering of healthy/recoverable capacity.

A later same-card external comparison reports 1592 to 1599 GB/s at a 256 MB working set while compute performance changes substantially [S89]. This is consistent with selective restriction, but is not a capacity-only intervention or validation of all addresses. Do not import later outcomes into the historical forecast inputs.

**ERROR CHECK:** Measured throughput, computed peaks and subsequent outcomes are labeled separately. Comparison dependence and missing test conditions are recorded. No new physical population, measurement, favorable lot, success probability, transaction series or X post.
