# Refining the predictions without hardware — v0.7.0

**Continuation:** [v0.8 capacity constraints](capacity-constraints.md) prove conditional bounds and distinguish inactive channels from restricted address depth; [manufacturing causality](manufacturing-causality.md) connects supply context to the decision it could actually change. This v0.7 discussion remains background.
[日本語](inference-refinement.ja.md) · [Current ranking](current-ranking.md) · [Physical theory](theory.md) · [Sources](sources.md)

**2026-11-26. Desk research; no new hardware measurements.** The task is to narrow explicit hypotheses about surplus HBM. This document separates sourced facts, deductions and hypothetical constructions. It does not assign success probabilities. The existing [theory](theory.md) supplies the equations, variable definitions and unit checks.

## 1. Predict a particular claim

Four questions need separate answers: is additional ordinary-data memory physically present; is any of it functional; can the configuration expose it; and can a workload use it reliably? Dedicated parity and repair spares are outside the ordinary-data claim. Evidence for one question does not automatically answer the others.

**Deduction:** a published specification can establish the advertised baseline while leaving surplus memory entirely unresolved. A larger memory report alone cannot establish additional distinct, resident, functioning HBM. Reservations, aliases, host memory and metadata discrepancies remain competing explanations. Conversely, a stock report matching the nominal capacity does not prove physical absence.

The [current ranking](current-ranking.md) therefore identifies the prediction, its ordinary alternative and the missing fact that would change the assessment. Research priority is not a recovery-success ranking. A documented disabled component can be an informative reference while providing weak prospects of usable extra capacity.

## 2. Two different mechanisms deserve different searches

| Mechanism | What could be restricted | Useful distinguishing evidence | Main unresolved point |
| --- | --- | --- | --- |
| Density / address subspace | Some storage behind otherwise active channels | Identified high-density parts on a lower-capacity variant; applicable addressing documentation | Actual population, mapping, health and exposure method |
| Whole channel / stack | An entire memory path or stack | Direct physical-population statement, part identification and enabled-path evidence | Whether the unused component is healthy and reachable |

**Fact:** Micron's HBM2E brief describes four-high and eight-high configurations with the same channel count and bandwidth. The eight-high design doubles per-channel capacity. Table 3 describes an additional SID, or stack-ID, bit selecting between bank sets associated with the lower and upper memory dies [S01].

**Hypothesis:** a controller/configuration exposing only one such storage subset could make a higher-density assembly look smaller without reducing external width. This is a concrete addressing model, not evidence that any ranked GPU masks SID. It establishes neither an accessible firmware switch nor compatibility with a particular GPU package. The Micron example is not a universal description of every HBM generation.

**Fact:** Intel documents four physical HBM stacks in Max 1100, three enabled 16 GB stacks and one permanently disabled stack whose position varies by card [S39]. The disabled stack's separate density and health are not established there. Its telemetry can return 0 or FF; such values are not an independent measurement of absence. Permanent disablement is contrary evidence for easy exposure.

**Deduction:** a high bandwidth-to-capacity ratio can suggest an address-subspace question. An ordinary ratio cannot exclude a physically installed but disabled stack. Neither pattern alone establishes functional surplus.

## 3. A constructive limit on specification-based inference

Consider these **hypothetical**, qualified boards under the same capacity convention, active data-lane count and effective lane rate. All capacities below are nominal comparison classes, not measured byte counts.

| Construction | Physically installed ordinary capacity | Exposed capacity | External width and theoretical peak |
| --- | --- | --- | --- |
| A: four 8 GB stacks, fully exposed | 32 GB class | 32 GB class | Four full HBM2E data interfaces |
| B: four 16 GB stacks, half of each exposed | 64 GB class | 32 GB class | The same four interfaces at the same rate |

Micron's density/interface example makes the premises internally consistent at the component level [S01]. Board B additionally assumes compatible addressing and restricted exposure. Adding the same lane rates produces the same theoretical bandwidth on both boards. Both report the same exposed capacity, yet only B contains physical surplus. Therefore these observations do not uniquely identify the construction. This does **not** prove B was manufactured or that its unexposed cells work.

The same ambiguity occurs between three installed-and-active stacks and four installed stacks with one disabled. Intel establishes that the latter general mechanism exists [S39]; it does not establish another product's population.

**Application:** official support documents identify H100 SXM5 64 GB and 94 GB HBM2e variants [S60,S64]. That is a useful comparison lead. Four 16 GB stacks already explain 64 GB ordinarily, however. A verified fifth or sixth memory stack would change the physical question; another support-list mention would mainly strengthen SKU identification.

## 4. Match the supply explanation to the manufacturing stage

| Proposed pathway | Required connection | What the historical event alone cannot establish |
| --- | --- | --- |
| Substitute a denser HBM part during packaging | Relevant availability and qualification before that package is assembled | A later shortage changed an already bonded stack |
| Reassign a completed GPU/HBM package to another SKU | Identified compatible package and a later allocation/configuration decision | Individual HBM stacks were exchanged |
| Resell or refurbish an existing board | Traceable original identity and subsequent changes | An original manufacturer changed its production BOM |

These are distinct hypotheses. Post-package events can motivate reassignment or rework, but cannot retroactively cause the package's original component selection. Firmware build, package manufacture, board assembly and sale dates must retain their own meanings. Unknown dates stay unknown.

**Fact:** NVIDIA's H20 commentary reports inventory/purchase-obligation charges and reuse of certain materials [S65]. It does not identify those materials as HBM or specify the destination SKU. **Deduction:** this strengthens the reason to look for allocation records; it does not establish high-density HBM in a lower-capacity product.

An available high-capacity assembly also has alternative uses and qualification costs. Scarcity of the high-density part can weaken the proposed substitution route. The [economic model](lot-history.md) states the necessary conditional comparison; company-wide shortages do not supply its missing product-level inputs.

## 5. Resolve ordinary explanations before promoting a lead

A difference between official capacity tables is initially a documentation question. For example, the current MIG supported-GPU table lists B300 at 288 GB and B200 at 180 GB [S79], whereas the earlier supported-hardware list includes a 270 GB HGX B300 configuration [S64]. Exact SKU, document revision and capacity-accounting conventions need resolution before interpreting this as surplus on one physical unit. Neither ECC nor a hidden-memory mechanism is established by the discrepancy alone.

A shared die family, PCB or package outline is similarly weaker than identified memory population. Additional corroboration of a product's existence should not be counted again as corroboration of its hidden capacity. Several reposts of one observation remain one observation.

## 6. Publicity changes the market being observed

**Causal possibility:** publishing a candidate ranking can increase attention and exploratory purchases, which can influence asking prices. A subsequent rise could therefore reflect this project rather than an independent discovery of extra memory.

Record repository-release and X-post times alongside market observations. Distinguish observations before publication, after publication and with unknown timing. Posts or seller descriptions repeating this repository are not independent technical corroboration. Later prices remain useful market data, but cannot by themselves validate the hypothesis that helped generate the attention. No validated price-based ranking adjustment is made here.

Track the original observation behind every claimed result. A claim leaving this repository and returning through another article gains no independent evidential weight merely by changing its URL.

## 7. Ask for the next discriminating fact

An unrestricted claim that “some unknown lot contains surplus” cannot be refuted by a finite collection of negative boards. Make the next question narrower: does this identified unit contain the specific proposed density or additional stack? A negative result can reject that construction for that unit without proving absence throughout an entire product family. A positive unit establishes existence in that scope, not market prevalence.

| Item | Compact decision for an optional source or owner contribution |
| --- | --- |
| **H — hypothesis** | State one construction and the named SKU/PN/revision or unit, the relevant date or documented interval, and its proposed physical excess. Do not invent a cohort. |
| **T — minimum check** | One attributable original source or one identified unit can settle a case-specific premise. Seek the part/population fact that distinguishes the constructions; stop when that narrow question is answered or the needed evidence is unavailable. This is not a prevalence sample. |
| **D — decision** | **PASS for the physical premise:** identified ordinary-data population exceeds the resolved baseline. **FAIL for the named construction:** reliable part/population evidence contradicts a necessary assumption. **UNCERTAIN:** evidence cannot distinguish alternatives. These labels do not assign a functional-capacity PASS. |
| **C — competing explanations** | Ordinary lower density, fewer populated stacks, permanent disablement, defective paths, changed metadata, rework, reservation or a different SKU. |
| **U — uncertainty** | Part identification, source independence, dates, units, repair history and incomplete topology. No combined numerical uncertainty or coverage factor is invented for these structural gaps. |

Functional claims additionally require stated hardware/configuration, operating conditions, distinct resident coverage, error criteria and observation duration under the [validation protocol](validation.md). A display change or failed initialization alone settles neither health nor physical absence. Source corrections and ordinary configurations are useful contributions; modification is not a prerequisite.

## 8. Disciplines and checks

**Computer architecture** supplies address/interface models; **packaging and reliability** distinguish real population from failed or inactive components; **industrial economics** evaluates feasible substitution at the relevant production stage; **statistics and causal inference** separate independent observations, publication feedback and population claims. Together they identify which missing fact is valuable without pretending that missing hardware evidence already exists.

### ERROR CHECK

- No new measurements, capacity recoveries, favorable lots or numerical success probabilities are claimed.
- SID is an addressing example, not an asserted GPU firmware control.
- Physical population, functionality, exposure and workload usability remain separate.
- Capacity classes in the constructed example are hypothetical; exact bytes require a resolved convention.
- Negative evidence applies to its stated scope; prices and repeated claims are not independent technical proof.
