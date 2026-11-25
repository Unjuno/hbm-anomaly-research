# Capacity constraints: what a bus width can exclude

[日本語](capacity-constraints.ja.md) · [Home](../README.md) · [Physical theory](theory.md) · [Current ranking](current-ranking.md) · [Sources](sources.md)

**v0.8.0 — 2026-11-26 JST. Theoretical deductions; no original hardware measurements.**

The useful next step is to test a **specific explanation** against capacity and interface constraints. A wide bus does not establish hidden memory, but it can contradict a proposed density or a whole-stack-only explanation. This note separates three causes of a capacity deficit: inactive memory partitions, unexposed addresses behind active partitions, and reporting reservations. None alone establishes healthy or recoverable memory.

**Classification:** manufacturer specifications below are sourced facts; the equations are deductions under declared assumptions; candidate constructions are hypotheses. An arithmetically admissible construction is not evidence that its parts were qualified, manufactured together, or installed on a particular unit.

## 1. Model scope and implementation assumptions

Use one identified physical GPU, package revision and configuration. Do not combine a width from one board with a capacity from another. The following are assumptions to check, not universal properties of every GPU:

1. For the capacity identities, every real HBM stack has the same full native data width. The count bound in section 5 needs only an upper bound on each stack's width. Dedicated parity and repair-spare cells are excluded from ordinary-data capacity; defective ordinary locations are not automatically excluded. Dummies and empty sites are not memory stacks.
2. Each stack consists of equal-capacity, equal-width memory partitions. Enabling a fraction of these partitions enables the same fraction of its raw ordinary-data capacity. A width reduction means partition selection, not a narrower serialization mode that still addresses the entire stack. A mapping that transfers a disabled partition's capacity through another partition would require a different model.
3. The width is the actual aggregate active **data-lane count**. A controller's design maximum, clock-derived estimate, ECC pins, marketing aggregate across GPUs, or a virtual-instance allocation is not an interchangeable input. Measured application bandwidth alone does not identify this width [theory](theory.md).
4. The exposed capacity counts distinct on-device ordinary-data locations. Aliased addresses, host spill, peer memory and managed-memory oversubscription do not add local HBM [S30]. Addressability does not imply health.
5. A reported capacity is related to exposed capacity only when its accounting is established. Driver total, free, reserved, BAR aperture, MIG/vGPU capacity and product labels have different meanings [S31]. In particular, advertised capacity is not automatically the exposed byte count.
6. The normalized 1024-lane reference is applicable to the HBM2/2E/3 examples here [S01,S82]. HBM2E and HBM3 have different channel/pseudo-channel organizations [S82]. Divisibility by a channel width does **not** prove that a particular GPU can independently disable that channel. The allowed masks must come from the actual implementation; arbitrary fractions are only a mathematical relaxation.

The model's restrictions make a proposed explanation falsifiable. If a restriction fails, revise that model; do not call the hardware impossible.

## 2. Variable table

`byte` and `bit` are information units, not SI base units; `1` denotes a dimensionless count or ratio. All capacity equations use exact bytes in one convention. The numerical examples introduce an explicit hypothetical scale instead of silently converting a vendor's “GB” label into GiB.

| Symbol | Meaning / 日本語 | Unit | Definition | Domain / assumptions | Type |
| --- | --- | --- | --- | --- | --- |
| $n$ | Physical stack count / 実装スタック数 | 1 | Number of real memory stacks on the target | Positive integer; excludes dummies and empty sites | Scalar |
| $i$ | Stack index / スタック添字 | 1 | Identifies one of the $n$ stacks | Integer from 1 through $n$ | Scalar |
| $d_i$ | Stack data capacity / スタックの通常データ容量 | byte | Ordinary-data capacity physically present in stack $i$ | Positive integer; excludes dedicated parity/spares, may include faulty ordinary cells | Scalar |
| $w_s$ | Common full-stack width / 共通フルスタック幅 | 1 | Full native data-lane count shared by stacks in the capacity model | Positive integer; 1024 in the stated HBM2/2E/3 examples; an upper bound alone suffices only for the count bound | Scalar |
| $w$ | Active aggregate width / 有効データ幅 | 1 | Aggregate active data lanes of this GPU | Positive integer; actual width, not an unsourced design maximum | Scalar |
| $a_i$ | Active partition fraction / 有効区画率 | 1 | Fraction of stack $i$'s equal-width, equal-capacity partitions enabled | Between 0 and 1; actual allowed masks and integer lane/byte counts must be respected | Scalar |
| $f_i$ | Exposed address fraction / アドレス公開率 | 1 | Distinct exposed fraction of the enabled partitions' ordinary capacity | Between 0 and 1; set to 1 by convention if $a_i=0$; not a health fraction | Scalar |
| $C_p$ | Physical data capacity / 物理データ容量 | byte | Sum of the $d_i$ | Nonnegative integer | Scalar |
| $C_e$ | Enabled-partition budget / 有効区画の生容量 | byte | Capacity behind active partitions before address-depth restrictions | Nonnegative integer; proportional-partition assumption required | Scalar |
| $C_a$ | Distinct exposed capacity / 重複のない公開容量 | byte | Distinct on-device ordinary locations exposed before reporting-only deductions | Nonnegative integer; excludes aliases and nonlocal storage | Scalar |
| $C_r$ | Specified reported total / 対象とする報告総容量 | byte | One identified total-memory field after its semantics are resolved | Nonnegative integer; not arbitrary free memory or a label | Scalar |
| $Q$ | Reporting deduction / 報告上の控除容量 | byte | Ordinary-data bytes omitted from that field while still included in $C_a$ | Between 0 and $C_a$; relation must be demonstrated, not assumed | Scalar |
| $H_{off}$ | Inactive-partition capacity / 無効区画の容量 | byte | Ordinary-data capacity behind inactive partitions | Nonnegative integer; not evidence of healthy memory | Scalar |
| $H_{depth}$ | Unexposed active-partition capacity / 有効区画内の非公開容量 | byte | Active-partition capacity not distinctly exposed | Nonnegative integer; does not specify cause or reversibility | Scalar |
| $N_e$ | Width equivalents / 幅換算スタック数 | 1 | $w/w_s$ | Positive real; not the physical stack count | Scalar |
| $d$ | Assumed common density / 仮定する共通容量 | byte | Common $d_i$ in the uniform-density submodel | Positive integer; must be independently justified for a factual conclusion | Scalar |
| $C_0$ | Advertised baseline / 公称基準容量 | byte | Advertised ordinary-data baseline after resolving its byte convention | Positive integer; an unresolved interval retains possible integer byte counts | Scalar |
| $\Delta_p$ | Physical excess / 公称基準からの物理的超過 | byte | $C_p-C_0$ | Signed integer; positive does not imply usability | Scalar |
| $d_{min}$ | Assumed density lower bound / 仮定する容量下限 | byte | Lower bound on every actual $d_i$ in the stated model | Positive integer; a comparison product is not a valid bound by itself | Scalar |
| $d_{max}$ | Assumed density upper bound / 仮定する容量上限 | byte | Upper bound on every actual $d_i$ in the stated model | Positive integer, at least $d_{min}$; scope must be established | Scalar |
| $n_{max}$ | Assumed population limit / 仮定する実装数上限 | 1 | Upper bound on actual real stacks in the stated package | Positive integer; a related GPU's interface count is insufficient alone | Scalar |
| $g$ | Example capacity scale / 数値例の容量単位 | byte | Exactly $2^{30}$ bytes in the hypothetical examples | Fixed positive constant; does not resolve any vendor label | Scalar |
| $\theta$ | One configuration / 一つの構成 | Mixed | Tuple of population, densities, masks, exposure and accounting parameters | Satisfies the explicitly chosen model | Tuple |
| $E$ | Observations / 観測情報 | Mixed | Sourced identity, widths, capacities, parts and any justified intervals | Same-unit observations distinguished from analogies and unknowns | Data set |
| $M$ | Model assumptions / モデルの仮定 | None | Stated topology, density, mask and accounting restrictions | May be incomplete; not silently supplied by comparison products | Set of assumptions |
| $\Theta(E,M)$ | Admissible configurations / 制約と整合する構成集合 | None | Configurations consistent with $E$ under $M$ | May be empty; arithmetic admissibility does not establish qualification | Set |
| $L_\Delta$ | Conditional excess lower bound / 条件付き超過下限 | byte | Infimum of $\Delta_p$ over the admissible set | Defined only for a nonempty set; any finite bound is attained in this integer-byte model | Extended-real scalar |
| $U_\Delta$ | Conditional excess upper bound / 条件付き超過上限 | byte | Supremum of $\Delta_p$ over the admissible set | Defined only for a nonempty set; any finite bound is attained, while an unbounded result is possible | Extended-real scalar |

## 3. Derive the three-way decomposition

By the partition assumptions, active width and enabled capacity are

$$
w=w_s\sum_{i=1}^{n}a_i,\qquad
C_p=\sum_{i=1}^{n}d_i,\qquad
C_e=\sum_{i=1}^{n}a_i d_i,\qquad
C_a=\sum_{i=1}^{n}a_i f_i d_i.
$$

Define the two physical deficits without overlap:

$$
H_{off}=\sum_{i=1}^{n}(1-a_i)d_i,\qquad
H_{depth}=\sum_{i=1}^{n}a_i(1-f_i)d_i.
$$

For each stack, its enabled and inactive fractions sum to its total capacity. Summing that identity gives the first equality below. Within the enabled fraction, exposed and unexposed fractions also sum to the enabled capacity, giving the second:

$$
C_p=C_e+H_{off},\qquad
C_e=C_a+H_{depth}.
$$

Substituting the second equality into the first and subtracting exposed capacity gives

$$
\boxed{C_p-C_a=H_{off}+H_{depth}}.
$$

Only if the specified reporting semantics establish the following relation may reporting be added:

$$
C_r=C_a-Q
\quad\Longrightarrow\quad
\boxed{C_p-C_r=H_{off}+H_{depth}+Q}.
$$

Thus a larger reported total after a change might reclaim a reporting deduction without finding any memory beyond the advertised baseline. Conversely, an inactive stack may be physically present while contributing nothing to currently accessible capacity. These equations describe location accounting, not firmware intent or reliability.

**Dimension check:** every capacity term is a dimensionless fraction multiplied by bytes, and all additions/subtractions have unit byte. Both sides of the width equality are dimensionless lane counts. No memory clock or bit/byte bandwidth conversion is needed for these identities.

## 4. What an independently identified common density would establish

Assume every populated stack has the same ordinary-data capacity. Substitution into the enabled-budget definition yields

$$
d_i=d\ \text{for every }i
\quad\Longrightarrow\quad
C_e=d\sum_{i=1}^{n}a_i=d\frac{w}{w_s}=dN_e.
$$

Every exposure fraction is at most one, so

$$
C_a\le C_e=dN_e.
$$

This produces three different decisions:

| Exact-byte comparison | Deduction under the model | What it does not establish |
| --- | --- | --- |
| $C_a>dN_e$ | The chosen density/partition/width model is inconsistent. Adding completely inactive stacks cannot fix it: they add neither enabled capacity nor active width. | That the product specification is false, or that a larger hidden density is the unique explanation. |
| $C_a=dN_e$ | $H_{depth}=0$. Every enabled stack fraction must be fully exposed, because a sum of nonnegative deficits can vanish only when each enabled term vanishes. | No physically extra stack exists; inactive capacity can still be present. |
| $C_a<dN_e$ | $H_{depth}>0$. Whole-stack or whole-channel disable **alone**, with all enabled address depths fully exposed, cannot explain this pair of width and capacity. | A firmware lock, healthy extra cells, or a way to recover them. |

The equality proof uses positive stack capacity: an enabled term can vanish only when its exposure fraction is one. For an inactive stack the exposure fraction has no effect. The strict-deficit result follows directly by subtracting exposed capacity from the enabled budget. It permits defects, remapping exclusions and configuration restrictions as causes; it is not a diagnosis of any one cause.

If only a reported field is available, unresolved reporting deductions prevent substituting it for exposed capacity. Evaluate all justified accounting possibilities. Likewise, the equality of two rounded “GB” labels is not the exact-byte equality in this theorem.

## 5. Width gives a lower count bound, not an exact population

For this count bound alone, each real stack need only supply at most the reference width; the native widths need not all be equal. Summing the at-most contribution from each of the $n$ stacks gives

$$
w\le nw_s
\quad\Longrightarrow\quad
N_e=\frac{w}{w_s}\le n
\quad\Longrightarrow\quad
\boxed{n\ge\lceil N_e\rceil}.
$$

Division is valid because the reference width is positive; the last step uses integer stack count. This is a lower bound on real stacks needed to supply a verified width, not a count of all installed stacks. Completely inactive stacks can increase the physical count without changing the width. The weaker upper-width assumption alone does not justify the capacity identities or uniform-density theorem in sections 3–4. In the more restrictive whole-stack-only model with a common full native width, each active fraction is zero or one, so their sum, the width equivalents, must be an integer.

If every actual density and the package's population limit are independently bounded, then

$$
C_p\ge\max\left(C_a,\lceil N_e\rceil d_{min}\right),
\qquad
C_p\le n_{max}d_{max}.
$$

For the lower bound, physical capacity contains exposed capacity; also, at least the ceiling number of stacks is present, and each contributes at least the density lower bound. For the upper bound, there are at most the stated number of stacks and each contributes at most the stated upper bound. Both products have unit byte. These bounds may be loose. If the density or population domain is unknown, leave that bound unknown; do not insert a favorite comparison density or another SKU's package geometry.

Uniform density is substantive. With mixed densities, enabled capacity is a weighted sum, so the same exposed capacity and width can admit additional ordinary constructions. An unsupported uniformity assumption can create a false anomaly.

## 6. Conditional examples and countermodels

**Unit rule for this section:** the first column quotes vendor capacity *labels*. The model column instead uses the declared example unit $g$, exactly one GiB. It conditionally assumes the exposed byte count equals the displayed integer times $g$, with reporting deductions removed. This is illustrative arithmetic, not a claim that a source established that exact byte count. The models require qualification and mapping evidence before being applied to hardware. All stack densities in these constructions are hypotheses.

| Target and sourced input | Explicit hypothetical construction | What the constraint resolves | First missing discriminating evidence |
| --- | --- | --- | --- |
| **A30:** 24 GB, 3072 data lanes [S06] | Three active $8g$ stacks, all exposed: $24g$ physical. Adding a fourth inactive $8g$ stack gives $32g$ physical with the same exposed $24g$. Alternatively, three active $16g$ stacks half exposed give $48g$ physical; compatibility of this last construction is unknown. | At common density $8g$, enabled budget is $24g$; any extra capacity in that submodel is behind inactive partitions. The $16g$ alternative instead requires unexposed depth. Common density $4g$ cannot supply exposed $24g$ at this width, even with more completely inactive stacks. | Actual real-stack population, part density and part/package compatibility on an identified A30. |
| **MI50 16 GB:** 4096 lanes; a 32 GB configuration also has 4096 lanes [S38,S80] | Four active $4g$ stacks fully exposed give $16g$. Four active $8g$ stacks with half their addresses exposed also give $16g$, with $32g$ physical. | Width and exposed capacity alone do not distinguish these models. If $8g$ density were established, whole-stack disable alone would not explain the same full width with exposed $16g$. | Actual density on an original 16 GB unit, separated from repaired cards and stale labels. |
| **A800 40 GB Active:** 5120 lanes [S71] | Five active $8g$ stacks fully exposed give $40g$. A sixth inactive $8g$ stack gives $48g$ physical. Five active $16g$ stacks half exposed give $80g$ physical. | The $48g$ and $80g$ constructions require different mechanisms: inactive population versus unexposed depth. A single vague “restriction” does not establish either. | Package population and compatible part density; the higher-density construction also needs compatibility evidence. |
| **RX Vega 64 8 GB:** 2048 lanes [S45]; do not transfer an unverified width to a different Vega variant | Two active $4g$ stacks fully exposed give $8g$. Two active $8g$ stacks half exposed give $16g$ physical and exposed $8g$. | This is the same non-identification as MI50. A shared PCB does not identify the soldered package [S46]. | Factory-origin package and part identities for the exact RX unit. |
| **CMP 100-200:** approximately 6 GB-class runtime observation; width not established [S02,S05] | **Only if** width were 3072 and exposed capacity $6g$: three active $2g$ stacks fully exposed, or three active $4g$ stacks half exposed, fit the arithmetic. | No factual density screen is currently available. The two-die HBM2 design possibility in S36 neither qualifies a $2g$ part for CMP nor permits assuming a universal $4g$ minimum. | Same-unit width, exact byte count, identity and part/population evidence. |
| **H100 SXM5 64 GB HBM2e:** named physical configuration, actual width not established here [S60,S64] | At hypothetical common density $16g$: width 4096 can expose $64g$ at full depth; width 5120 would require $16g$ of unexposed enabled capacity to expose $64g$; width 6144 would require $32g$. | These are alternative conditional branches, not a width claim. Mixed-density populations can produce other full-depth totals; the uniform-density assumption matters. | Same physical SKU's width, HBM generation, population and density. |
| **H100 NVL 94 GB HBM3:** 6016 lanes [S72], a different configuration from the HBM2e 64/94 GB support entries | Hypothetical common density $16g$ gives enabled budget $94g$ at this width. Six real $16g$ stacks would give $96g$ physical, with $2g$ behind inactive partitions. | Width equivalents are not an integer, so whole-stack-only activation cannot explain this width. At most 1024 lanes per stack requires at least six real stacks. The width alone does not establish their density, $96g$ total, health, or reversibility. | Density/population evidence before promoting this ordinary geometry comparison to a physical-excess claim. |

### 6.1 Complete counterexample: MI50-shaped observations

Take an exact hypothetical exposed capacity of $16g$ and a width of 4096 with a 1024-lane stack reference. In the first model, set four stack capacities to $4g$, all active fractions to one and all exposure fractions to one. Summing gives physical and exposed capacities of $16g$ and width 4096. In the second model, keep the count and active fractions, set all capacities to $8g$ and all exposure fractions to one half. Physical capacity becomes $32g$, exposed capacity remains $16g$, and width remains 4096. Both models therefore produce the same two observations while disagreeing on physical excess. Those observations alone cannot identify physical capacity within the model. This is an information-limit proof, not evidence that the second assembly exists.

### 6.2 A30: a specific alternative can be excluded

The A30 brief describes its native HBM2 ECC as imposing no capacity or bandwidth overhead [S06, printed p.1]. Thus routine ECC overhead is not a supported explanation for turning a hypothetical 32 GB ordinary-data population into the advertised 24 GB. This excludes that **particular accounting story**; it does not establish 32 GB population, eliminate runtime reservations, or generalize to other SKUs. Its 32 GiB BAR1 entry is an address window, not an independent memory-density observation [S06].

### 6.3 H100 64 GB: why a generic “half hidden” story can fail

Consider only the explicitly restricted hypothetical model with at most six real stacks, no stack exceeding $16g$, and every enabled stack fraction exposing at most half its depth. Since active fractions are at most one,

$$
C_a=\sum_{i=1}^{n}a_i f_i d_i
\le\frac12\sum_{i=1}^{n}d_i
\le\frac12\,(6)(16g)=48g.
$$

It cannot expose $64g$. This rejects the **uniform half-depth explanation within that density/population bound**, not the H100 64 GB configuration or all excess-capacity hypotheses. Larger densities, different restrictions, mixed exposure fractions, or a different package domain change the model. The six-stack and $16g$ limits are assumptions here, not established bounds on the target's complete compatible-parts history.

## 7. Partial identification instead of a guessed probability

Record every admissible configuration under the observations and declared assumptions. For a nonempty set, define

$$
\Theta(E,M)=\{\theta:\theta\text{ satisfies }E\text{ under }M\},
\qquad
\Delta_p(\theta)=C_p(\theta)-C_0(\theta),
$$

$$
L_\Delta=\inf_{\theta\in\Theta(E,M)}\Delta_p(\theta),
\qquad
U_\Delta=\sup_{\theta\in\Theta(E,M)}\Delta_p(\theta).
$$

If the baseline convention is unresolved, retain the justified baseline possibilities inside the configuration rather than mixing incompatible extrema. Then:

| Conditional result | Proper interpretation |
| --- | --- |
| $L_\Delta>0$ | Every admissible configuration has physical excess **under these assumptions**. This sufficient condition is not a claim of health or recovery. |
| $U_\Delta\le0$ | Positive physical excess is excluded within the stated model and scope. |
| Ordinary and positive-excess configurations are both admissible | The observations do not identify whether physical excess exists. Show both constructions. |
| The admissible set is empty | Inputs or assumptions are inconsistent. Diagnose identity, units, width, density, mapping and accounting before inferring anything about hardware. |
| A bound is unbounded or a needed parameter domain is unknown | Report the missing bound. Do not substitute a numerical likelihood or guessed maximum. |

All capacities in this model are exact integer bytes, so every finite lower or upper bound on a nonempty admissible set is attained, even if that set contains infinitely many parameter tuples. To see this for the lower bound, translate the possible integer excesses by an integer lower bound: the resulting nonempty set of nonnegative integers has a least member. Translating back gives an attained minimum. Reversing signs gives the corresponding upper-bound proof. Consequently a finite zero lower bound does include a zero-excess model. Unbounded results remain possible when the parameter domain permits them.

A finite, explicitly listed scenario worksheet makes the assumptions easier to audit, but its scenario counts are **not probabilities**. Counts change with grid choices, unsupported density options and duplicate permutations. Rejecting several toy explanations does not calibrate the chance of the remaining one. A worksheet containing only selected examples also cannot exclude configurations outside its declared domain.

No enumerator is needed to make the current deductions. If one is later added, it should output assumptions, ordinary/excess countermodels, conditional bounds and inconsistencies, with exact byte arithmetic and implementation-qualified masks. Unknown-width candidates must retain separate scenario-only branches.

## 8. H / T / D / C / U: turn the constraint into a bounded question

| Item | Unit-scoped application |
| --- | --- |
| **H — falsifiable hypothesis** | Name a board and original configuration, a density/population construction, its proposed inactive-partition or depth mechanism, and the observation date. Example: an identified 16 GB MI50 uses four $8g$ stacks, while its full 4096-lane enabled population exposes only $16g$ after accounting is resolved. This is a hypothesis, not an existing finding. |
| **T — minimum discriminating evidence** | One identified unit can test that unit's construction: source its width, part capacities/population, exact original capacity and reporting semantics. Existing documents or owner observations may suffice; the present release does not require a purchase or firmware change. Stop when the construction is contradicted, its physical population is established, or a named missing fact prevents a decision. One unit does not estimate prevalence. |
| **D — PASS / FAIL / UNCERTAIN** | PASS for physical excess requires independently supported population exceeding the resolved baseline, or assumptions covering the actual unit that force a positive lower bound. FAIL rejects only the named construction when its necessary conditions conflict with established observations. UNCERTAIN applies when ordinary and excess models remain, or a decisive assumption is unknown. Mere arithmetic consistency is not PASS. Functional excess requires the separate [validation protocol](validation.md). |
| **C — competing explanations** | Lower-density parts; fewer real stacks; inactive partitions; restricted or retired address regions; an unsupported partition model; a repaired assembly; a stale label; virtual/nonlocal memory; reporting deductions. Preserve the strongest ordinary construction. |
| **U — uncertainty** | Separate exact integer arithmetic from uncertainty in identity, units, topology, qualification and reporting. Use documented intervals when justified. Structural unknowns are not measurement noise; no combined standard uncertainty or coverage factor is assigned without an applicable error model. |

This connects **computer architecture** (width and mappings), **packaging/reliability** (real parts versus dummies and faults), **metrology** (byte conventions and reporting), and **inverse problems/statistics** (what observations identify). Supply history can motivate which cohort to inspect, but cannot supply a missing density bound.

**Next question:** which single obtainable observation would remove the ordinary construction for a named unit: its actual stack count, its part density, or the distinction between reported and distinctly exposed bytes?

## ERROR CHECK

- The deficit identity partitions capacity without counting reporting deductions twice.
- Width equivalents supply a conditional lower stack-count bound, not an exact physical count.
- Channel arithmetic and allowed disable masks are different; implementation compatibility is explicit.
- A common density, minimum density and package maximum are assumptions requiring their own evidence.
- The MI50 counterexample proves non-identification inside the model; it does not prove a hidden assembly exists.
- H100 NVL HBM3 is not conflated with the 64/94 GB HBM2e support entries.
- All numerical constructions use an explicit hypothetical GiB scale; vendor labels and actual byte counts remain distinct.
- Physical excess, healthy excess, recoverability, cohort prevalence and manufacturing cause remain separate claims.
