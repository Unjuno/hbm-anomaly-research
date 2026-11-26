# HBM Anomaly Research

[日本語](README.ja.md) · [Document index](docs/README.md)

**Forecasting GPUs with physically installed HBM beyond their advertised capacity, using performance, component specifications and manufacturing history.**

## The starting point: CMP 170HX

A 2023 first-person review reported 4096-bit memory and 1166–1355 GB/s measured throughput on an 8 GB-class CMP 170HX. Four published 2 GB HBM2 parts at 2.0 Gb/s would provide at most 1024 GB/s. A faster, larger memory population with partial exposure could explain that mismatch. [Analysis and sources](docs/diagnostic-inference.md)

## Current research focus

| Product | Why investigate it? |
| --- | --- |
| **CMP 100-200** | About 6 GB: look for same-unit width and bandwidth to test the same type of mismatch. |
| **A800 40GB Active** | Late-2022 inventory and sales disruption motivate checking completed-package reassignment. |
| **AMD MI50 16 GB** | Compare original 16 GB packages before and after the 32 GB variant was added. |
| **AMD RX Vega 56/64** | Investigate supplier and package changes around late 2017–2018. |

**[All 11 hypotheses and capacity scenarios →](docs/current-ranking.md)**

These are research hypotheses, not independently verified hardware results or guarantees of usable extra capacity.

## Research notes

- [Theory: capacity and bandwidth](docs/diagnostic-inference.md)
- [Manufacturing history: when and why substitution might occur](docs/historical-context.md)
- [Candidate CSV](data/current_ranking.csv) · [Sources](docs/sources.md) · [Technical notes and archive](docs/README.md)

[Contribute evidence or counterexamples](docs/call-for-participants.md) | [MIT License](LICENSE)

<sub>v0.12.0 · 2026-11-27 · Public-source research</sub>
