# Nominal geometry screen

[Hypothesis ranking](candidates.md) · [Method](ranking-method.md) · [Data](../data/devices.csv)

Generated from the v0.4.0 configuration table. Prediction-rank labels are supplied by the separate hypothesis register; this calculation does not derive the ranking. Unknown widths remain unknown.

| Device | Role / prediction rank | Width evidence | GB/1024 bit | BW/GB (nominal) | Pin rate (Gb/s) | q | Status |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| CMP 170HX 8GB | control | community_report | 2 | 186.625 | 2.91602 | 0.25 | strong_relative_mismatch |
| CMP 170HX 10GB | control | community_report | 2 | 155.5 | 2.42969 | 0.25 | strong_relative_mismatch |
| CMP 100-100 | control | unknown | — | — | — | — | missing_width |
| CMP 100-200 | prediction_rank_1 | unknown | — | — | — | — | missing_width |
| CMP 100-210 | prediction_rank_4 | unknown | — | — | — | — | missing_width |
| NVIDIA A30 | prediction_rank_2 | vendor | 8 | 38.875 | 2.42969 | 1 | no_relative_mismatch |
| NVIDIA A30X | prediction_rank_5 | unknown | — | 50.9583 | — | — | missing_width |
| DRIVE A100 PG199 | prediction_rank_3 | unknown | — | — | — | — | missing_width |
| Tesla P100 PCIe 12GB | reference | vendor | 4 | 45.75 | 1.42969 | 1 | no_relative_mismatch |
| Tesla P100 PCIe 16GB | reference | vendor | 4 | 45.75 | 1.42969 | 1 | no_relative_mismatch |
| Tesla V100 PCIe 16GB | reference | vendor | 4 | 56.25 | 1.75781 | 1 | no_relative_mismatch |
| Tesla V100 PCIe 32GB | reference | vendor | 8 | 28.125 | 1.75781 | 2 | no_relative_mismatch |
| A100 40GB PCIe | reference | unknown | — | 38.875 | — | — | missing_width |
| A100 80GB SXM | reference | unknown | — | 25.4875 | — | — | missing_width |
| A100X | reference | unknown | — | 25.4875 | — | — | missing_width |
| AX800 | reference | unknown | — | 25.4875 | — | — | missing_width |

Nominal labels only; missing widths remain missing. Flags are descriptive, not predictions.
