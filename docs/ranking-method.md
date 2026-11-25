# How the hypothesis ranking is made

> **Historical analysis. Use the [v0.7 current ranking](current-ranking.md) for the current tiers and categories. Earlier ordinals are retained as the judgment of that release.**

> Historical NVIDIA-only v0.4.0 snapshot. For the expanded current investigation order, see [cross-vendor ranking](cross-vendor-ranking.md). The earlier five predictions are preserved for comparison; Intel's documented physical surplus is a distinct evidence class.

[Home](../README.md) · [Candidate ranking](candidates.md) · [Physical theory](theory.md) · [Manufacturing context](lot-history.md) · [Sources](sources.md)

**v0.4.0 / 2026-11-25. This is an explicit desk-research prediction.** The project uses public specifications, first-person reports, product history and physical reasoning to rank hypotheses. Owning or testing a GPU is not a prerequisite for contributing a reasoned prediction.

## 1. What the main rank predicts

The ranked hypothesis is: **at least some stock units of the named variant already contain ordinary-data HBM beyond the advertised capacity, with some of that additional capacity remaining functional but unexposed.** Dedicated parity and spare cells are excluded from ordinary-data capacity.

This combines physical presence with latent functionality. A larger assembly whose entire extra region is defective would satisfy a narrower physical-presence claim, but would not satisfy the complete ranked hypothesis. Whether software can expose the extra region, whether a complete workload can use it reliably, and whether a modification is economical are separate unknowns. A rank does not attach value to unusable memory.

The scope is variant-dependent existence, not the fraction of all units sold under a product name. Predictions identify relevant revisions or production conditions when sources support them. They do not imply that an unspecified buyer will receive a suitable unit.

## 2. Rank, confidence and capacity are separate

| Field | Meaning | What it does not mean |
| --- | --- | --- |
| Prediction rank | Relative order in which this release suspects the stated latent-capacity hypothesis | A measured success probability or an order of purchasing value |
| Confidence in the hypothesis | Strength and specificity of the available support for actual extra functional memory | Certainty merely because specifications are well documented |
| Evidence status | Whether a particular premise comes from a vendor specification, an owner's direct observation, a community summary, or an explicit assumption | A quality label automatically transferred to the whole conclusion |
| Conditional capacity scenario | Total physical ordinary-data capacity of a hypothetical assembly with the stated density and population; its healthy and accessible portions remain separate unknowns | An estimate of actual installed, healthy or recoverable bytes, or an expectation or ceiling |
| Rank sensitivity | Which new fact or different judgment would change the order | An excuse to retain the same claim after contradictory evidence |

**All five currently ranked candidates have low confidence in actual latent extra functional capacity.** A candidate can be first among weak predictions. The external CMP 170HX and CMP 100-100 reports are controls and historical precedents, not new predictions from this ranking [S03,S04a,S16].

The current order is CMP 100-200, A30, PG199 / DRIVE A100, CMP 100-210, and A30X. The [candidate cards](candidates.md) contain the actual forecasts, assumptions and counterarguments. A30 and PG199 occupy the same weak tier; their second/third ordering is particularly sensitive to judgment and missing package evidence.

## 3. Compare explanations instead of adding arbitrary points

Each candidate receives a written comparison along these dimensions. We do not add them into a numerical score because neither the weights nor the relationship to real outcomes has been calibrated.

| Dimension | What strengthens the prediction | What weakens it or remains unresolved |
| --- | --- | --- |
| Candidate-specific clue | A sourced mismatch between the nominal capacity and actual part/topology information; a specific documented variant difference | Only a shared GPU die name, similar package outline, or a large bandwidth number |
| Concrete production/configuration pathway | A relevant capacity-restriction precedent, identified package commonality, or a specific component transition that could leave extra functional memory | A generic claim that every manufacturer may segment products or reuse stock |
| Ordinary explanation | The proposed extra-capacity construction explains a fact that a normal assembly explains poorly | Known lower-density parts, fewer active channels, or an ordinary SKU already explain the specification |
| Assumption burden | The forecast follows after a small number of explicit, physically compatible assumptions | It requires unverified width, stack count, density, compatibility and health simultaneously |
| Contrary observations | Identified observations leave the proposed mechanism open | Direct low-density identification, absent population, or well-scoped evidence that additional regions are defective |

Source quality controls how much weight a premise deserves. Ten pages repeating one owner's report remain one underlying observation. An official specification can establish the advertised configuration while leaving physical surplus and health completely unknown. A single failed initialization is weak evidence about presence; a well-identified low-density assembly is much stronger evidence against an extra-density scenario.

Missing information is not treated as a zero-capacity measurement. It limits confidence and makes the prediction conditional. A candidate may therefore remain high in the relative order even though a decisive specification is missing, but the card must state that dependency prominently.

## 4. Why this particular order is a prediction

**CMP 100-200 is first** because the roughly 6 GB-class mining configuration, its Volta identity, and the related CMP capacity-restriction precedents form a more specific conjunction than a generic high-capacity product sibling [S02,S04a,S05]. This remains an analogy. The cited stock log does not establish memory width or density, and 12 GB is a conditional scenario, not a measured baseline hidden underneath it. TITAN V establishes that a 12 GB Volta configuration existed [S32]; it does not establish a shared physical package. The historical existence of two-die HBM2 designs also prevents an assumed universal 4 GB stack minimum from proving excess memory [S36].

**A30 is second and PG199 third** because this release gives slightly more weight to the concrete low-capacity GA100 derivative pathway around A30 and its documented specification. The A30 capacity-to-width relationship is ordinary, and restoring compute blocks on one A30 does not establish extra memory [S06,S34]. PG199's OEM lineage motivates a package/configuration hypothesis but does not identify the extra density [S12]. The relative preference is a weak editorial judgment; it is not a measured difference in prevalence or manufacturer economics.

**CMP 100-210 is fourth** because mining specialization and variant differences provide a mechanism to consider, while a normal 16 GB Volta assembly explains the nominal capacity. First-person sources distinguish hardware families and compute/link results from broader conversion claims [S04,S33]. These performance results are not memory-capacity observations.

**A30X is fifth** because its high bandwidth and 24 GB capacity admit an ordinary lower-density explanation. The cited vendor sheet does not establish its effective bus width [S10]. The community negative report remains a source-tracing lead whose primary record, method and scope were not obtained [S11]; it is not used to determine this rank or as a verdict on every A30X.

Detailed scenarios belong in the candidate cards. These paragraphs explain the comparative judgment and do not replace their contrary evidence.

### Why not rank A100 40 GB equally with A30?

The shared GA100 family alone cannot justify such a difference. NVIDIA describes the A100 40 GB configuration using five active stacks, while describing a fuller GA100 design separately [S35]. That gives an ordinary explanation of its marketed configuration; it does not prove an absent or defective sixth site. An A100 with additional functional memory remains a permissible watchlist hypothesis.

This release places A30 ahead because it tentatively favors a broader package-reuse pathway for the lower-capacity derivative. **No source here establishes that reuse occurred, was cheaper, or was more prevalent on A30.** If one declines that extra manufacturing assumption, A30's advantage over ordinary A100 variants narrows substantially. We expose that dependence instead of presenting the order as uniquely determined by the specifications.

## 5. Sensitivity and conditions for changing the rank

| New information or different criterion | Consequence |
| --- | --- |
| Require direct proof of extra functional memory before ranking | None of the five qualifies as an established positive. Keep the external controls separately; this project's predictive ranking would serve a different question. |
| PG199 has independently identified higher-density population beyond its baseline | Its physical premise strengthens and it can move above A30; health remains an additional question. |
| A30 is identified as an ordinary assembly with no extra population in a specified cohort | Lower that cohort's prediction; do not silently move the claim to an unnamed lot. Other separately identified cohorts remain untested. |
| CMP 100-200 is identified as a normal low-density assembly matching the baseline | Its main analogy weakens sharply; revise the first-place forecast for that identified variant. |
| A failed memory-exposure attempt has no reliable topology or test coverage | Lower expectations for that tested method if appropriate; do not infer that the memory is physically absent. |
| Additional installed regions are demonstrably defective under the defined conditions | Physical presence can remain supported while the ranked latent-functional-capacity hypothesis weakens. |
| A new source simply repeats an existing story | No independent evidential promotion. |
| Only maximum conditional capacity is prioritized | This becomes a different ranking. A 64 GB scenario may move above a 12 GB scenario without becoming more credible. |

Each ranking revision should name the changed premise and its effect on the preferred explanation. A reversal is a useful research result. The earlier prediction remains in version history so that hindsight does not masquerade as prior foresight.

## 6. Manufacturing dates and prices

Manufacturing context helps explain **when a particular pathway could operate**. An available, qualified higher-density part or completed package might be substituted when its opportunity cost plus conversion and risk costs are favorable relative to ordinary procurement and delay. The [lot-history model](lot-history.md) sets out those conditions. Corporate shortages and long commitments are documented [S21,S22,S29]; candidate-specific HBM substitution is not.

A common shortage period cannot by itself distinguish two candidates exposed to that same period. A ranking adjustment needs a more specific connection: identified package compatibility, a dated part change, an applicable OEM revision, or another candidate-level observation. Part manufacture, package assembly, PCB manufacture, final assembly and sale dates remain distinct. Lack of date evidence permits a lot hypothesis but does not establish its timing.

**Price-based adjustment in this release: none.** The [market register](market.md) does not contain a sufficient comparable transaction series. An asking-price snapshot, a sold counter and a disappearing listing cannot establish a selective purchase wave. Later revision-specific price evidence may strengthen the case for a hypothesis, but must still be compared with condition, accessories, integration support, performance changes, general demand and repeated listings.

## 7. Role of theory, data and optional owner reports

The primary output is a readable forecast: what is suspected, why, under which assumptions, and why it might be wrong. [Physical theory](theory.md) supports or rules out deductions; it cannot manufacture missing part identities. The offline screening tool reports nominal geometry ratios, not this ranking and not a recovery probability. In particular, its comparator and heuristic flag do not replace the comparative reasoning above.

The candidate/specification register and the prediction should remain distinct. Unknown factual fields stay empty. Conditional scenarios belong in hypothesis fields and prose. A manufacturer source attached to a row does not turn that row's forecast into a manufacturer claim.

Hardware owners may contribute observations that improve later editions. The [study design](study-design.md) and [validation protocol](validation.md) are supporting references for that purpose. A desk-research contributor can instead identify a source, challenge an assumption, construct a normal explanation or argue for a different rank. No experiment is required to make the current hypotheses explicit and useful.

## ERROR CHECK

- The ranked claim requires some latent functional extra capacity; defective surplus alone is insufficient.
- Software exposure, workload reliability, prevalence and commercial value are separate questions.
- No calibrated probabilities, summed scores or numerical uncertainty intervals are claimed.
- The second/third ordering and A30-versus-A100 preference reveal their judgment dependence.
- Shared generation, broad shortages and unverified price movements do not independently establish a candidate-specific anomaly.
- Direct observations, ordinary alternatives, explicit assumptions and predictions remain distinguishable.
