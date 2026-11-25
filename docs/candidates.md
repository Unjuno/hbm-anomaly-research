# Candidate register

[Home](../README.md) · [Sources](sources.md) · [Machine-readable data](../data/devices.csv)

Updated 2026-11-25. Source classes: `vendor` (advertised specifications), `owner` (external individual measurement), `community` (curated or secondary report), `hypothesis` (not an observation). Priority reflects **information value**, not probability or commercial upside. This initial register is non-exhaustive.

## P1 — high information value

| Candidate | Evidence and reason | Conditional research question | What would reduce priority? |
| --- | --- | --- | --- |
| CMP 100-200 (Volta) | NVIDIA lists the SKU; a May 2026 owner log reports roughly 6 GB [S02,S05]. A 2024 review is a lead [S15], but its detailed package claims were not independently transcribed/verified here. | Confirm bus width and HBM type first. If 3072-bit and 4 GB stacks, three equivalents give a 12 GB reference configuration. | Ordinary low-density or partly active geometry; no extra functional memory. 24 GB is not supported by current evidence. |
| A30 (GA100, `10de:20b7`) | Official 24 GB, 3072-bit, 933 GB/s and known board PN prefix `699-21001-0205` [S06]. Community research reports differing partition masks, but the interpretation is disputed [S11]. | If additional compatible 8 GB stack equivalents are physically present and usable, 32 or 40 GB scenarios merit checking. | Missing/dummy/defective parts; no independently readable extra addresses. The published capacity-to-width ratio is normal. |
| PG199 / DRIVE A100 | Owner integration account [S12] and community 32 GB configuration reports [S11]. | If four fully populated 16 GB stacks were physically confirmed, 64 GB would be a geometric possibility, not a recovery guarantee. | Actual 8 GB stacks, disabled or defective interfaces, initialization failures, unsupported host/cooling. |

## P2 — controls and lower-priority leads

| Candidate | Evidence and reason | Next observation / caveat |
| --- | --- | --- |
| CMP 100-210 (`1df4`, `1d84`) | Separate owner research describes different board/firmware families [S04,S14]. | Compare labels and density. Existing performance and link restoration do not establish memory expansion. |
| A30X | Official 24 GB HBM2e and 1223 GB/s [S10]. Community negative report [S11]. | Seek ordinary read-only topology and independent package identification. Do not treat 48 GB as likely. |
| A100 40 GB / A100 80 GB | Related products with different density/geometry [S09]. | Controls for product-line inference; no positive hidden-memory result asserted. |
| P100 12/16 GB | Vendor documents proportional capacity and width [S07]. | Negative-style specification comparator, not proof all boards lack additional memory. |
| V100 16/32 GB | Same bus and bandwidth for both vendor configurations [S08]. | Non-identifiability control; don't infer 32 GB from a 16 GB board's bandwidth. |
| Other HBM accelerators (AMD, Intel, Hopper) | Expansion scope; not evidence-backed candidates yet. | Submit vendor spec, compatible density, distinct variant IDs and counterexamples before adding numeric rows. |

## Positive controls (external results, not replicated by this repository)

- CMP 170HX: external community reports 8→64 GB class and 10→40 GB class in software on eligible variants [S03]. A separate 8 GB-labeled subsystem `1586` is reported to reach 32 GB only [S16]; do not merge variants. Reports of higher capacities via hardware work exist, but they are out of project scope.
- CMP 100-100: author reports two 6144→12288 MiB transitions and zero failures for two reported 11264 MiB memory-test runs [S04a]. Unallocated/reserved bytes and complete independent test coverage are not established; physical stack height and fourth site are unknown.
- P104-100: historical owner reports of 4→8 GB GDDR memory [S17], with failures on some boards. Historical product-strategy comparator only; not HBM.

## Manufacturing cohort overlay

Priorities are conditional on available cohort evidence. For each P1/P2 candidate, stratify by independently dated production period, board revision, package identification and known repair history. Compare pre-transition, transition and later production where dates are documented, including null results. See [lot history](lot-history.md). The 2020–22 supply context raises questions but does not justify promoting an otherwise unsupported candidate or assuming all late units have higher density. Collect per-device data in [lot observations](../data/lot_observations.csv).

## How to promote a lead

1. Identify a particular revision (PCI/subsystem IDs, PN, PCB, GPU markings if available).
2. Add a dated source with explicit observed data and distinguish inference.
3. Demonstrate topology/physical part evidence with counter-hypotheses.
4. Seek independent corroboration. Any validated extra capacity is stated in bytes with scope and test coverage; a broader SKU claim requires additional representative data.

No candidate is a buy recommendation, and no hypothetical capacity is a published inventory of installed memory.
