# Time-dependent supply substitution and lot-level inference

[Home](../README.md) · [Theory](theory.md) · [Study design](study-design.md) · [Sources](sources.md) · [Validation](validation.md)

This background supports the [current prediction ranking](current-ranking.md). The cohort protocol below is an optional route to future evidence. A sourced manufacturing hypothesis can be published before hardware observations exist; its uncertain timing and compatibility must remain explicit.

## Hypothesis and scope

A SKU is a marketed specification, not a guarantee of identical bill of materials (BOM) across its lifetime. The research unit is an identified hardware variant and production cohort, not just the product name. A negative result on one board cannot rule out a distinct cohort. Conversely, a positive result on one board does not establish the prevalence of that configuration.

**H-lot (unverified):** When the usual low-capacity component or preassembled package is scarce, a manufacturer may use an available, compatible higher-capacity assembly while retaining the original advertised capacity. Demand shocks, changes in product mix, long procurement commitments, yield harvesting, and end-of-life inventories are separate mechanisms that may create variant differences. The project has no supplier-specific evidence that this caused hidden HBM in A30, A30X or any other unverified candidate.

H-lot names a family of hypotheses, not a claim a finite volunteer survey could disprove everywhere. Before collection, specify the part/revision groups, manufacturing-stage date bounds, minimum difference, environment, collection limit and separate verdicts using the [study design](study-design.md). Physical heterogeneity, functional excess, cohort association and a supply cause can each have a different outcome. A negative result must not be evaded by silently redefining the target lot after seeing it.

HBM is attached alongside the GPU on a qualified package/interposer. Substituting an individual HBM stack during package manufacture and reassigning an already completed GPU+HBM package during board manufacture are different operations. Ordinary board assembly cannot simply exchange bonded stacks. Compatibility must cover interposer routing, stack height, electrical timing, power, thermal design, controller address mapping, firmware, test/qualification and contractual requirements. A readily available part is not necessarily a usable substitute. A high-density assembly may be defective, committed to another customer, or worth more in a high-end SKU.

See the [manufacturing-stage deductions](inference-refinement.md) and [v0.8 causal model](manufacturing-causality.md) for why a later shortage can motivate a still-possible reassignment but cannot retroactively change the original bonded population or a configuration decision already made irreversible. Rework and later reconfiguration require their own evidence. The substitution must also address the actual bottleneck: loose denser memory does not automatically bypass a shared packaging-capacity constraint.

## Economic model (illustrative decision criterion)

All quantities refer to one identified production cohort at the decision date, on the same accounting basis. Costs are incremental expected amounts, not original purchase prices or observed NVIDIA costs.

| Symbol | Meaning / definition | Unit | Domain / assumptions | Type |
| --- | --- | --- | --- | --- |
| $A$ | Incremental qualification, conversion, and test cost allocated to one shipped substitute unit | currency per shipped unit (non-SI) | Nonnegative real; same cohort/accounting basis | Scalar |
| $O$ | Opportunity cost of using the available high-capacity assembly instead of its best alternative disposition | currency per shipped unit (non-SI) | Nonnegative real; not its sunk purchase cost | Scalar |
| $F$ | Incremental expected failure, warranty and compliance cost of substitute | currency per shipped unit (non-SI) | Nonnegative real; same delivery obligation | Scalar |
| $K$ | Incremental cost of obtaining the usual assembly, excluding delay | currency per shipped unit (non-SI) | Nonnegative real; purchase or production basis stated | Scalar |
| $L$ | Expected incremental loss from waiting, missed deliveries or lost margin, relative to delivering on time | currency per shipped unit (non-SI) | Nonnegative real; avoid duplicated lost revenue | Scalar |
| $J_s$ | Incremental expected substitution cost, $A+O+F$ | currency per shipped unit (non-SI) | Nonnegative real; technically qualified alternative | Scalar |
| $J_w$ | Incremental expected usual-assembly cost including delay, $K+L$ | currency per shipped unit (non-SI) | Nonnegative real; same expected sales proceeds | Scalar |

For two mutually exclusive, technically qualified ways of fulfilling the same order with unchanged expected sales proceeds, their common proceeds cancel in the expected contribution comparison. The lower cost route is favored. Thus substitution is economically favored over waiting if

$$J_s < J_w \iff A+O+F < K+L.$$

All terms have identical currency/unit dimensions. This is a conditional decision rule, not a prediction of any company's action. If revenue, yield or delivery probabilities differ, use a full expected net-contribution comparison; cancellation or redesign can be a better third option. Avoid double counting lost margin in $L$ or acquisition cost in $O$. Sunk expenditure on stock is not its opportunity cost. Illustratively, a substitute with 20 qualification, 100 opportunity and 10 risk cost has cost 130; waiting with 70 part and 90 delay cost has cost 160 (arbitrary currency units per unit). If the high-end alternative raises opportunity cost to 300, the result reverses. No actual manufacturer costs are inferred.

## Dated context: 2020–2023

Use [supply events](../data/supply_events.csv) as a context ledger. Dates are event/announcement dates or explicitly labeled fiscal reporting-period ends, not dates of an individual board's production. Sources S21–S28 are primary announcements, filings or industry process descriptions.

| Date | Observed fact | Inference boundary |
| --- | --- | --- |
| 2020-02-04 | Samsung announced 16 GB HBM2E [S23] | Existence of density, not GPU qualification or local stock |
| 2020-07-02 | SK hynix announced volume production of HBM2E [S24] | Supply capability, not NVIDIA allocation |
| 2020-11-16 | NVIDIA announced A100 80 GB HBM2e [S25] | High-density architecture in commercial product line, not A30 compatibility |
| 2021-01-31 (FY end) | NVIDIA FY2021 filing described long lead times, inventory mismatch and supply commitments [S21] | Corporate context, not HBM-specific shortage |
| 2021-02-19 | NVIDIA's Japanese CMP announcement published [S13] | Date of the accessible Japanese article; not every individual SKU launch or manufacture date |
| 2021-04-12 | NVIDIA announced systems featuring A30/A10 [S26] | Product launch window; no board manufacturing dates |
| 2022-01-30 (FY end) | NVIDIA FY2022 filing described procurement at least twelve months ahead vs approximately six, and excess-inventory risk [S22] | Company-wide; expected near-term constraints mainly gaming/networking, not proven HBM shortage |
| 2022-09-15 | Ethereum Merge ended proof-of-work on mainnet [S27] | Demand-shock candidate; not proof that surplus was redirected to other SKUs |
| 2023-01-29 (FY end) | FY2023 filing described actual supply/demand mismatch varying by platform [S29] | Company-wide; no specific BOM substitution documented |

Semiconductor product-change-notification practice provides a way to search for affected part numbers, qualification and transition dates [S28]. This example is general industry practice, not evidence of a relevant NVIDIA PCN or a claim that all internally qualified substitutions are publicly announced.

## Testable predictions and alternatives

- **P1 (physical heterogeneity):** Same nominal SKU includes at least two independently identified physical memory densities or populated topologies. Establish that from reliable package identification and sources; different VBIOS/PCI IDs alone are insufficient.
- **P2 (time dependence):** Physical variants cluster in documented production cohorts, possibly a bounded interval around a supply or lifecycle change. Test earlier, transition and later cohorts; production shifts need not be monotone or match the announcement date because of manufacturing and shipping lags.
- **P3 (functional capacity):** Some higher-density variants have separately verified additional device-memory bytes. Physical presence does not imply functionality.
- **P4 (supply mechanism):** An attributable supplier/board-specific document or other direct evidence identifies substitution and its reason. A temporal correlation with corporate shortages supports a lead, not causation. Treat this as a separate claim from P1–P3.

Counter-hypotheses: ordinary low-density configuration; normal supplier diversity; yield-related binning; different OEM contract; revision change unrelated to shortages; post-sale repair or counterfeit; metadata mismatch; common firmware; and survivor/selection bias. A lack of published PCNs does not establish a lack of change. More HBM in an assembly could reflect product strategy rather than shortages.

## Cohort sampling and evidence gates

Collect `data/lot_observations.csv` rows from independently owned physical devices. Preserve raw date codes and their provenance, distinguish DRAM fabrication / package assembly / PCB manufacture / final board assembly / shipment / sale / test dates. Do not assume a date code format without a manufacturer reference. PCB manufacture can precede final assembly substantially. VBIOS build date is not a hardware manufacturing date; retail listing date is not a production date. Use date ranges where only bounds are known; do not force a week into a day. Missing values remain unknown. Do not publish full serial numbers or identifying photos. Use a stable anonymous sample ID and a non-sensitive cohort/lot token only when supported and safe to share.

Initial exploratory target: at least two independent owners per early/middle/late cohort of a priority SKU, ideally across independent acquisition channels and board/part revisions. This is a six-device target for coverage of potential variants, **not** a statistically sufficient sample or random design. Preregister date windows from sources rather than choosing them to fit successes; if dates are not documented, stratify by part/revision without pretending time is known. Keep uncertain and negative reports. Shared donor inventory or sellers can create correlated samples. For population prevalence, first establish a representative sampling frame and clustered confidence intervals; otherwise do not estimate a rate. Re-evaluate candidate priority when contradicting evidence appears.

**H/T/D/C/U:** H is a bounded instance of H-lot fixed in a dated study record; T is the separate P1–P4 comparison above; D is reported separately for each prediction and cohort using the [claim-specific decision rules](study-design.md) (supported, contradicted within scope, uncertain); C is the set of alternative explanations; U comprises date-code interpretation, missing/biased cohorts, repair history, package identification, test coverage, and nonindependent samples. No combined measurement uncertainty or causal probability is calculated without data. A failed initialization alone is uncertain, not proof of missing physical memory. Supply context, cohort association, physical capacity, and usable capacity each require their own evidence.

## Priorities for dated collection

CMP 170HX: compare 1585/1586 and other documented variants as external controls; establish dates independently, do not infer package origin from IDs. CMP 100-200 and 100-100: date/board IDs, donor generation, and memory part markings; older silicon may have been packaged or repurposed later. A30: compare early/late 24 GB boards and distinct memory-part/PN groups; verify actual chronology before invoking the 2020–22 transition. A30X and PG199: separate qualification and OEM restrictions; negative observations are particularly valuable. V100 16/32 GB and P100 12/16 GB: controls for known capacity differences, not evidence that their advertised SKU masks capacity.

**ERROR CHECK:** This document does not assert a particular excess HBM inventory, compatibility, substitution, or capacity recovery. The inequality is a conditional model; context events are not per-lot evidence. No lot observations have been generated or measured by this project.
