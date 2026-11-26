# Theory: what specifications can and cannot identify

[Home](../README.md) · [Sources](sources.md) · [Capacity constraints](capacity-constraints.md) · [Manufacturing causality](manufacturing-causality.md) · [Validation protocol](validation.md)

This physical model supports the [current hypothesis ranking](current-ranking.md). Its descriptive ratios do not compute that order. The v0.9 [historical-recurrence forecast](recurrence-hypotheses.md) also weighs repeated productization decisions, part/package lineage, manufacturing context and the strength of ordinary explanations. Those inputs can change a forecast before physical population is established.

The [v0.7 refinements](inference-refinement.md) add concrete address-density versus disabled-stack mechanisms, manufacturing-stage constraints and publication-feedback rules without changing this model.

The [capacity-constraint model](capacity-constraints.md) derives conditional bounds and separates inactive interfaces from unexposed address depth. The [manufacturing-causality model](manufacturing-causality.md) identifies the additional historical evidence needed to explain why a construction was produced.

## 1. Separate the claims before collecting evidence

This project investigates whether a specified board variant contains ordinary HBM data capacity beyond its advertised baseline, and whether any of that capacity works. Four claims require different evidence:

| Claim | Evidence that could support it | What that evidence does not establish |
| --- | --- | --- |
| **Physical population:** installed ordinary data capacity exceeds the baseline | Legible part identification, applicable manufacturer documentation and independently established population | Healthy cells, accessible addresses or a recovery method |
| **Functional extra capacity:** additional distinct on-device storage works | Address-sensitive tests beyond a correctly defined baseline, residency checks and documented conditions | Universal reliability or the same result on every board |
| **Cohort dependence:** documented revisions or production cohorts differ | Comparable identified units, including negative results, with reliable manufacturing-stage dates | A particular shortage caused the difference |
| **Manufacturing cause:** supply conditions motivated substitution | Relevant sourcing/change records or other evidence discriminating competing pathways | Merely occurring in a shortage period is insufficient |

An unusually high bandwidth-to-capacity ratio is a **screening observation**, not any of these conclusions. Price changes also require competing explanations. Driver reports, virtual address ranges and PCIe BAR apertures are not measurements of installed DRAM. For example, the A30 product brief lists 24 GB of memory and a 32 GiB BAR1 aperture [S06].

## 2. Variables, units and scope

The equations concern one GPU, a specified configuration and a common data-capacity convention. Information units are explicit: bit and byte are not SI base units; time uses SI seconds. One byte is exactly eight bits. Decimal GB/s means billions of bytes per second; GiB means binary gibibytes. A capacity label alone does not establish which byte count a vendor's “GB” denotes.

| Symbol | Meaning | Unit | Definition | Domain / assumptions | Type |
| --- | --- | --- | --- | --- | --- |
| $w$ | Active **user-data** lane count | 1 | Count represented by a sourced “$w$-bit bus” specification | Positive integer; actual active interface of the same physical GPU/configuration, not an aggregate across GPUs or the die's maximum controller capability | Scalar |
| $w_s$ | Reference full-stack data-lane count | 1 | 1024 for the covered HBM2/2E and HBM3 references [S01,S82] | Positive integer; not universal across generations; a stack-count bound additionally requires this to be a verified maximum per real stack | Scalar |
| $r$ | Effective transfer rate of each active lane | bit/s | Bits transferred per second per lane; DDR already included | Positive real; equal rate across active lanes assumed | Scalar |
| $\kappa$ | Bit-to-byte conversion factor | bit/byte | Exactly 8 bit/byte | Exact constant | Scalar |
| $B$ | Theoretical peak user-data bandwidth | byte/s | Aggregate rate of active data lanes | Positive real; not application throughput | Scalar |
| $C_0$ | Advertised baseline in exact ordinary data bytes | byte | SKU capacity after resolving its label convention | Positive integer; not stock free memory or a BAR size | Scalar |
| $n$ | Physically populated HBM stack count | 1 | Actual memory stacks, excluding dummy spacers or empty sites | Nonnegative integer; width alone does not establish the exact count, but can bound it below under a verified per-stack lane maximum | Scalar |
| $i$ | Stack index | 1 | One populated stack | Integer from 1 through $n$ | Scalar |
| $d_i$ | Ordinary data capacity of stack $i$ | byte | Identified stack's data capacity | Positive integer; excludes parity and repair spares; may include defective ordinary locations | Scalar |
| $C_p$ | Aggregate populated ordinary data capacity | byte | Sum of the $d_i$ | Nonnegative integer; usually unknown without physical evidence | Scalar |
| $\mathcal P$ | Ordinary data locations physically present | Byte-sized locations | Physical locations represented by $C_p$ | Fixed hardware; parity and spare locations excluded | Set |
| $\mathcal A$ | Distinct on-device locations exposed by the configuration | Byte-sized locations | Physical locations accessible through that configuration | Host/peer storage and virtual aliases excluded; locations need not be healthy | Set |
| $\mathcal H$ | Locations satisfying a stated functional condition | Byte-sized locations | Operationally healthy locations under declared conditions | Depends on voltage, clock, temperature, patterns and observation period | Set |
| $\mathcal V$ | Distinct locations with accepted validation evidence | Byte-sized locations | Locations covered by the protocol | Finite evidence, not exhaustive fault coverage or permanent health | Set |
| $\lvert\cdot\rvert$ | Byte-valued size of a location set | byte | Number of byte-sized locations multiplied by one byte | Finite sets of ordinary data locations | Scalar-valued measure |
| $C_v$ | Accepted validated coverage | byte | Cardinality of $\mathcal V$, using byte-sized locations | Nonnegative integer; no double counting across passes or devices | Scalar |
| $N_e$ | Full-stack **width equivalents** | 1 | $w/w_s$ | Positive real; not a physical stack count | Scalar |
| $c_e$ | Baseline capacity per width equivalent | byte | $C_0/N_e$ | Positive real; normalization, not measured density | Scalar |
| $R$ | Peak bandwidth per baseline data byte | s⁻¹ | $B/C_0$ | Positive real; common byte convention required | Scalar |
| $d_{ref}$ | Chosen comparison density | byte | Reference from a stated comparison set | Positive real; **not** automatically the minimum compatible density | Scalar |
| $q$ | Capacity-per-width ratio relative to the comparator | 1 | $c_e/d_{ref}$ | Positive real; descriptive screening proxy | Scalar |

**Normalize the width and generation.** A raw I/O count may include ECC/parity lanes, whereas a bandwidth figure may count only data. Micron distinguishes 1024 user-data lanes from 1152 data-plus-ECC lanes in its technical brief [S01]. Do not insert unlike definitions into the same equation. The covered HBM2E interface has eight 128-lane channels, each divided into two 64-lane pseudochannels. HBM3 keeps 1024 data lanes but divides them into sixteen 64-lane channels and thirty-two 32-lane pseudochannels [S01,S82]. These are interface units, not evidence of a particular GPU's independently disableable units.

**Normalize the rate.** A clock in MHz is not automatically the effective bit-transfer rate; do not apply a DDR multiplier twice. HBM3 changes the relationship between command/address clocks and data strobes [S82]. A field labelled “memory clock” therefore needs its product-specific meaning before conversion; there is no universal multiplier to apply to every reported clock.

**The CSV uses approximate nominal proxies.** The nominal_capacity_gb field retains capacity classes; peak_bandwidth_gbps means decimal **GB/s**, despite the lowercase name. A nominal “8 GB” result must not silently become a measurement of either eight billion bytes or eight GiB. Exact runtime MiB and independently tested bytes have separate fields. See the [data dictionary](../data/README.md).

## 3. Derive the bandwidth and geometry relationships

Each of the $w$ active data lanes transfers at rate $r$. Adding equal rates gives $wr$ bit/s. Conversion to bytes gives

$$B=\frac{wr}{\kappa}.$$

Expressing active lanes in reference-stack widths gives

$$N_e=\frac{w}{w_s}.$$

Dividing baseline capacity by that count gives

$$c_e=\frac{C_0}{N_e}=\frac{w_s C_0}{w}.$$

Substitute the bandwidth expression and rearranged capacity expression into the definition of $R$:

$$R=\frac{B}{C_0}=\frac{wr/\kappa}{wc_e/w_s}=\frac{w_s r}{\kappa c_e}.$$

A high bandwidth-per-byte ratio can therefore result from faster signaling or lower capacity per width equivalent. The ratio alone cannot distinguish them and is unsuitable as a universal cross-generation threshold.

Physical population instead obeys

$$C_p=\sum_{i=1}^{n}d_i.$$

Active width does not establish the **exact** physical stack count or stack densities. It does supply a conditional lower bound: if the reported width is the actual active data interface, and no real stack can provide more than the verified per-stack maximum, at least the active width divided by that maximum, rounded up, must be backed by connected real stacks. For example, 6016 active data lanes require at least six such stacks when each supports at most 1024 lanes. The H100 NVL brief supplies the 6016-lane observation [S72]; the bound does not establish 96 GB of installed capacity or healthy spare memory. See the [complete proof and geometry assumptions](capacity-constraints.md).

Partially active channels, different densities, unpopulated sites, dummy spacers and defective components prevent turning that bound into an exact population or capacity claim. Width alone also puts no upper bound on additional unconnected stacks. Package outline or apparent stack height alone does not establish density: match verified part identity to applicable documentation.

For a stated comparison density, the screen computes

$$q=\frac{c_e}{d_{ref}}.$$

The existing flag at 0.5 or lower is an **uncalibrated prioritization heuristic**. It is not a probability, physical lower bound or detection rate. No claim that $d_{ref}$ is the smallest historically compatible part is implied. Missing or unverified width prevents a defensible width-normalized result.

### Dimensional check

Lane count is dimensionless, so bandwidth has units

$$\frac{1\times\mathrm{bit/s}}{\mathrm{bit/byte}}=\mathrm{byte/s}.$$

The ratio $w_s/w$ is dimensionless, giving $c_e$ units of bytes. Dividing byte/s by byte gives inverse seconds for $R$. Both $N_e$ and $q$ are dimensionless. Treating $w$ as bits and then multiplying it by bit/s would be dimensionally wrong: the “bit” in marketed bus width denotes a lane count here.

### Numerical example

For 1024 data lanes at an effective rate of 3.2 billion bit/s each,

$$B=\frac{1024\times3.2\times10^9\ \mathrm{bit/s}}{8\ \mathrm{bit/byte}}=409.6\times10^9\ \mathrm{byte/s}.$$

That is 409.6 decimal GB/s; the vendor brief rounds to 410 GB/s [S01]. This is a calculated peak, **not a benchmark**. Refresh, access patterns, clocks and other constraints affect observed throughput; caches or compression can make an application's apparent byte rate differ from physical HBM traffic.

## 4. Why bandwidth cannot prove hidden capacity

**Primary-source premise:** Micron documents 8 GB and 16 GB HBM2E classes with the same 1024 data I/O and maximum 3.2 Gbit/s per-pin rate [S01]. Different densities can therefore have the same external peak.

Construct two hypothetical boards using those interface characteristics:

1. Board A uses the lower-density option and exposes its ordinary data capacity.
2. Board B uses the higher-density option but restricts exposure to the lower option's capacity. This restriction is a modeling assumption, not an observation of a particular product.
3. Both have the same active width, transfer rate, calculated peak and exposed baseline. The bandwidth derivation contains no density term, so it gives the same result.
4. Board A has no hidden extra ordinary capacity in this model; Board B does. The shared external specifications therefore do not uniquely identify the physical construction.

This establishes **non-identifiability from that observation set**. It does not show that Board B was manufactured, that its restriction is reversible or that its extra cells are healthy. Verified part density, actual population, sound distinct-address tests or manufacturing records can distinguish the models.

### Capacity, interface width and signaling are separate choices

There is no necessary conservation law forcing capacity to fall whenever bandwidth rises. The following are model comparisons; their stated fixed conditions are necessary, not observations about every product.

| Changed feature | Conditions held fixed | Consequence in the model |
| --- | --- | --- |
| Physical density of an active stack | Data-lane count and effective per-lane rate | Installed ordinary capacity can change while calculated peak bandwidth stays the same; the Micron density alternatives provide an interface example [S01]. |
| Exposed address depth within active memory | Physical parts, active lanes and their effective rate | Exposed capacity changes without requiring a change in external width or calculated peak. Whether such a restriction exists is a separate product-specific hypothesis. |
| Number of active complete identical stacks, or identical channel partitions | Data width and ordinary capacity per partition, full depth exposure and effective per-lane rate | Active width, exposed capacity and calculated peak change proportionately. Partially active stacks require a finer model than a whole-stack on/off assumption. |
| Effective signaling rate | Active width, physical parts and exposure | Calculated peak changes without requiring a capacity change. Qualification, power and thermal limits still constrain the choice. |

For a **same-width comparison**, first verify the physical SKU, data-lane definition, generation and capacity convention. At the same active width, a different calculated peak reflects a different effective per-lane rate in the equal-rate model; it does not identify extra memory. At the same width and rate, differing capacities can still come from lower-density parts or restricted exposure. The width-normalized $c_e$ describes the difference without deciding between those constructions.

Uniform rate, uniform density and uniform activation are **distinct assumptions**. The bandwidth equation assumes a common $r$; it does not assume identical $d_i$, identical active fractions or whole-stack-only activation. The [capacity-constraint model](capacity-constraints.md) states the additional conditions required to reject a proposed density or disabling mechanism.

Qualification depends on controller addressing, package, timing, power and thermal constraints. These relationships establish possibilities within their assumptions, not universal part interchangeability or a manufacturing motive.

## 5. Installed, accessible, healthy and validated are different

As idealized bookkeeping on one GPU, accessible and healthy locations are each subsets of the physically populated data locations:

$$\mathcal A\subseteq\mathcal P,\qquad\mathcal H\subseteq\mathcal P.$$

There is **no general inclusion between** $\mathcal A$ **and** $\mathcal H$. Damaged memory can be addressable; working memory can be inaccessible in a given configuration. When residency, identity and error checks are valid, accepted validation evidence is intended to establish

$$\mathcal V\subseteq\mathcal A\cap\mathcal H.$$

This concerns declared conditions and observation time. Finite patterns cannot prove absence of every mapping error, intermittent fault or future failure. Observations may be misclassified: report coverage and limits instead of claiming exhaustive injectivity from a short test.

Under those conditions, cardinalities give

$$C_v=|\mathcal V|\leq|\mathcal A\cap\mathcal H|\leq C_p.$$

The middle term cannot generally become an ordered chain of “addressable capacity” and “healthy capacity.” Nor may an advertised label or a reported virtual-space size be substituted for a physical-set cardinality.

Functional extra capacity requires, as a necessary condition, accepted distinct on-device coverage exceeding the correctly defined baseline:

$$C_v>C_0.$$

The [operational decision rule](study-design.md) is stronger: it also requires the predeclared minimum additional capacity, evidence gates, repetitions and error criteria. The inequality alone does not assign PASS.

Exceeding stock **free** memory may merely reclaim reservations. Testing an address numerically above the nominal boundary is also insufficient: it may alias a lower address. Evidence must cover distinct, simultaneously resident storage without summing repeated reuse across tests.

Managed allocations can exceed device memory and migrate to host memory on supported CUDA systems [S30]. NVIDIA also documents reservations, ECC accounting, retired pages and remapping [S31]. These are concrete alternatives to interpreting every capacity-report change as new DRAM. Record allocation backend, device identity, residency evidence, ECC, clocks, temperatures and errors.

**A product-specific discriminator:** the A30 product brief, printed p.1, states that its native HBM2 ECC has no memory-capacity or bandwidth overhead [S06]. Explaining its nominal 24 GB as a hypothetical 32 GB of ordinary payload minus 8 GB consumed solely by ECC contradicts that accounting description. This does not prove the physical population, make ECC cells ordinary payload, or establish that runtime reservations are zero; the statement must not be generalized to every GPU.

Practical usability is a separate workload question. A configuration may pass a capacity test while lacking reliable drivers, required instructions, adequate bandwidth or workload stability. Report its operating envelope rather than hiding these conditions inside a capacity number.

## 6. Apply the screen without promoting assumptions to specifications

These are **nominal GB-class proxies**, not exact physical-byte estimates. Peaks discussed here are specifications or external descriptions, not measurements by this project.

| Configuration | Sourced active data width | Nominal capacity per 1024-lane equivalent | Interpretation |
| --- | --- | --- | --- |
| CMP 170HX, 8 GB class | 4096, community report [S19,S20] | 2 GB class | Ratio 0.25 against a selected 8 GB comparator. A retrospective positive control, not independent heuristic validation. |
| CMP 170HX, 10 GB class | 5120, community report [S19,S20] | 2 GB class | Same flag; exact variant identity still matters [S16]. |
| A30, 24 GB | 3072, manufacturer [S06] | 8 GB class | Ordinary density explains the specification; no strong mismatch against the 8 GB comparator. |
| V100 PCIe, 16 / 32 GB | 4096 for both, manufacturer [S08] | 4 / 8 GB class | Both specify 900 GB/s: different capacities sharing width and peak bandwidth. |
| A30X, 24 GB | Not established by the cited specification [S10] | Not computed | Its 1223 GB/s peak does not establish the missing width or density. |
| CMP 100-200, about 6 GB class | Not established [S02,S05] | Not computed | Verify width and variant first. A conditional 3072-lane calculation is not an observed specification. |

An ordinary ratio does not exclude hidden capacity. An unusual ratio may reflect low-density parts, partially active stacks, defective regions or bad source data. The [candidate register](candidates.md) separates screening priority from evidence status.

## 7. Connect physical theory to history and prices

Production-time substitution is a plausible **conditional hypothesis**: a qualified higher-density assembly might be economical when a nominally cheaper input is unavailable. Existing inventory nevertheless has opportunity cost, qualification and yield may differ, and HBM is package-integrated rather than freely interchangeable as any board component. A shortage announcement neither dates an individual board nor establishes its bill of materials.

The [lot-history model](lot-history.md) details the economic comparison and date distinctions; the [manufacturing-causality model](manufacturing-causality.md) separates production stages and competing causes. Predeclare product identity, revision/date interval, observation criteria and stopping rule. Repeatedly moving a proposed cohort after negative results would make the claim effectively unfalsifiable. A failed recovery method rejects that method under its tested conditions; it does not alone establish absence of physical capacity. A positive sample establishes that sample, not market prevalence.

The [market protocol](market.md) treats price as a secondary signal. AI demand, performance-only changes, adapters, supply releases, condition and speculation can produce the same pattern. A revision-specific verified transaction premium can justify collecting hardware evidence, but it cannot prove hidden memory or manufacturing cause. This release has no validated market time series or significance claim.

## 8. Make the research informative

The [study design](study-design.md) fixes bounded hypotheses, thresholds and stopping rules; the [validation protocol](validation.md) specifies observation records and claim-specific PASS/FAIL/UNCERTAIN decisions. Screening chooses **what to inspect next**, not what to buy or what an alteration will recover. Independent owners help replicate findings; convenience samples and repeated reports from one supply chain do not establish population prevalence.

Uncertainty has different forms. Rounded bandwidth specifications and throughput variability may support numerical uncertainty calculations when error models exist. Unknown identity, unresolved GB/GiB labels, incomplete residency checks and selection bias are structural gaps. An invented combined uncertainty or confidence percentage would conceal them; record them and retain competing explanations.

Related fields contribute distinct tests: **computer architecture** establishes interfaces and mappings; **semiconductor packaging and reliability** establish population and fault behavior; **industrial economics** explains conditional substitution incentives; **statistics and causal inference** distinguish replication, selection effects and historical correlation from prevalence or cause.

## ERROR CHECK

- Lane counts are dimensionless; bit/byte conversion is explicit. Raw clocks differ from effective rates.
- Ordinary data capacity excludes parity and spares. Effective width does not identify the exact physical stack count; a lower bound requires a verified active interface and maximum lanes per stack.
- HBM2E and HBM3 channel widths differ. Interface granularity does not establish a GPU's disabling controls; uniform rate, density and activation remain separate assumptions.
- Reference density is a stated comparator, not an invented minimum; thresholds are uncalibrated.
- Non-identifiability is an information-limit proof; the restricted higher-density board is hypothetical.
- Accessible and healthy locations intersect rather than forming an assumed capacity ordering. Validation remains conditional on finite coverage.
- Physical excess, functional excess, cohort association and manufacturing cause require separate evidence. Neither bandwidth nor price proves all four.
