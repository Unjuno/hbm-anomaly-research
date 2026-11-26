# Forecasting recurrence across generations and production cohorts

> **v0.10 correction:** This document supplies historical hypothesis-generating context. Similarity-based ranking tiers are withdrawn. Target evidence distinguishing ordinary and excess-memory models is assessed in the [current assessment](current-ranking.md) and [inference method](diagnostic-inference.md).

[日本語](recurrence-hypotheses.ja.md) · [Current ranking](current-ranking.md) · [Historical context](historical-context.md) · [Precedent ledger](../data/capacity_precedents.csv) · [Manufacturing causes](manufacturing-causality.md) · [Capacity constraints](capacity-constraints.md) · [Sources](sources.md)

**v0.11.0 — 2026-11-26. Documentary forecasts; no new hardware measurements.**

This research forecasts where previously observed or reported capacity restrictions and excess population may recur. Historical precedents help **select manufacturing routes and cohorts to investigate**. They justify looking for a reusable product or manufacturing mechanism across related generations, then predicting the part and production groups in which it would appear. General resemblance alone does not justify ranking excess population as more plausible than ordinary construction.

The central question is: **given that related outcomes have occurred before, which existing products and cohorts share the conditions that could produce them again?** A forecast can be useful before its target parts are identified. We record what makes it plausible, where it should cluster, and what would weaken it. Population confirmation and operational health remain separate records.

## 1. What the precedents let us predict

Repeated outcomes can make a common mechanism a better research lead than treating every lower-capacity product as an unrelated case. Potentially reusable decisions include assigning one assembly to several product tiers, limiting the capacity exposed for a particular use, substituting a qualified available part, and selling a completed package after excluding selected resources.

The precedents establish different things. A report of extra physical memory supports the feasibility of that outcome; it does not by itself identify the manufacturer's motive. A successful capacity change supports that particular configuration path; it does not establish that later generations use the same controls. The forecast transfers the **manufacturing or product decision**, while part compatibility and configuration details remain product-specific.

### Keep generation, manufacture, observation and publication separate

The generation of a chip, the production date of a particular board, the date of an observation/trial and the publication date of its report are different. An experiment date stated by an owner is not automatically its publication date. An older architecture can receive a new report years later. That report can inform older-generation recurrence without establishing that its discovery preceded another report.

| Precedent | Established historical input | How it contributes to the forecast |
| --- | --- | --- |
| **RX 480 4 GB / 8 GB, 2016** | AMD announced both capacities. A July 2016 first-person retail report identified an 8 GB GDDR5 population on a 4 GB-labelled card and reported expanded operation [S53,S54]. The sourcing explanation is a contemporary report, not an internal procurement record [S55]. | A lower advertised capacity can coexist with higher original population in a consumer product. Temporary sourcing is a plausible reported explanation; the HBM packaging route must still be considered separately. |
| **P104 owner report, 2018-12-02; later discussion in 2019** | A user post hosted on ASUS's forum claims 8 GB installed with half exposed [S84]. Later owner discussion includes mixed results [S17]. The ASUS-hosted post is a user's claim, not a vendor endorsement or a complete capacity-validation record. | A mining-oriented restriction is an older-generation precedent worth pursuing. Mixed reports motivate variant/cohort predictions rather than treating all cards as identical. The separate Gigabyte 4 GB product specification [S85] does not identify the ASUS unit's population. |
| **CMP 100-100, GP100 family** | GP100 belongs to the architecture introduced in 2016 [S86]. The owner dates the two-device capacity trial to 2026-11-02 [S04a]; this is neither the CMP boards' manufacture date nor an established first-publication date. | A Pascal-family CMP report provides a close product-line precedent for investigating the Volta CMP variants. Architecture chronology and report chronology are retained separately. |
| **CMP 170HX, GA100 family** | External research describes capacity changes for identified 8 GB and 10 GB variants, with differences between variants [S03,S19]. This project does not establish the first discovery date. | A later architecture in the same mining product line supplies another capacity-restriction reference. It strengthens the reason to examine related CMP variants while leaving each variant's parts and excluded resources to be explained. |

The [precedent ledger](../data/capacity_precedents.csv) preserves source type, dates and limitations. The ledger is not a random sample of products. Its number of positive stories cannot be converted into a frequency or success rate; negative and mixed reports belong in the comparison too.

## 2. Three recurring mechanisms make different cohort predictions

These are **working causal hypotheses**, not established motives for every precedent above.

| Recurrence mechanism | Why it can recur | Positive prediction about cohorts | What would weaken that prediction |
| --- | --- | --- | --- |
| **Durable commercial capacity restriction** | A common assembly can serve different uses, contracts or product tiers while exposing different resources | Similar part/package groups retain the same reduced capacity across multiple revisions or deliveries. The pattern need not be confined to a brief shortage episode | Documentation shows a dedicated lower-density physical design throughout the named scope, or the apparent capacity difference is only metadata/accounting |
| **Temporary qualified-part substitution** | An available compatible denser part can meet an order when the usual assembly is delayed or otherwise less attractive | The same nominal-capacity product contains a distinct original part/revision group with different density. The group is associated with the relevant assembly and sourcing interval, possibly blurred by inventory and shipment delays | The substitute was unavailable, incompatible, committed elsewhere, or more valuable in its alternative use; identified target parts consistently support the ordinary construction |
| **Post-bond grading or harvesting** | A completed package can be used in a lower product after excluding resources that fail a grade or are not needed for the target | A package lineage retains physical resources while enabled regions or product grades differ. Grouping by package, configuration and grading history is more informative than grouping only by sale date | The relevant selection occurred before the extra memory was attached, or the target design uses a physically smaller dedicated population |

### Completed-package reassignment is a distinct substitution branch

A temporary shortage can be addressed by changing loose parts before assembly or by reassigning an already completed compatible package. The latter predicts **continuity of package identity with a later change in allocation or permitted configuration**. It need not predict a later HBM date code or a newly manufactured memory part.

This branch matters when the constrained resource is packaging capacity. An already assembled package may avoid repeating the constrained operation; denser loose HBM still needs an assembly route. TSMC's 2023 distinction between front-end support and constrained CoWoS capacity illustrates why the bottleneck location matters [S83]. A later supply event must precede the particular decision it is proposed to change [manufacturing model](manufacturing-causality.md).

### The reason for grading predicts different prospects

If compute, power or frequency qualification causes the downgrade, retained HBM is a plausible place to look for additional healthy resources. If the memory or its connection caused the downgrade, physical surplus may instead include failing regions. These are different branches of the forecast. A product's grade alone does not decide which branch applies; corresponding test or grading information would change the assessment.

## 3. Candidate forecasts: where recurrence should cluster

The following statements are **predictions to investigate**, not claims that a favorable production group has already been found. A group is defined by attributable package/part identity, original configuration and any supported manufacturing interval. A new seller name or later resale date is insufficient to create a new manufacturing group.

| Candidate | Forecast from the recurring mechanism | Expected grouping if the forecast is right | Main competing construction or weakening information |
| --- | --- | --- | --- |
| **CMP 100-200, about 6 GB** | A larger compatible assembly was capacity-restricted in part of the Volta mining product line, analogous at the product-decision level to the Pascal and GA100 CMP references [S02,S04a,S03,S19] | The suspected configuration clusters by original package/board identity and capacity-setting family; another group could retain an ordinary smaller population | Target width and parts remain to be identified. A genuine compatible lower-density construction explains the capacity without the proposed surplus. TITAN V is a comparison, not the target's population map [S32,S36] |
| **CMP 100-210, 16 GB** | Some identified board families used a denser compatible assembly while retaining the marketed capacity | Differences follow the documented board/device families rather than all “CMP 100” labels. Original part identities distinguish a capacity branch from performance-only changes [S04,S14,S33] | Ordinary V100-derived 16 GB construction; existing performance improvements need no extra capacity |
| **A30** | Shared GA100 packages or post-bond grading left extra memory regions on a subset of original package groups | Part/package lineage explains which groups have inactive regions; a denser-part substitution would be a separate address-depth branch [S06,S35] | The ordinary 24 GB construction remains viable. Extra compute blocks do not establish extra memory [S34] |
| **DRIVE A100 / PG199** | An OEM package lineage was assigned a smaller capacity and later appeared in another commercial channel | Original OEM module and package identifiers cluster the construction; repaired or rebadged PCIe cards form separate histories [S12,S35] | A normal 32 GB OEM population or later modification explains the observed card without factory high-density restriction |
| **A800 40 GB Active** | A later eligible allocation of a GA100 package retained physical resources beyond the target's exposed capacity | Candidate parts map to an earlier or shared GA100 package lineage; the relevant configuration/allocation was still changeable at reassignment [S25,S60,S71] | An ordinary 40 GB assembly is already sufficient. Later introduction alone does not identify surplus donor material |
| **MI50 16 GB** | A density or package transition included some original 16 GB groups using the denser same-family construction | HBM part and revision groups differ while the 16 GB baseline is retained; a procurement interval is inferred only if it is documented [S38,S80] | The normal lower-density construction and stale labels are distinct alternatives. A 32 GB sibling supplies a concrete comparison, not a part identification on the lower-capacity group |
| **H100 SXM5 64 GB HBM2e** | A common or compatible HBM2e package lineage was configured or graded into the 64 GB category | Exact package/part groups connect the 64 and higher-capacity categories; width and mapping distinguish depth restriction from inactive regions [S60,S64] | A dedicated ordinary 64 GB population. Another support-list entry adds SKU documentation but no new package relationship |
| **H100 SXM5 80 GB** | Some original package revisions retain a real additional memory region after grading or configuration | The content and density of the additional site cluster by actual package revision [S62,S63] | A dummy/support site or the ordinary five-active-stack construction; this direct alternative weakens the additional-memory forecast |
| **RX Vega 56 / 64 8 GB** | Qualified dense parts or completed compatible packages were temporarily used in an original RX group | A specific RX package and HBM-part group differs while nominal capacity remains 8 GB; the proposed interval follows documented part availability [S45–S49] | Ordinary lower-density RX parts, different soldered packages despite a common PCB, and high demand for the denser parts themselves |
| **BC-160** | A mining derivative reused a compatible denser production assembly | A particular original BC-160 package group can be linked to that denser assembly [S50–S52] | The ordinary reported 8 GB construction; no established shipped 16 GB Navi 12 counterpart in the current evidence |
| **A30X** | A converged-module package group used denser qualified HBM with restricted exposure | The pattern follows the exact integrated module/package revision, with an independently sourced effective width [S01,S10,S11] | Ordinary density plus faster signaling; bandwidth alone does not supply the missing width or part identity |

These forecasts intentionally do not prescribe “early is better” or “late is better.” Durable product segmentation, temporary substitution and later inventory reassignment predict different time patterns. The relevant historical mechanism chooses the direction; a generic calendar rule does not.

## 4. Make the ordinary construction carry its own evidence

The arithmetic model remains useful: a normal low-density construction can explain a capacity/width pair. Its physical feasibility is a separate input. The alternative part must also meet the relevant signaling, voltage, package, addressing and time constraints.

| Evidence behind the ordinary explanation | Interpretation for the forecast |
| --- | --- |
| Parts and population documented on the target unit or an applicable target-product configuration | A concrete ordinary construction; strong counterevidence for that scope |
| A normal same-family configuration is documented | A meaningful alternative with a close design relationship; applicability to the target group still matters |
| Only a component catalogue shows a suitable density | The part exists; target qualification, package fit and availability need separate support |
| Only capacity/width arithmetic fits | A possible model whose necessary real parts and implementation have not yet been identified |
| Key inputs remain unresolved | A specified missing input, not evidence that either excess or ordinary population is impossible |

An arithmetic-only ordinary possibility should not receive the same evidential weight as an identified factory population. Conversely, failing to find a low-density part in an incomplete public catalogue does not establish that no such part existed. The useful forecast states **which concrete ordinary assembly would have to exist to remove the anomaly**, then looks for it.

## 5. History updates manufacturing plausibility and the cohorts to investigate

Contemporaneous sources can make a hypothesis more specific before hardware is available. The first updates concern **whether the proposed manufacturing route was feasible given its period, parts and supply conditions**, and which cohorts would distinguish it from ordinary construction. This work can proceed while the separate `physical_status` field remains unconfirmed. [Historical context](historical-context.md) applies the method to individual candidates and records the direction of each update.

| Stage | Relationship to examine | What it can update, and its limit |
| --- | --- | --- |
| **1. Chronological fit** | Did the supply event precede the assembly, configuration or reassignment decision it is proposed to change? Separate announcement, expected shipment, manufacture and resale dates | Narrow the relevant manufacturing interval and reject explanations with reversed time order. A later reassignment is a separate decision to investigate. Later product introduction alone does not show use of denser parts |
| **2. Compatible parts and inventory form** | What was constrained, and what was available? Distinguish loose HBM, completed GPU-plus-HBM packages and finished cards in the channel; examine density, signaling, voltage and package compatibility | Support or narrow a specific substitution or reassignment route. An industry-wide shortage or finished-card inventory is not evidence of surplus compatible high-density HBM |
| **3. Difference from the ordinary explanation** | Could normal-density supply, price reductions or ordinary reuse explain the same event? Which clustering of parts, revisions or settings is predicted specifically by excess population? | Target-specific differences can strengthen the excess-memory hypothesis. Background shared by both constructions can support a feasible route without selecting excess population over the ordinary alternative |

These stages do not require every internal record or hardware observation before a forecast can be made. Use established relationships and leave the unresolved ones as explicit conditions. For example, a documented supplier change can identify package groups worth comparing. If normal-density parts can undergo the same change, it does not yet supply evidence of hidden capacity.

**The R1/R2/R3 tiers withdrawn in v0.10 are not reinstated.** The eleven candidates above are hypotheses to investigate, not a current ranking. The register preserves the old v0.9 tiers in `v09_recurrence_tier` and the old v0.8 specificity tiers in `v08_specificity_tier` as history. Adding general family resemblance does not change the [current assessment](current-ranking.md).

The order of documentary work can change as a testable period, part relationship or cohort becomes more specific. That order is not a hidden-capacity probability ranking or a recovery success rate. Repeating the same story on several websites adds no independent recurrence event; a capacity/width ratio calculated from the same specifications is not another independent observation.

## 6. A compact H / T / D / C / U for documentary forecasting

| Item | Application |
| --- | --- |
| **H — forecast** | Name the candidate, proposed recurring decision, predicted part/cohort pattern and the date or historical interval being considered. Distinguish a still-unknown group boundary from a claimed favorable lot |
| **T — minimum next step** | Identify the one source or part relationship that would most distinguish the proposed group from its ordinary alternative. One original source may settle a narrow premise; there is no universal source-count threshold and no purchase requirement |
| **D — update rule** | Apply PASS/FAIL to a named premise such as chronology or compatibility. Distinguish support for a manufacturing route from support that selects excess population over ordinary construction. If the constructions remain indistinguishable, the excess-memory assessment stays UNCERTAIN while the cohort and next source to investigate become more specific |
| **C — alternatives** | A purpose-built lower-density product, planned common parts without excess, defective memory, ordinary resale, repaired assembly, or capacity-label/accounting differences |
| **U — uncertainty** | Record source dependence, incomplete part catalogues, missing configuration dates, ambiguous group boundaries and repair history. No numerical combined uncertainty or probability is assigned without an applicable model |

Fix the cohort definition when it becomes supportable. If negative information contradicts that named group, retain the negative result. A new group requires a new attributed reason, not an unnamed escape after every contradiction. One normal unit can constrain its group without erasing the broader recurrence hypothesis; one positive unit can establish its construction without establishing market prevalence.

## 7. Connections and ERROR CHECK

**Computer architecture** supplies the capacity, width and addressing constraints. **Packaging and reliability engineering** distinguishes original part population, post-bond selection and repair. **Industrial economics and manufacturing history** explain when common parts, substitution or reassignment could be attractive. **Causal inference** separates architecture chronology, manufacturing decisions, later reports and shared evidence. These roles support a predictive research programme even when the project owns no hardware.

**Next question:** for one candidate, which part or configuration difference within the cohort suggested by its historical context would distinguish ordinary construction from hidden capacity?

### ERROR CHECK

- Historical precedents inform predictions about manufacturing routes and cohorts; direct hardware confirmation is not an entry requirement.
- Architecture, production, observation/trial and publication dates remain separate.
- The ASUS-hosted P104 statement is attributed to a user; the separate Gigabyte specification is not substituted for that user's board.
- Manufacturing motives remain hypotheses unless separately sourced.
- Known ordinary parts and arithmetic-only ordinary models receive different descriptions.
- Chronology, compatible parts and inventory form, and differences from the ordinary explanation are examined in sequence; manufacturing feasibility and evidence of excess capacity remain separate.
- The v0.10 ranking withdrawal remains in force; general resemblance and documentary-work priority are not recast as an excess-memory ranking.
- No favorable exact lot, recovery probability, new measurement, or universal cross-generation configuration method is asserted.
