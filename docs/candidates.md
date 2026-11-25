# Ranked hypotheses: which HBM products look suspicious, and why?

> Historical NVIDIA-only v0.4.0 snapshot. For the expanded current investigation order, see [cross-vendor ranking](cross-vendor-ranking.md). The earlier five predictions are preserved for comparison; Intel's documented physical surplus is a distinct evidence class.

[Home](../README.md) · [日本語ランキング](ranking.ja.md) · [Ranking method](ranking-method.md) · [Physical theory](theory.md) · [Sources](sources.md)

**Forecast register — 2026-11-25. Every ranked candidate below is unconfirmed.** We do not own the candidate hardware. The main output is a reasoned, revisable prediction from public specifications, product relationships, historical conditions and attributed owner reports.

The ranking asks: **could an identifiable variant already contain ordinary HBM data capacity beyond its nominal capacity, with some of that additional capacity still healthy but unexposed?** Physical presence, health and accessibility remain different claims. The forecast proposes physical excess with a healthy unexposed subset; it does not establish either premise on a ranked candidate. Practical software recovery and the amount recoverable are separate unknowns. Dedicated ECC and spare cells do not count as hidden ordinary data capacity.

This is an ordinal judgment about a particular suspicion, not a success probability, purchase ranking or statistically calibrated score. All positions have substantial uncertainty. Existing external capacity-expansion reports appear as comparison cases outside the novel-candidate ranking.

## 1. Current ranking

| Rank | Candidate and nominal capacity | Conditional forecast | Why it is suspicious | Strongest ordinary explanation | Forecast confidence |
| --- | --- | --- | --- | --- | --- |
| **1** | **CMP 100-200, about 6 GB class** | Some variants may retain healthy unexposed data capacity in a **12 GB-class** assembly. | A capacity-specific reduction relative to a known 12 GB Volta product, plus a 6-to-12 GiB precedent in a different CMP generation. | Genuine lower-density or defective/partly active HBM; actual width and parts remain unknown. | **Low**; strongest relative lead, not a strong absolute prediction. |
| **2** | **A30, 24 GB** | Some package groups may retain healthy HBM beyond 24 GB; **32 or 40 GB-class** assemblies are the first conditional constructions. | A reduced GA100 configuration in a family with larger memory assemblies provides a plausible exclusion mechanism. | Ordinary 24 GB population, omitted/dummy sites, or populated extra regions disabled because they are defective. | **Low**; same weak tier as rank 3. |
| **3** | **DRIVE A100 / PG199, 32 GB class** | Some OEM variants may retain healthy unexposed capacity from a denser assembly; **64 GB class** is a conditional construction. | An unusual GA100-derived OEM configuration creates a product-reuse hypothesis. | A purpose-built 32 GB assembly, or excluded regions that do not meet the intended operating conditions. | **Low**; rank 2/3 can reasonably be tied or reversed. |
| **4** | **CMP 100-210, 16 GB class** | An unidentified density cohort could contain healthy unexposed memory beyond 16 GB; **32 GB class** is a weak construction. | Same-name board/firmware families differ, so a uniform SKU assumption is unsafe. | Ordinary 16 GB V100-derived memory, with restrictions applying to computation, clocks and PCIe. | **Very low**; little capacity-specific support. |
| **5** | **A30X, 24 GB** | A high-density package variant could retain healthy unexposed memory; **48 GB class** is a conditional construction. | Product-family reuse leaves a substitution pathway conceivable. | A normal 24 GB assembly; bandwidth does not require higher density. | **Very low**; weak positive support. |

All larger capacities are **hypothetical total physical data capacities**. They are not measured totals, promised healthy totals or software results. The amount of healthy extra memory could be smaller, including zero. These are discrete constructions, not confidence intervals; the ordinary-capacity scenario remains viable for every candidate.

**Why A30 is provisionally second:** our analyst judgment first considers additional same-density regions in its reduced active-interface configuration, whereas PG199's central 64 GB construction adds an unverified density-substitution premise. Compute-resource recovery supplies no positive HBM-capacity evidence. A conventional 32 GB configuration also readily explains PG199. Neither has direct part-level evidence for the proposed excess, so their ordering is fragile and should not be presented as a meaningful probability gap. See the [ranking method](ranking-method.md).

## 2. Rank 1 — CMP 100-200

**Facts and attributed reports.** NVIDIA lists this as a Volta product [S02]. A dated owner log reports `6016 MB` total in its displayed notation [S05]. Preserve that notation rather than converting it silently to MiB. NVIDIA's 2017 TITAN V announcement establishes a 12 GB HBM2 product in the same architecture generation [S32]. Neither source establishes the CMP's bus width or memory density. The review video remains a lead, not a transcribed package specification [S15]. The documented CMP-to-TITAN-V conversion is explicitly classified as a community description/screenshot without local reproduction [S33]; a changed identity would not by itself establish more memory.

**What we predict.** The best unconfirmed capacity-specific lead is a CMP 100-200 variant whose approximately 6 GB exposed capacity is a reduced view of a larger assembly, with at least some additional cells healthy. Our central construction is 12 GB class.

**Why it is suspicious.** A mining SKU can prioritize throughput while accepting a small advertised working set. Related Volta hardware supports a larger capacity, and the separate GP100 CMP 100-100 reports make capacity limiting across mining products a concrete analogy [S04a]. This is a product/generation analogy, not a shared implementation or manufacturing-date claim. We rank it above 100-210 because the suspicious feature concerns capacity itself, whereas 100-210's documented restrictions mainly concern performance and connectivity.

**Capacity construction and assumptions.** Three real 4 GB-class stacks would give a 12 GB-class physical assembly. A 3072-data-lane active interface is compatible with that construction, but neither the width nor those parts is established here. A bus-width equivalent is not a physical stack count. Reduced addressing or partial use could explain exposing less; defects remain a competing reason. The healthy-extra hypothesis additionally assumes that not all excluded ordinary cells are defective. There is no present basis for making 24 GB the central forecast.

**Strongest ordinary counterargument.** Approximately 6 GB may describe a complete low-density assembly. Early HBM2 research included lower-density stack configurations; 4 GB is not a universal minimum compatible density [S36]. Lower-density memory, partly active interfaces and defective regions can explain the same label. Unknown width is a missing premise, not positive anomaly evidence.

**Lot conditions.** Keep board PN/revision, part markings and independently supported production dates separate. The identifiers `1dc1` and `1d83` are search keys where documented, not evidence of density differences. A donor/package relationship would strengthen the conjecture; a general 2021 shortage narrative does not date older silicon or its assembly.

**What changes its rank.** Greater physical density tied to an actual unit, plus evidence that some excluded data capacity remains functional, would move it up. Identified ordinary low-density population, a mistaken product identity, or evidence that excluded regions are defective would move it down. Defects reduce the healthy-extra forecast without proving physical absence.

## 3. Rank 2 — NVIDIA A30

**Facts and attributed reports.** NVIDIA specifies 24 GB HBM2, 3072-bit and peak bandwidth up to 933 GB/s, with board PN prefix `699-21001-0205` [S06]. This is a normal capacity-per-active-width relationship. Full GA100 architecture has a larger memory-interface design, which does not establish A30 package population [S35]. An owner reports recovering four compute SMs on one A30 in October 2026, while explicitly stating that extra memory was not recovered and configuration reads did not establish hidden capacity [S34]. This is a compute-resource observation, not an HBM-capacity result. Community memory-mask interpretations remain contested [S11].

**What we predict.** Some A30 package groups might retain ordinary memory beyond 24 GB, with a healthy subset excluded by their exposed configuration. A shared package with disabled interfaces is the main construction, rather than a claimed density anomaly in the published specification.

**Why it is suspicious.** A reduced memory configuration inside a larger architecture creates a plausible place for inaccessible but populated components. Reusing a qualified package can be economical when availability, requalification cost or product mix favors it. The same economics can also favor a purpose-built lower-capacity assembly, so company-level supply history modestly motivates the conjecture without proving it [S21,S22].

**Capacity construction and assumptions.** The 32 and 40 GB-class scenarios assume respectively four or five real 8 GB-class stacks, or an independently established equivalent population. These are assumptions, not quantities derived from 3072-bit. Some excluded capacity must also remain healthy for the ranked hypothesis. There is no basis to escalate the central forecast to 64 or 80 GB from the GA100 family name alone.

**Strongest ordinary counterargument.** Three ordinary 8 GB-class stacks, with other sites omitted or nonmemory, explain 24 GB. Alternatively, extra parts could be present but excluded because of defects; physical presence would then overstate the usable opportunity. The official width/bandwidth relationship forces neither additional parts nor healthy excluded regions. The 32 GiB BAR1 aperture is an address window, not extra memory [S06].

**Lot conditions.** A documented package or HBM-part change while retaining the 24 GB specification would be a relevant cohort. The 2020 density announcements, product launches and later supply commitments are context, not proof that such a cohort exists [S22–S26]. No currently identified manufacturing interval is presented as a favorable lot.

**What changes its rank.** Part-level evidence of greater population and credible evidence of healthy excluded regions would move it up. Repeated minimal-population observations, or defect evidence for the excluded regions in the stated package group, would move it down. More SMs, a larger BAR or a new mask interpretation alone do not justify a higher memory forecast.

## 4. Rank 3 — DRIVE A100 / PG199

**Facts and attributed reports.** An owner describes integrating four PG199 / DRIVE A100 modules and reports 32 GB per card [S12]. This demonstrates an unusual automotive/OEM platform in a different host context, not capacity beyond 32 GB. Some package and density statements remain community reports [S11]. Exact form factor and part identity matter; not every DRIVE-branded listing is the same assembly.

**What we predict.** Some OEM variants could retain a denser memory assembly than their 32 GB exposed configuration uses, with some excluded data capacity healthy. The 64 GB-class construction has greater hypothetical upside than A30's central constructions, but upside does not determine the suspicion ranking.

**Why it is suspicious.** OEM qualification, package reuse, product requirements and later inventory disposition provide plausible mechanisms for variants that differ from ordinary data-center SKUs. This is a concrete product-history question, yet it does not distinguish restricted high density from a normal 32 GB OEM design. That weak discrimination keeps PG199 in the same weak tier as A30.

**Capacity construction and assumptions.** 64 GB class assumes four real 16 GB-class data stacks, or separately established equivalent population, with only part exposed. Neither stack count nor density follows from the name or package outline. Four ordinary 8 GB-class stacks would explain 32 GB. The owner's bandwidth notation is ambiguous, so we do not derive a verified bus width or density from it [S12].

**Strongest ordinary counterargument.** A deliberately qualified 32 GB assembly is sufficient; excluded resources may also fail the intended operating requirements. Larger GA100 products supply no missing part evidence. Adapters and host integration can explain improved usefulness or demand without newly discovered memory.

**Lot conditions.** Separate automotive platform generations, SXM/PCIe versions, board revisions, package markings and repair/transplant history. Inventory entering the market later need not be newly manufactured. A 32 GB module does not inherit the capacity forecast of a visually similar CMP 170HX.

**What changes its rank.** An identified PG199 part group with greater ordinary capacity and healthy excluded regions would move it up and could reverse its order with A30. Confirmed ordinary density, transplant/relabeling explanations or documented failed extra regions would move it down. Mere scarcity or a larger sibling leaves the forecast unchanged.

## 5. Rank 4 — CMP 100-210

**Facts and attributed reports.** Owner research distinguishes `1df4` / PG500 SKU111 from `1d84` / SKU110 [S04,S14,S33]. One investigated `1df4` unit is reported as V100-PCIE-16GB-derived silicon without memory-interface floorsweeping. The same project inspected nine `1d84` cards read-only and did not claim that one-card result for them [S04]. Its memory improvement refers to clock/bandwidth, not capacity.

**What we predict.** An unidentified density cohort could contain healthy unexposed memory beyond its 16 GB configuration. This is a weak extension of a documented variant distinction, not a result implied by the existing performance improvements.

**Why it is suspicious.** Same-name board/firmware families demonstrably differ, giving a concrete axis on which a component-substitution hypothesis could vary. However, existing differences mostly concern compute and connectivity. The ordinary 16 GB V100-derived explanation fits the product without unused DRAM; a general configuration-control mechanism is not repeated evidence for a memory restriction.

**Capacity construction and assumptions.** 32 GB class requires a higher-density physical assembly, for example four real 8 GB-class stacks, and a healthy excluded subset. V100's known 16/32 GB options establish family-level density variation [S08]; they do not identify a CMP's installed parts. No confirmed 16-to-32 GB result appears in the sources reviewed here.

**Strongest ordinary counterargument.** The card exposes all its ordinary 16 GB capacity while restricting performance and connectivity. This accounts for the existing owner results without hidden healthy memory.

**Lot conditions.** `1df4` versus `1d84` can organize source records. Their VBIOS build dates in 2018/2019 are not manufacturing dates. A density-specific part change, rather than nomenclature alone, would identify a more suspicious cohort.

**What changes its rank.** Exact part markings showing additional ordinary capacity and evidence of healthy excluded storage would move it up. Population matching 16 GB across the stated groups would move it down. Tensor, FP64, PCIe and clock improvements without capacity evidence remain neutral.

## 6. Rank 5 — A30X

**Facts and attributed reports.** NVIDIA lists 24 GB HBM2e and 1223 GB/s peak for A30X, alongside 80 GB and 2039 GB/s for A100X/AX800 [S10]. The table does not establish A30X's bus width or density. An attributed community report describes an unsuccessful memory-related attempt, with insufficient primary evidence to generalize to all units [S11].

**What we predict.** A particular A30X package group could use denser memory while retaining a 24 GB exposed configuration and a healthy excluded subset. The central construction is 48 GB class. This is the weakest of the five positive conjectures.

**Why it is suspicious.** The larger family assembly supplies a possible reuse/substitution mechanism. Yet this is weaker than evidence that A30X actually shares that physical population, and the converged module has its own qualification constraints.

**Capacity construction and assumptions.** 48 GB class assumes three real 16 GB-class stacks with only half their data capacity exposed. Topology, compatible parts and actual substitution are all unverified. Three ordinary 8 GB-class stacks would produce 24 GB; a suitable transfer rate can explain high bandwidth without denser memory. A bandwidth ratio between products cannot establish the missing width or physical count [S01,S10].

**Strongest ordinary counterargument.** Normal population explains the capacity without hidden memory. The attributed negative report remains a source-tracing lead and is not used to determine the rank because the primary record and its scope were not obtained. A failed attempt alone would prove neither physical absence nor defective memory.

**Lot conditions.** Compare exact module/board part groups, not all converged accelerators sharing a GPU family. A later data-sheet publication date is not a manufacturing transition.

**What changes its rank.** Attributable denser-part evidence and a healthy excluded region would move it up; ordinary population or confirmed defective excluded regions would move it down. High bandwidth, the larger sibling and unexplained initialization failures are insufficient by themselves.

## 7. External comparison cases, outside the novel ranking

| Product | Evidence used here | Role and limitation |
| --- | --- | --- |
| CMP 170HX | Community synthesis reports selected 8-to-64 GB-class and 10-to-40 GB-class cases, plus 32 GB exceptions for some identities [S03,S16]. | Existence example for capacity restrictions. Variant differences prevent a universal product claim; these are external reports. |
| CMP 100-100 | The owner reports two 6144-to-12288 MiB enumerations and two 11264 MiB checker logs with zero reported failures; reserved coverage, device association and stack details have limits [S04a]. | A precedent in another CMP architecture, with explicitly limited evidence coverage. |
| P104-100 | Historical owner accounts describe 4-to-8 GB GDDR outcomes and failures [S17]. | Product-segmentation analogy only, outside the HBM scope. |

Known results informed these hypotheses. They are not an independent blinded validation of the ranking or the numerical screening heuristic.

## 8. Watchlist and ordinary comparisons

These remain speculative extensions below the ranked leads. A shared die or a larger sibling is too common to establish an anomaly by itself.

| Product family | Explicit speculation | Why it is not promoted |
| --- | --- | --- |
| **A100 40 GB** | **48 GB class** if a sixth real 8 GB-class stack is populated but excluded; separately, **80 GB class** if a 40 GB SKU uses five 16 GB-class stacks with a restricted configuration. Both healthy-extra hypotheses need healthy excluded cells. | These are different constructions. Full GA100's six-interface architecture and commercial 40/80 GB options do not identify population, health or substitution [S09,S25,S35]. An omitted/dummy site defeats the first; defects defeat its healthy-extra benefit even when memory is present. |
| **P100 12/16 GB** | Lower-capacity variants might retain healthy excluded memory. | Official capacity and active-width changes are proportional and have an ordinary explanation [S07]. No specific extra-capacity cohort is identified here. |
| **V100 16/32 GB** | A 16 GB-labelled cohort could reuse denser parts with some healthy capacity unexposed. | Different real densities explain the published products despite identical width/bandwidth [S08]. No lower-SKU substitution is established. |
| **AMD MI50 and related Vega 20 products** | Product-family reuse or later density substitution is conceivable. | The 2018 MI50/MI60 capacity difference supplies a comparison, not a hidden-memory result [S37]. No capacity-specific discrepancy or attributable hidden-capacity variant is established here. |
| **Other HBM accelerators** | Later-generation or OEM variants may provide further mechanisms. | Add a concrete part/configuration discrepancy and its strongest ordinary explanation before assigning a rank. |

## 9. How history and prices affect the forecast

The [lot-history model](lot-history.md) explains when a qualified higher-capacity assembly could be an economical substitute. Shortages, excess stock, end-of-life production and product-mix changes can make one nominal SKU heterogeneous. These are distinct possible causes; corporate context does not identify a favorable lot for any row above.

Price would strengthen a lead if a reproducible premium selectively followed a relevant part/revision after accounting for ordinary differences. Whole-model appreciation can follow compute improvements, adapters or broad AI demand. This release has no adequate verified transaction series, so **price contributes no positive weight to the present ordering**. Missing price evidence is not negative price evidence. See the [market protocol](market.md).

Public desk research is sufficient to propose and revise the ranking. Hardware ownership is not required to contribute a source, counterexample, historical mechanism or better prediction. Independent measurements, when available, can update it through the separate [validation protocol](validation.md); they are not a prerequisite for stating a conditional hypothesis now.

## ERROR CHECK

- The target hypothesis combines installed excess with a healthy unexposed subset; those underlying claims remain separate and unconfirmed.
- Each larger capacity is a conditional total physical construction, not a measured value, healthy total or promised software result.
- Missing widths, density and manufacturing dates remain unknown.
- Ranks 2 and 3 share a weak tier; their order is analyst judgment, not a calibrated probability gap.
- Performance, identity, BAR and broad supply events are not memory-capacity measurements.
- Defects can undermine the healthy-extra hypothesis without refuting physical population.
- Existing positive reports are comparison cases; ordinary configurations remain explicit alternatives.
