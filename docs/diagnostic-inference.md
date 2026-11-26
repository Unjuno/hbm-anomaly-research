# Test ordinary configurations instead of ranking resemblance

[日本語](diagnostic-inference.ja.md) · [Current classifications](current-ranking.md) · [Capacity constraints](capacity-constraints.md) · [Performance records](performance-gap.md) · [Sources](sources.md)

**v0.10.0 — November 26, 2026 JST. Conditional inference from public sources; no project hardware measurements.**

## 1. Retracted ordering and continuing objective

The v0.9 tiers 1–3 treated proximity to a product family, use case or precedent as the strength of evidence for candidate-specific surplus HBM. We retract that ordering. The v0.9.1 bandwidth/capacity ratio against a selected GPU also does not, by itself, exclude an ordinary configuration. **Continue making predictions, but identify the observation that each prediction explains better than an ordinary construction.**

| Category | Treatment here |
| --- | --- |
| Fact | Manufacturer component and GPU specifications; attributable owner measurements with their conditions retained |
| Inference | Whether the stated component set and observations can coexist; conclusions remain conditional on those premises |
| Hypothesis | Additional physical capacity, partial exposure, populated inactive regions, or substitution in an identified manufacturing cohort |
| Uncertainty | Unlisted components, target qualification, measurement conditions, capacity conventions, dates, population and health |

A shared die, use case or larger sibling can select a research lead. Substituting that sibling's density into the candidate and concluding that capacity must be hidden simply assumes the disputed premise. Compute throttling and additional HBM are also different propositions.

## 2. Find parts that satisfy capacity and speed together

Compare bandwidth/capacity with **ordinary configurations that contemporary components could support**, rather than an arbitrary comparison GPU. Couple capacity, speed and width from the same part evidence. Values below are nominal classes, not evidence of adoption or qualification in a target GPU.

| Public component example | Capacity per stack | Data width per stack | Published speed | Arithmetic peak per stack | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| SK hynix HBM2, 2016 product table | 2 GB | 1024 lanes | Up to 2 Gb/s | 256 GB/s | S93, p.12 |
| Samsung HBM2, 2016 production announcement | 4 GB | 1024-lane equivalent | Corresponding to the published 256 GB/s | 256 GB/s | S90 |
| Samsung Aquabolt, 2018 production announcement | 8 GB | 1024 lanes | 2.4 Gb/s | 307.2 GB/s | S91 |
| Samsung Flashbolt, 2020 announcement | 16 GB | 1024 lanes | 3.2 Gb/s | 409.6 GB/s | S92 |
| Micron HBM2E, 2021 technical brief | 8 / 16 GB | 1024 lanes | Up to 3.2 Gb/s | 409.6 GB/s | S01 |

S92 also reports testing at 4.2 Gb/s. That does not guarantee every production operating condition, but even allowing it leaves the 16 GB part below the 2 GB part's bandwidth/capacity ratio. This table does not exhaust all manufacturers, OEM parts or speed grades.

**New contrary evidence:** S93's “HBM Product Available” table lists the combination 2Hi, 2 GB, 1024DQ and 1 / 1.6 / 2 Gb/s. Therefore a calculation that restricts parts to 4 / 8 GB and declares 6 GB impossible is unsuitable. Three 2 GB-class stacks normally explain CMP 100-200's approximately 6 GB-class capacity alone. The table does not prove their use or clock in CMP, but it prevents treating low-density parts as merely imaginary.

## 3. A conditional capacity lower bound from bandwidth

### Assumptions and variable table

Use one identified GPU configuration. Ordinary-data capacity excludes dedicated ECC and repair-spare cells. Distinguish actual DRAM traffic from cache reuse, compression and host/peer transfers. Do not substitute a calculated peak for a measurement.

| Symbol | Meaning | Unit | Definition | Domain and assumptions | Type |
| --- | --- | --- | --- | --- | --- |
| $\mathcal P$ | Evaluated part and speed-condition set | None | Attributable conditions coupling date, capacity and speed | Nonempty; coverage of every actual part is a separate premise | Set |
| $j$ | Part-condition index | 1 | Identifies a condition in $\mathcal P$ | Within the set | Integer |
| $n$ | Real stack count | 1 | Populated memory stacks, excluding dummies | Positive integer; need not be known for the derivation | Scalar |
| $i$ | Populated-stack index | 1 | Identifies one actual stack | 1 through $n$ | Integer |
| $c_j,c_i$ | Physical ordinary-data capacity | byte | Capacity of a catalog condition or populated stack | Positive; normalized capacity convention | Scalar |
| $b_j,b_i$ | Ordinary-data bandwidth upper bound | byte/s | Bound coupled to that part's capacity and speed conditions | Nonnegative; revise if operation exceeds the stated conditions | Scalar |
| $\rho_{\max}$ | Maximum part-set bandwidth/capacity | s$^{-1}$ | $\max_{j\in\mathcal P}b_j/c_j$ | Positive and finite | Scalar |
| $B$ | Actual DRAM data bandwidth | byte/s | Traffic actually supplied by DRAM in the observation | Nonnegative; distinct from apparent application throughput | Scalar |
| $B_L$ | Conservative bandwidth lower bound | byte/s | A lower bound on $B$ supported by conditions and errors | Nonnegative; the minimum across vector widths is not automatically such a bound | Scalar |
| $C_p$ | Physical ordinary-data capacity | byte | Sum of populated $c_i$ | Positive; says nothing about health or exposure | Scalar |
| $C_U$ | Upper bound on the comparison capacity | byte | Conservative upper bound on the resolved nominal-capacity baseline | Positive; correct reservations/deductions if comparing a reported total instead | Scalar |
| $g$ | Example capacity unit | byte | Exactly $2^{30}$ byte | Illustrative constant, not resolution of vendor GB notation | Scalar |

If every populated part follows a condition in the set, the definition of its maximum gives, for every part,

$$b_i\le\rho_{\max}c_i.$$

The bandwidth actually supplied cannot exceed the sum of the parts' bandwidth upper bounds. Summing the individual inequalities gives

$$B\le\sum_{i=1}^{n}b_i\le\rho_{\max}\sum_{i=1}^{n}c_i=\rho_{\max}C_p.$$

Divide by positive $\rho_{\max}$ and use a justified lower bound $B_L$:

$$\boxed{C_p\ge B/\rho_{\max}\ge B_L/\rho_{\max}}.$$

Consequently, $B_L>\rho_{\max}C_U$ excludes a physical construction within the comparison capacity **inside that component set**. Failure to satisfy this inequality does not exclude additional inactive regions or partial exposure of denser parts.

**Unit check:** $b_i/c_i$ has units s$^{-1}$; $B/\rho_{\max}$ has units byte. Do not silently convert GB labels to GiB. Integer population, package positions and active width can tighten the model, but a sibling product does not supply a missing width.

### Conditional example using 170HX

S87 reports an 8 GB-class 170HX with 4096-bit width, a calculated 1492.99 GB/s peak, and vector-width-dependent clpeak results of 1165.79–1355.40 GB/s. GPU clock 1410 MHz, memory clock 729 MHz and CUDA driver version 12.20 retain the log's notation. The corresponding tables do not establish working set, load clocks, temperature or repeat variance.

For this example, assume every capacity class above uses $g$ units and bandwidth GB/s uses decimal byte/s. The 2 GB / 256 GB/s part has the largest ratio:

$$\rho_{\max}=\frac{256\times10^9}{2g}\approx119.21\ \mathrm{s}^{-1},\qquad \rho_{\max}(8g)=1024\times10^9\ \mathrm{byte/s}.$$

**If** 1165.79 GB/s were a justified lower bound on actual DRAM bandwidth, then

$$C_p\ge\frac{1165.79\times10^9}{256\times10^9/(2g)}\approx9.108g>8g.$$

This conclusion is not based on resemblance to A100. It addresses **bandwidth that an ordinary 8 GB-class construction cannot supply using the selected public component set**. However, S87's range across vector widths is not an error interval and its minimum is not an established $B_L$. The component set is also not known to be exhaustive. Therefore this document makes no definitive physical-surplus finding: it retains a source-grounded, conditional inconsistency.

**Sensitivity to the component set:** S36's 2016 research material includes two-, four- and eight-die configurations and a roughly 307 GB/s figure, without establishing that every configuration reaches that maximum. Favor the ordinary countermodel by allowing 2.4 Gb/s / 307.2 GB/s even for a 2 GB part. The ceiling for $8g$ then becomes 1228.8 GB/s: 1165.79 lies inside, whereas 1355.40 is about 10.3% above it. Exceeding the baseline set's 1024 GB/s is therefore sensitive to the permitted component conditions. **We do not claim that all 2 GB parts worldwide are limited to 2 Gb/s.** The measured lower bound also remains unresolved, so this sensitivity exercise still does not establish physical surplus.

## 4. Ordinary constructions must change the conclusion

| Target | Ordinary explanation supported by the part literature | Present implication |
| --- | --- | --- |
| MI50 16 GB, 1 TB/s, 4096-bit [S38] | Four 2016 4 GB / 256 GB/s parts give 16 GB / 1024 GB/s [S90] | A same-bandwidth 32 GB sibling alone does not favor surplus; this is not identification of the target BOM |
| A30X 24 GB, 1223 GB/s [S10] | Three 8 GB / 3.2 Gb/s part examples give 24 GB / 1228.8 GB/s [S01] | Lower density and signal speed can explain the ratio; target width, qualification and actual population remain separate questions |
| CMP 100-200, approximately 6 GB class [S05] | Three 2 GB-class parts explain capacity; the cited example permits up to 256 GB/s each [S93] | Same-unit width and bandwidth are needed; 768 GB/s is this example's ceiling, not a CMP measurement |

These are not assertions that the actual BOM has been identified. They are concrete countermodels to the claim that the specifications require surplus. An ordinary construction does not prove absence of surplus; it means **the current observation does not favor surplus over that explanation**.

The old ranks for the eleven new predictions are blanked and replaced by `ordinary_fit` (ordinary explanation in the public part literature), `information_gap` (insufficient target inputs) and `topology_gap` (the identity of additional physical population is the question). See the [candidate table](current-ranking.md). These classes are not probability tiers. Investigating CMP 100-200's same-unit width, bandwidth and part speed or identity first is a document-research decision because those inputs can constrain its ordinary construction, not a finding that it has the greatest chance of surplus. Establishing 3072-bit width alone would still permit three ordinary 2 GB parts.

## 5. Competing explanations and historical context

Alternatives for the 170HX inconsistency include unlisted fast low-density parts, speed selection or operation outside published conditions, cache or other contributions to apparent bandwidth, and capacity units/reservations. Describe the required part or operating condition and its evidence, rather than treating every conceivable alternative as equally supported. An FMA/non-FMA performance difference also fits low-density HBM with compute throttling; do not count it as additional capacity evidence.

History supports a separate manufacturing forecast when it identifies **the changeable production stage, compatible part or package, decision time and substitution costs**. A general shortage, shared generation, later launch or common brand does not promote a candidate. A sale date is not a package-production date, and denser inventory has alternative uses and opportunity cost. Do not invoke an unspecified favorable lot to escape contrary observations.

## 6. H / T / D / C / U: decisions that public records can update

| Item | Operation |
| --- | --- |
| **H: falsifiable hypothesis** | For an identified SKU/part group and source date, predict that its bandwidth lower bound exceeds the ordinary part-set ceiling within the comparison capacity. Health and accessibility are separate hypotheses |
| **T: minimum check** | For an individual construction, one attributable configuration is the minimum unit. Match capacity, bandwidth definitions and component conditions to that target. Existing records suffice; ownership or modification is not required. Stop this comparison once an ordinary construction works or a specific unresolved input is identified |
| **D: decision** | **PASS (within-set conflict):** justified $B_L>\rho_{\max}C_U$. This is not a physical finding excluding unlisted alternatives. **FAIL (this discriminator):** an ordinary construction satisfies the target conditions, not proof of no surplus. **UNCERTAIN:** part conditions, capacity or bandwidth lower bound cannot be established |
| **C: failure modes** | A qualified fast low-density part, corrected speed conditions, cache/compression, corrected capacity interpretation, or mixed SKUs |
| **U: uncertainty** | Evaluate measurement uncertainty only when repeated observations and systematic-error information support it. Incomplete component coverage and unresolved qualification are structural uncertainty; do not invent combined uncertainty or a coverage factor for them |

## 7. Related fields and ERROR CHECK

**Computer architecture** separates width, rate, cache and actual traffic. **Packaging and reliability engineering** separate compatibility, population and health. **Constraint solving and inverse problems** enumerate ordinary constructions that produce the same observations and identify discriminating conditions. **Industrial economics and causal inference** examine substitution timing, alternative costs and manufacturing cohorts. This approach transfers to other memory types and disabled compute resources.

- Conditional capacities are not registered as measurements; part existence is not target adoption.
- The argument does not omit 2 GB parts, rely on comparison-GPU ratios alone or infer capacity from compute throttling.
- Measurement ranges and error intervals, calculated peaks and measurements, remain distinct.
- Physical surplus, healthy surplus, accessibility, usefulness and population prevalence remain different claims.
- The known 170HX case is retrospective illustration, not an independent test of predictive accuracy on unknown candidates.
