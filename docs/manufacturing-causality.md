# Manufacturing constraints and candidate predictions — v0.11.0

[日本語](manufacturing-causality.ja.md) · [Current ranking](current-ranking.md) · [Historical context](historical-context.md) · [Inference refinement](inference-refinement.md) · [Lot history](lot-history.md) · [Capacity constraints](capacity-constraints.md) · [Sources](sources.md)

**2026-11-26 JST. v0.11 connects primary supply, qualification and discontinuance records to manufacturing stages and dates. Theoretical desk review; no new hardware measurements.** This document turns the supply-substitution hypothesis into narrower predictions. **Facts** are attributed to sources; **deductions** follow from stated premises; **hypotheses** describe unverified manufacturing pathways. The similarity-led v0.9 ranks withdrawn in v0.10 are not reinstated. Historical records narrow the conditions and production groups worth comparing; differences from ordinary construction and physical-evidence statuses are evaluated separately. See the [recurrence hypotheses](recurrence-hypotheses.md) for the revision history and [historical context](historical-context.md) for the new chronology.

## 1. Identify the constraint that the substitution would relieve

"Supply was tight" does not identify which resource was scarce, which alternative was available, or which manufacturing decision could still change. A proposed substitution becomes more specific when it addresses the actual constraint.

**Fact:** On 20 July 2023, TSMC distinguished its ability to support AI demand in front-end manufacturing from tight back-end advanced-packaging capacity, particularly CoWoS [S83, PDF p.7]. This establishes a historical example of stage-specific constraints. It does not identify a GPU's memory population or a substitution program.

The following entries are **conditional model predictions**, not reports of manufacturers' actions.

| Constraint or inventory condition | Pathway that could help | Discriminating prediction to pursue | Counterexample or missing condition |
| --- | --- | --- | --- |
| The normal lower-density HBM part is scarce; a denser alternative is available | Use a qualified denser part during package manufacture while retaining the advertised capacity | A bounded part/revision group changes HBM density without changing nominal capacity; relevant component availability precedes its assembly | The denser part is also scarce, incompatible, committed elsewhere, or more valuable in another product |
| HBM broadly, including dense parts, is scarce | No special advantage for hidden high-density population follows; a particular surplus pool would need separate evidence | Search for density-specific inventory and qualification, not only corporate shortage statements | Scarcity can increase the alternative value of the very part the hypothesis proposes to leave partly unused |
| Packaging/interposer throughput is constrained | Reassign an already completed compatible package, if no repeat of the constrained operation is needed | A documented completed-package pool and a later permitted allocation/configuration decision | Denser loose HBM still needs the common packaging operation; a different work content, yield, or route must be shown before claiming it relieves that bottleneck |
| Finished high-capacity inventory loses its original outlet | Reassign, resell, or configure compatible stock for another eligible product | Original package identity persists while allocation, configuration, or sale changes after the event | Another profitable outlet, holding the stock, or ordinary resale may be preferable; an accounting charge does not identify the parts |
| A board, cooling, connector, or host-integration stage is constrained | An available completed assembly might bypass the specific missing stage | Trace which stage the substitute has already completed and which approvals remain | Changing HBM density alone does not supply the missing board or cooling component |

**Deduction:** an event supports a particular pathway only to the extent that the proposed alternative relieves its identified constraint. An event affecting another stage supplies context, not a causal link. Actual changes in cycle time, yield or work content could change this assessment; they must be evidenced rather than assumed.

This yields useful search targets. A component-specific shortage suggests part-change and qualification records. A packaging shortage suggests completed-package inventories and allocation records. A demand shock suggests disposition records and still-permitted configuration changes. These searches need different documents even when the marketed SKU is the same.

## 2. Date the decision that could still change

Separate three decisions rather than assigning one undifferentiated "manufacturing date" to a board.

| Decision | Relevant information | Temporal limit |
| --- | --- | --- |
| Physical population | HBM part selection and original package assembly; separately documented rework | A later event cannot cause the original bonded population to change without a subsequent physical operation |
| Exposure or grade | When the capacity/grade configuration is set and whether it remains changeable | A later event cannot cause an earlier irreversible restriction; it may explain a later permitted configuration choice |
| Commercial allocation | SKU assignment, destination, shipment and sale | A later allocation can change the market story without changing either physical population or earlier restrictions |

**Deduction:** the relevant boundary is the point at which the particular decision became irreversible, not merely the broad factory stage. Completed-package reassignment requires both compatibility and a configuration state that permits the intended use. If an irreversible restriction was already set before a demand shock, that shock cannot explain why it was originally set. It can still explain subsequent resale or allocation.

**Unknown:** the candidates' exact configuration procedures and lock-in times are not established here. Fuses, fixed routing and configuration controls are possible categories to investigate, not asserted implementations for every candidate. Do not assume board assembly is always a stage at which memory capacity can be freely reassigned.

**Conditional chronology predictions:**

- A density-substitution explanation requires the substitute to have been available and selected when the affected original package was assembled. Relevant qualification must cover the shipped configuration; this model does not assume that qualification completion always precedes first assembly. The public announcement date alone dates neither internal availability nor approval.
- A completed-package reassignment explanation predicts continuity of package identity and a later eligible assignment/configuration. It does not predict replacement of individual HBM stacks.
- A resale explanation can predict a later sales-date concentration without any new manufacturing cohort. A market listing date cannot distinguish it from fresh production.
- A temporary substitution might produce a bounded density variant, but inventory and shipping delays can obscure or extend the interval. A clean before/after pattern is neither guaranteed nor sufficient to identify its cause.

Firmware build, installation, package assembly, PCB manufacture, board assembly and sale dates retain separate meanings. Unknown dates stay unknown. The [lot-history protocol](lot-history.md) describes recording those distinctions.

## 3. Physical surplus, healthy surplus and configurability are different claims

**Physical surplus** means ordinary-data memory is present beyond the resolved baseline. **Healthy surplus** additionally requires functioning excluded memory and its relevant paths. **Configurability** asks whether the existing device can expose that resource. **Reliable workload use** adds operating conditions and sustained correctness. A fact about one claim does not settle the next.

**Fact:** Intel documents four physical HBM stacks in Max 1100, three enabled 16 GB stacks and one permanently disabled stack whose position varies. The disabled stack's separate density and health are not specified there; its reported 0/FF sensor values do not test memory health [S39]. The physical statement is informative even though permanent disablement weighs against easy exposure.

**Deduction:** lower-grade selection must be interpreted through its cause. The following causes are alternatives, not diagnoses of any ranked product.

| Hypothesized grading reason | What it could leave physically present | What would inform the healthy-surplus claim |
| --- | --- | --- |
| Compute, power or frequency qualification | Memory retained alongside a lower-grade compute device | Applicable, attributable evidence that the relevant HBM and paths passed testing |
| HBM cell, interface or connection failure | Physically retained but excluded regions | Failure/retirement records; this pathway can weaken the healthy-surplus expectation |
| Commercial segmentation or contract requirements | Potentially healthy resources excluded by configuration | Evidence of the segmentation plus separate evidence of memory health |
| Unknown grading reason | Any mixture of the above | The lower SKU label alone supplies no health conclusion |

**Constructive counterexample:** imagine two qualified product programs with four real stacks and three enabled. One disables a healthy stack to define a product tier; the other disables a failing path. Their published capacity and enabled width can match while their extra usable capacity differs. Thus those observations do not identify the reason for disablement. Variation in disabled position alone does not remove this ambiguity.

Neither a complete-product label nor a pre-assembly component test, if one is documented, automatically establishes the later assembled path's health. Its timing, coverage and applicability must match the claim. No actual yield distribution or healthy-surplus rate is inferred here.

## 4. Distinguish mechanisms by their predicted observations

These observations are **discriminators**, not unique signatures. More than one mechanism may produce the same observation.

| Hypothesis | Observation that would strengthen it | Important remaining alternative or limitation |
| --- | --- | --- |
| Higher-density address space is partly restricted | Identified higher-density original parts on a lower-capacity unit; compatible addressing information | Defective regions, post-sale replacement or misidentified SKU; ordinary width/bandwidth alone does not decide |
| A whole stack/path is disabled | Independent physical-population information and enabled-path information | Extra physical memory can be defective, disconnected or permanently disabled |
| A completed package is reassigned | Identified donor/recipient package relationship, chronology and permitted target configuration | Planned common parts or a normal lower product may explain the same family resemblance |
| Defect harvesting | Applicable grading/test evidence identifying the excluded path's failure | A generic failure report or absent telemetry does not identify which component failed |
| Ordinary lower-density construction | Reliable part density and count account for the advertised baseline | Other unobserved cohorts remain unknown; this unit does not require a surplus explanation |
| Metadata, reservation or accounting difference | A documented interpretation explains the reports for an unchanged physical configuration | A label difference alone does not establish the physical inventory in either direction |
| Aftermarket rework | Traceable repair/replacement history or a documented change from the original population | This may establish a later modified unit, not factory supply substitution |

The [capacity-constraint analysis](capacity-constraints.md) provides the interface and density checks; the [inference refinement](inference-refinement.md) explains why matching capacity and bandwidth can leave different physical constructions observationally equivalent.

## 5. Apply the model to the existing candidate groups

These are **bounded research predictions**. They specify useful next facts without claiming that a particular favorable lot exists.

| Candidate group | More specific prediction/question | Information gap identified in v0.8 |
| --- | --- | --- |
| MI50 16 GB / documented 32 GB sibling | Does an identified original 16 GB group use the ordinary lower-density population or a restricted higher-density population? Density-specific part and qualification records discriminate | Official 16/32 GB specifications establish normal alternatives, not higher density inside a 16 GB unit [S38,S80] |
| H100 SXM5 64 GB HBM2e | Does an identified package include more ordinary-data memory than the minimal construction explaining 64 GB? Search for actual population, not another support-list entry | The named 64/94 GB variants sharpen comparison, but do not establish extra populated stacks in the 64 GB variant [S60,S64] |
| A30 / H100 80 GB | Is a proposed additional memory site real DRAM with an identifiable density, and what excludes it? | Architecture and package appearance do not establish healthy excess; dummy, omitted and defective cases remain alternatives [S35,S39,S63] |
| A800 or other later product introduction | Was the particular package/configuration still eligible for reassignment at the proposed event date? | A later launch date does not identify donor inventory, compatibility or configuration timing |
| H20 supply watch | Which materials were reused, for which destination, and before which configuration decision? | Official reuse and charges motivate the question but do not identify hidden HBM; documented sales outside China also provide an alternative disposition [S65–S67] |
| Vega / BC-160 / A30X | Is there an identifiable compatible high-density package pathway beyond common branding, PCB or supply context? | Generic scarcity or mining use does not supply the missing part-level connection |
| CMP 100-200 | Establish the exact memory interface and package before treating bandwidth/capacity as anomalous | Existing specification uncertainty cannot count as a measured anomaly [S02,S05,S15] |
| Max 1100 reference | What, if anything, separately identifies the disabled stack's density and health? | Its documented physical extra component remains a reference, not a demonstration of healthy configurable surplus [S39] |

**v0.11 rank rule:** applicable part, qualification and manufacturing-date records can narrow a hypothesis without the project owning hardware. A shared generation, package family or generic shortage does not by itself raise a rank. State which candidate-specific relationship the new record changes and how it distinguishes the proposed construction from the simplest ordinary one. If it cannot discriminate, retain the conditional research hypothesis and its unranked status. Keep physical, healthy-excess and access statuses separate; do not convert unresolved-premise counts into recovery probabilities. The [current ranking](current-ranking.md) records the current treatment, while old ranks remain historical.

## 6. Count observations, not URLs

**Inference rule:** evidence independence depends on origin and claim, not the number of publications.

- Two board briefs repeating the same specification strengthen its documentation trail; they are not two independent observations of hidden population.
- A press release, an earnings transcript repeating that release, and several news reports may share one underlying event. Keep the event and its corroborating references together.
- Two reports about the same physical board remain one device observation. Different boards from one donor inventory may share a relevant production or repair history.
- A source can independently establish that a SKU exists while adding no independent information about surplus HBM.
- A claim copied from this repository and cited back to it is not independent corroboration. Market attention following publication is not technical validation.

Record the original source/event or device identifier, the exact claim it supports, and known dependencies. Unknown dependence remains unknown; it is not permission to multiply evidential weight. Independent reproduction of a physical observation and independent confirmation of a press announcement answer different questions.

## 7. H/T/D/C/U for the next desk review

This is a documentary decision framework, not a hardware gate before publishing a hypothesis. Unresolved hypotheses remain useful when their distinguishing conditions are explicit.

| Item | Desk-review rule |
| --- | --- |
| **H — hypothesis** | Name the exact SKU/part/revision scope, proposed physical excess and manufacturing pathway. State the event date or bounded interval, the relevant decision, and whether its timing is known. Do not invent a favorable cohort. |
| **T — minimum check** | One attributable original document may settle a narrow part or timing premise; there is no universal sufficient source count. Seek its necessary definitions, inspect contradictory evidence, then stop when that premise is settled or the evidence is unavailable. This is not a prevalence sample. |
| **D — decision** | **PASS, named premise only:** evidence establishes the specific part, timing or compatibility claim. **FAIL, named construction only:** a reliable contradiction breaks a necessary condition. **UNCERTAIN:** alternatives remain indistinguishable. Physical, health, configurability and supply-cause conclusions receive separate labels. Temporal coincidence alone does not pass a supply-cause claim. |
| **C — competing explanations** | Normal density, planned product segmentation, defective paths, fixed disablement, a different SKU, post-sale rework, ordinary resale, metadata/reservation, or unrelated revision changes. |
| **U — uncertainty** | Record part identification, date interpretation, missing configuration history, qualification scope, repair provenance and source dependence qualitatively. These are structural gaps, not supplied measurement-error distributions. No combined numerical uncertainty or coverage factor is fabricated. |

**A useful next question:** which missing documented fact would distinguish the investigated candidate's proposed construction from its simplest ordinary explanation? Answering that question narrows the research without requiring the project to own hardware.

## 8. Cross-disciplinary use and ERROR CHECK

**Computer architecture** identifies which resources can share an interface while differing in capacity. **Packaging and reliability engineering** separate original population, rework and grading causes. **Industrial economics** asks whether a substitution relieves the scarce stage and beats the best alternative use; the conditional cost model is in [lot history](lot-history.md). **Causal inference** checks chronology, shared evidence and competing explanations. The same framework applies to disabled CPU resources or storage-device variants, with their own physical and configuration assumptions.

### ERROR CHECK

- No new hardware result, favorable production interval, confirmed substitution or success probability is asserted.
- The TSMC statement establishes stage-specific supply context, not a GPU population fact.
- Model predictions remain conditional on compatibility, availability and decision timing.
- Physical presence, health, configurability and reliable use remain separate.
- Old ranks are historical. v0.11 does not reinstate the similarity-led ranks withdrawn in v0.10 or confuse narrower historical pathways with new population evidence.
- No new mathematical model or numeric uncertainty is introduced; the existing economic model retains its own assumptions and units.

## 9. Read historical constraints by manufacturing stage and customer

The following published facts narrow possible substitution pathways. Applying them to another customer, product or period requires a separate documented connection.

| Published event | Meaning and scope for a manufacturing hypothesis |
| --- | --- |
| **2020-02-04:** Samsung introduced 16 GB-per-stack Flashbolt with a plan to continue supplying 8 GB Aquabolt while expanding the new offering [S92] | A denser introduction does not establish disappearance of the older density. The statement does not establish sufficient volume or delivery timing for a particular customer |
| **2022-06-08:** SK hynix announced HBM3 mass production and completion of NVIDIA's sample performance evaluation, with supply for NVIDIA systems expected to start shipping in Q3 of that year [S106] | This distinguishes a standards-level candidate from a part evaluated by the target customer. The announcement does not give the exact evaluation-completion date or establish qualification for a different SKU |
| **2023-07-20:** TSMC distinguished adequate AI front-end support from tight back-end capacity, particularly CoWoS [S83] | Completed-package reassignment could bypass a constrained stage; choosing denser loose HBM alone does not eliminate assembly. This record cannot retrospectively establish the constraint affecting CMP in 2021 |
| **2023-09-30 / 2024-09-30:** Intel/Altera announced discontinuance of 16 GB / 8H Stratix 10 products and then 8 GB / 4H products because their vendor was ending HBM2 supply [S107,S108] | **16 GB / 8 GB are each FPGA product's total memory capacities, not per-stack capacities.** The first notice covers MX/NX; the second covers MX/NX and the DX 2100 product line. Both offer last-time orders and state that no replacement devices are available. Their order does not establish the discontinuance sequence for the whole HBM market |

**Deduction:** do not assume that lower densities necessarily disappear first and force substitution with higher densities. In the cited customer-specific example, the 16 GB notice preceded the 8 GB notice; last-time orders and product discontinuance were actual responses to supply withdrawal [S107,S108]. A **conditional hypothesis** remains for reassigning an already assembled package that is compatible with the intended use and permits the required configuration: it may be usable without repeating the constrained stage. Separate loose-HBM substitution, completed-package reassignment and ordinary resale, and identify which constraint each route would relieve.

See [historical context](historical-context.md) for candidate-specific chronology and competing explanations of price changes. These events alone do not establish a particular GPU's hidden capacity or its recovery rank.
