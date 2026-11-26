# Manufacturing history and lot differences

[日本語](historical-context.ja.md) · [Home](../README.md) · [Candidates](current-ranking.md) · [Sources](sources.md)

Look for **periods when allocating a larger assembly to a smaller-capacity product could be rational**. Three concrete historical leads stand out.

## A800 / later GA100: sales-channel changes

For the quarter ended October 2022, NVIDIA reported a USD 702m inventory charge mainly related to lower China Data Center demand. Its November 18 filing described alternate A800 sales (S96). ELSA announced Japanese handling of A800 40GB Active on November 2, 2023 (S99).

**Prediction:** if larger packages were reassigned, some later low-capacity configurations should map to earlier package identities. Ordinary 40 GB fits; the 2022 A800 and later Active are distinct SKUs.

## MI50: addition of a capacity variant

AMD announced MI50 16 GB on November 6, 2018. An AMD statement published October 15, 2019 explains the 32 GB addition as a response to customer demand (S103, S104).

**Prediction:** compare original 16 GB packages around that introduction for evidence of denser common parts. A legitimate 32 GB outlet and contemporary 4 GB HBM2 remain alternatives (S101).

## RX Vega: late-2017 supply changes

Samsung announced an 8 GB HBM2 expansion plan in July 2017; SK hynix announced a Q4 supply plan in October (S47, S100).

**Prediction:** investigate supplier, density and part differences among original RX packages from late 2017–2018. Expansion plans are not surplus inventory, and Frontier Edition used a different installed package (S46).

## Other important transitions

| Period | Event and implication |
| --- | --- |
| 2020 | Samsung planned continued 8 GB supply alongside new 16 GB HBM2E. Do not assume lower density disappeared (S92). |
| 2021–22 | CMP quarterly revenue fell from USD 266m to 105m to 24m before the Merge. Finished-stock resale is an alternative (S95). |
| 2023 | TSMC documented CoWoS constraints. Loose-part substitution and completed-package reassignment are different routes (S83). |
| 2023–24 | Intel/Altera HBM2-dependent FPGA discontinuance notices. Last orders and discontinuation are alternative supply responses (S107, S108). |

**Cohort rule:** distinguish HBM manufacture, package assembly, product allocation, VBIOS changes and sale. Compare the stage that was still changeable.

[43-event ledger](../data/supply_events.csv) · [11-candidate history assessments](../data/history_assessments.csv) · [Detailed manufacturing model](manufacturing-causality.md)

Full technical record: [v0.11 snapshot](https://github.com/Unjuno/hbm-anomaly-research/blob/36ac571449d3a26c44da46afb06fda97093e6e47/docs/historical-context.md).
