# Study design: separate four claims before collecting results

[Home](../README.md) · [Physical theory](theory.md) · [Lot history](lot-history.md) · [Validation](validation.md) · [Sources](sources.md)

**Status: proposed protocol, not a completed experiment.** This document turns the research idea into bounded questions that owners and reviewers can answer. The observation register contains no measurements made by this project.

The main project deliverable is the [explicitly speculative ranking](candidates.md). This study protocol supports future empirical work; it is not a prerequisite for publishing a reasoned prediction from public information.

## 1. Four claims, four evidence requirements

| Claim | What is being tested | Evidence that can support it | What it does not establish |
| --- | --- | --- | --- |
| **H-P: physical excess** | An identified unit contains more user-data DRAM capacity than the specified baseline. | Verified memory part identity/density and populated topology, with dedicated parity cells and spares excluded from the user-data comparison. | That the additional cells work, are reachable, or can be used by an application. |
| **H-F: functional excess** | The identified unit demonstrates additional distinct, resident device-memory bytes under stated conditions. | Reviewed address-sensitive write/read coverage, independence and residency controls, exact units, errors and repeatability. | Lifetime reliability, every address/pattern, the rest of the SKU, or the reason the capacity was restricted. |
| **H-L: cohort difference** | The specified physical variants or functional results differ between predeclared manufacturing cohorts. | Reliable production-date provenance, individual observations, comparable methods, and acquisition/repair history. | A population prevalence estimate from volunteer samples or a supply-related cause. |
| **H-S: supply mechanism** | A stated component shortage or inventory condition caused the specified substitution. | Attributable evidence linking the affected part/assembly, production change, date and reason; evaluate contradictory evidence. | That additional memory in every affected unit is healthy or recoverable. |

These are related claims, not one automatic evidence ladder. A valid functional result can establish a lower bound on physical device storage without identifying every stack. A part-identification result can support H-P while H-F remains uncertain. A causal production-change document can support H-S without any successful capacity test.

**Addressable and healthy are different properties.** Faulty memory can still be addressable. Driver-reported total, virtual address-space size, physically populated user-data capacity, tested distinct resident bytes, and workload usability must therefore remain separate fields. CUDA distinguishes device allocations from managed and mapped host allocations; the API choice and residency evidence must be recorded, not inferred from the pointer size alone [NVIDIA CUDA memory API](https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/group__CUDART__MEMORY.html). Driver memory accounting and error/page-retirement fields are described separately in the [NVIDIA System Management Interface documentation](https://docs.nvidia.com/deploy/nvidia-smi/index.html).

## 2. Freeze a study record before interpreting new results

Create a dated issue or document containing the following fields. An amendment must retain the old version and explain the reason. Existing published findings may guide an exploratory study, but cannot become an independent prediction after the fact.

| Field | Required content |
| --- | --- |
| Target | Product, PCI/subsystem identifiers, board PN/revision, allowed package/part groups, and explicit exclusions. Product name alone is insufficient. |
| Manufacturing window | Inclusive start/end bounds, manufacturing stage, date-code source and allowed precision. If dates are unknown, study revision/part groups and leave time dependence untested. |
| Primary claim | Select H-P, H-F, H-L or H-S; state which other claims remain outside the conclusion. |
| Baseline | Exact advertised ordinary-data capacity and source after resolving the label's byte convention; do not substitute free memory or a runtime total reduced by reservations. Record those observations separately. A rounded GB label is not an exact threshold. |
| Material difference | Minimum additional byte count or specified change in part density/topology. Choose it from the research question before inspecting outcomes. |
| Environment | Actual device, stock/modified status, OS/kernel, driver/runtime/test version, allocation backend, virtualization/MIG state, ECC, clocks, power, temperature and restart state. |
| Coverage and duration | Declared address coverage, patterns/seeds, complete passes, elapsed test time, restart repetitions and acceptable error behavior. Record actual values even if a report does not meet the plan. |
| Collection plan | Recruitment channels, inclusion order, minimum coverage target, maximum number of devices, closing date, dependency checks and stopping rules. |
| Alternatives | At least ordinary low-density parts, defects, aliases/host storage, reservations, revision/OEM differences, repair and source/date errors. |
| Decision plan | Per-claim PASS/FAIL/UNCERTAIN rules and the scope of every verdict. Keep unknown and failed observations in the denominator/report. |

“Some unknown lot somewhere contains extra memory” is an exploratory possibility, not a finitely falsifiable survey claim. A useful bounded claim is: **“In the predeclared set of documented revisions and production windows, this protocol will identify at least one unit exceeding the stated baseline by the stated amount.”** Its result applies to the collected set and collection window. Zero positives in a volunteer sample do not rule out every unsampled unit in that cohort. A claim about all units or a population rate needs a representative sampling design and its own statistical analysis.

## 3. Functional decision rule and units

This rule classifies an observed experiment. It does not prescribe device modification or establish long-term reliability.

| Symbol | Meaning | Unit | Definition / assumptions | Domain / type |
| --- | --- | --- | --- | --- |
| $C_0$ | Advertised ordinary-data capacity in exact bytes | byte (information unit, not an SI base unit) | Exact predeclared nominal baseline after resolving the label's byte convention; excludes dedicated parity/spares; neither transient free memory nor a runtime total reduced by reservations | Positive integer, scalar |
| $\Delta_{\min}$ | Minimum additional capacity required by this study | byte | Positive threshold chosen before outcome inspection; not a universal physical constant | Positive integer, scalar |
| $C_v$ | Verified distinct resident device bytes | byte | Reviewed coverage of simultaneously retained, independently distinguished data on this GPU, under the declared test conditions; excludes host fallback, aliases, untested and reserved ranges | Nonnegative integer, scalar |
| $M$ | Observed data mismatches in the complete declared test | 1 (count) | Includes failures in any declared region or pass; do not discard a failing region and call the remaining test a pass | Nonnegative integer, scalar |
| $G$ | Evidence and protocol gate | 1 | True only when baseline comparability, independence, device residency, coverage records, required repetitions and predeclared error criteria are all substantiated | Boolean, scalar; missing evidence cannot make it true |
| $n_{\min}$ | Minimum devices for a replication claim | 1 (device count) | This project's initial replication target is two independently tested physical devices; dependency/provenance must still be assessed | Positive integer, scalar |

The functional observation qualifies for PASS only when

$$
G = \mathrm{true},\qquad C_v \ge C_0 + \Delta_{\min},\qquad M = 0.
$$

Derivation: the baseline and minimum material increase are first added on the same exact byte basis. The reviewed count must reach that total. Counting distinct, simultaneously retained data prevents reusing the same cells from satisfying the increase; a reviewed device-residency condition excludes storage elsewhere. The mismatch and evidence gates then restrict the conclusion to a successfully checked experiment. This is an operational acceptance definition, not a proof that finite testing exhausts all possible faults.

**Unit check:** both sides of the capacity comparison have units of byte. Mismatch and device counts are dimensionless; they are not added to capacities.

**Illustrative planning example, not measured results:** choose a baseline of 6 GiB (6,442,450,944 bytes), an additional-capacity threshold of 1 GiB (1,073,741,824 bytes), and require at least 7 GiB (7,516,192,768 bytes) of qualifying coverage. A report checking 11 GiB can meet the byte-count condition; a screenshot showing 12 GiB cannot meet the evidence gate. A report checking only 5 GiB cannot establish the declared increase, even if its allocation API reported more. GiB here means 1,073,741,824 bytes; vendor “GB” labels must be resolved independently.

The study record could additionally require three complete pattern passes and repetition after two cold starts, with a specified elapsed-time target and error policy. Those are **illustrative engineering choices**, not statistically validated universal thresholds. Reviewers must use the frozen study's actual requirements. Corrected ECC events, missing telemetry and unavailable cold-start evidence need an explicit treatment; absence of a reported counter is not evidence of zero events.

## 4. PASS, FAIL and UNCERTAIN are claim-specific

| Claim | PASS | FAIL within the stated scope | UNCERTAIN |
| --- | --- | --- | --- |
| H-P | Reliable part/topology evidence establishes the declared excess on this unit. | Reliable complete topology/part evidence establishes insufficient user-data capacity for the declared excess on this unit. | Ambiguous markings, unknown density, inaccessible sites or inferred stack counts from bandwidth. |
| H-F | The functional rule above is met for the declared coverage, duration and environment. | A reviewed, reproducible data failure defeats the specified experiment under its declared conditions; or a substantiated physical upper bound makes its required capacity impossible. State which reason applies. | Enumeration only; missing residency/alias controls; incomplete coverage; failed initialization/allocation with unresolved cause; missing baseline or unreviewable logs. |
| H-L | For a **descriptive sampled-set claim**, verified cohort membership and comparable observations demonstrate the predeclared difference in the collected devices. Report the full cross-tabulation. | Complete adequate observations contradict the predeclared difference **in the collected set**. | Missing dates, incomplete groups, inconsistent methods, overlapping date ranges or dependence that prevents the proposed comparison. Population association remains unestablished without an adequate sampling and statistical design. |
| H-S | Attributable, sufficiently specific evidence links this substitution to the proposed supply condition. | Credible direct evidence rules out that particular proposed mechanism for the stated change. | General shortages, price movements, timing alone, no public PCN, or lack of a causal record. |

A functional FAIL is not proof that the extra DRAM is absent, that another configuration cannot work, or that all units fail. A physical PASS is not a functional PASS. “No qualifying positive observed before the closing date” is an honest survey outcome; it is not automatically a physical FAIL for untested boards.

## 5. Minimum collection and sequential stopping

Start with read-only inventory and existing owner evidence. For an exploratory temporal comparison, the initial target is **six documented devices: two owners in each of three predeclared early/transition/late cohorts**, preferably through different acquisition channels. If reliable dates cannot be established, use documented revision/part groups instead and report that the temporal question is unanswered. This is a coverage target, not a sample-size calculation or a guarantee of statistical power.

For replication of an H-F result, the initial minimum is **two independently tested physical units of the relevant variant**. Two owners may have bought cards from one donor lot, copied one method's error, or relied on the same source. Record such dependencies. Multiple tests on one device are repeated measurements, not additional devices. Replication can strengthen a bounded existence claim; it does not estimate how frequently a random buyer would receive that variant.

Predeclare a collection closing date, maximum device count and minimum evidence coverage. Stop an individual experiment when its declared operational/error limit is reached and retain that outcome. A first success may be published as a unit result while the agreed collection continues. Do not stop the comparative study just because a favorable result appears, silently extend it until success, or remove difficult units. If resource limits end collection before the target, report the shortfall and leave the affected comparison uncertain. Any later cohort or revised threshold begins an explicitly labeled exploratory extension.

## 6. H / T / D / C / U record

| Element | Required report |
| --- | --- |
| **H — hypothesis** | One of H-P/H-F/H-L/H-S, exact variant/cohort, declared effect threshold, environment and time window. |
| **T — minimum test** | Sources and data, physical units and owner/dependency counts, evidence gate, coverage/repetitions, collection limit and sequential stopping rule. |
| **D — decision** | Claim-specific PASS/FAIL/UNCERTAIN, exact supported byte count or part difference, and the units/conditions to which it applies. |
| **C — competing explanation** | Low-density parts; defective memory; addressing aliases or other storage; ECC/reservations; different OEM/revision; repair; source/date ambiguity; selection or shared-origin bias. State which controls addressed each relevant alternative. |
| **U — uncertainty** | Missing coverage, identification and residency confidence, date intervals, measurement conditions, dependent observations and selection effects. Distinguish uncertainty of a measurement from uncertainty of an explanation. |

Exact byte arithmetic does not make uncertain topology, host residency or cohort assignment exact. Do not invent a combined standard uncertainty or coverage factor from these categorical unknowns. If a separate bandwidth or temperature measurement has calibrated errors and repeatability/correlation data, report its uncertainty model and coverage factor with that measurement; otherwise mark them not estimated. A conventional coverage factor cannot compensate for unknown bias or an unidentified component.

## ERROR CHECK

- Installed, addressable, healthy and verified memory are not treated as one ordered scalar sequence.
- A finite successful test supports its checked bytes and conditions; it does not prove permanent fault freedom.
- Minimum counts are exploration/replication gates, not a success probability or prevalence estimate.
- Cohort association and supply causation have independent evidence requirements.
- Negative and unknown observations remain part of the report; unsampled lots are not declared disproved.
- No hardware measurements, population statistics or manufacturer motives have been generated by this protocol.
