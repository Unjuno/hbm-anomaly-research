# Forecasting from capacity and bandwidth

[日本語](diagnostic-inference.ja.md) · [Home](../README.md) · [Candidates](current-ranking.md) · [Sources](sources.md)

## What made 170HX suspicious?

| Published observation or part model | Capacity | Width | Bandwidth |
| --- | ---: | ---: | ---: |
| 2023 170HX review (S87) | 8 GB class | 4096 bit | Measured 1166–1355 GB/s |
| Four 2 GB / 2.0 Gb/s HBM2 (S93) | 8 GB class | 4096 bit | 1024 GB/s ceiling |
| Four 2 GB / 2.4 Gb/s (sensitivity case) | 8 GB class | 4096 bit | 1228.8 GB/s ceiling |
| Four 8 GB / 3.2 Gb/s HBM2E (S01) | 32 GB class | 4096 bit | 1638.4 GB/s ceiling |

**Inference:** the listed low-density speed conditions struggle to fit capacity and throughput together. Faster, denser parts with partial exposure could explain the observation. Unlisted low-density parts, over-rated operation and benchmark accounting including cache are alternatives.

## The bound

| Symbol | Definition | Unit | Assumption / type |
| --- | --- | --- | --- |
| $c_i$ | Ordinary-data capacity of real stack i | byte | Positive scalar |
| $b_i$ | Bandwidth ceiling of that stack | byte/s | Nonnegative scalar |
| $\rho_{\max}$ | Maximum bandwidth/capacity over admitted part and speed conditions | s$^{-1}$ | Positive finite scalar |
| $B$ | Actual DRAM bandwidth | byte/s | Nonnegative scalar |
| $C_p$ | Physical capacity (sum of all $c_i$) | byte | Positive scalar |
| $n,i$ | Real stack count and index | 1 | Positive integers, $1\le i\le n$ |

Assume every populated part satisfies an admitted condition. By definition, $b_i\le\rho_{\max}c_i$ for each stack. Actual aggregate DRAM bandwidth cannot exceed the sum of the ceilings, so

$$B\le\sum_{i=1}^n b_i\le\rho_{\max}\sum_{i=1}^n c_i=\rho_{\max}C_p.$$

Divide by the positive maximum ratio:

$$C_p\ge B/\rho_{\max}.$$

Units: byte/s divided by s$^{-1}$ gives bytes. If a justified lower bound on actual DRAM throughput exceeds the ordinary-capacity ceiling, the ordinary model is excluded within that part set. An incomplete catalog does not establish physical excess.

## Apply it to other GPUs

MI50 16 GB at about 1 TB/s fits four 4 GB, 256 GB/s parts. A30X 24 GB at 1223 GB/s fits three 8 GB, 3.2 Gb/s parts. CMP 100-200's approximately 6 GB lacks matched width and bandwidth. Record these differences in the [candidate list](current-ranking.md) and combine with [manufacturing history](historical-context.md).

## Details

[Part ledger](../data/hbm_part_constraints.csv) · [Performance ledger](../data/performance_gap_observations.csv) · [Full capacity and width derivations](capacity-constraints.md)

Full technical record: [v0.11 snapshot](https://github.com/Unjuno/hbm-anomaly-research/blob/36ac571449d3a26c44da46afb06fda97093e6e47/docs/diagnostic-inference.md). Includes measurement conditions, exact capacity conventions, uncertainty and full sensitivity analysis.
