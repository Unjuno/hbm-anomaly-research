# Candidate hypotheses

[日本語](current-ranking.ja.md) · [Home](../README.md) · [Sources](sources.md)

The capacity scenarios are **conditional physical totals**, not recovered capacity. The first four are the current research focus; the remaining rows are comparison leads. This is not an ordering of recovery probability.

| Product | Nominal capacity | Conditional total | Reason and unresolved alternative | Source IDs |
| --- | --- | --- | --- | --- |
| CMP 100-200 | ~6 GB | 12 GB class | Three ordinary 2 GB HBM2 parts fit capacity; their listed grade gives a 768 GB/s ceiling if three fully active stacks are used. Check same-unit width and rate. | S05, S93, S95 |
| A800 40GB Active | 40 GB | 48 / 80 GB class | 2022 inventory charges and alternate A800 sales motivate checking package reassignment. Ordinary five-by-8 GB also fits. | S71, S96, S99 |
| MI50 16 GB | 16 GB | 32 GB class | Later 32 GB addition provides a concrete cohort comparison. Four 4 GB parts can explain the ordinary 1 TB/s rating. | S38, S80, S101, S103, S104 |
| RX Vega 56/64 | 8 GB | 16 GB class | Compare suppliers/packages across late 2017–2018. Ordinary two-by-4 GB fits; Frontier Edition uses a different installed package. | S45–S49, S100 |
| H100 SXM5 64 GB HBM2e | 64 GB | 80 / 96 GB class | Official documents also list a 94 GB HBM2e SKU. Exact 64 GB population and width remain unknown; four 16 GB parts suffice. | S60, S61, S64, S110 |
| DRIVE A100 / PG199 | 32 GB class (reported) | 64 GB class | Original OEM package identity remains unresolved. Ordinary four-by-8 GB and later board conversion are alternatives. | S12, S98 |
| A30 | 24 GB | 32 / 40 GB class | Look for additional inactive HBM. Three 8 GB parts fit capacity and width; compute recovery is not capacity evidence. | S06, S34, S35 |
| H100 SXM5 80 GB | 80 GB | 96 GB class | Determine whether site six contains DRAM or support material. Five enabled stacks explain 80 GB. | S62, S63, S106 |
| CMP 100-210 | 16 GB class | 32 GB class | Compare density across original board families; reported performance improvements fit ordinary 16 GB. | S04, S08, S14, S33 |
| BC-160 | 8 GB (reported) | 16 GB class | Ordinary 8 GB RDNA/HBM products predate this mining board. No compatible 16 GB donor established. | S50–S52, S105, S109 |
| A30X | 24 GB | 48 GB class | Three 8 GB HBM2E stacks can explain 1223 GB/s; planned in 2021. Actual width and parts remain unresolved. | S01, S10, S97 |

## Known reference cases

| Product | Observation or report |
| --- | --- |
| CMP 170HX | External 8→64 GB-class and 10→40 GB-class reports, variant-specific (S03, S19). |
| CMP 100-100 | Owner report of 6→12 GB-class capacity (S04a). |
| Intel Max 1100 | Vendor documents four physical stacks, three enabled (48 GB), one permanently disabled; fourth-stack density and health unknown (S39). |
| AMD RX 480 | Retail 4 GB GDDR5 card with 8 GB population and reported operation (S54). |

## Next questions

First find same-unit width, bandwidth and component identity for CMP 100-200. For A800, MI50 and Vega, use the [manufacturing history](historical-context.md) to identify parts and package groups.

[Full 26-entry register](../data/current_ranking.csv) · [Inference method](diagnostic-inference.md) · [Contribute](call-for-participants.md)

Full technical record: [v0.11 snapshot](https://github.com/Unjuno/hbm-anomaly-research/blob/36ac571449d3a26c44da46afb06fda97093e6e47/docs/current-ranking.md).
