# Cross-vendor HBM research priorities (v0.5.0)

> **Archive v0.5.0; not the current assessment.** [Current analysis](current-ranking.md) · [Document index](README.md)

[日本語](cross-vendor-ranking.ja.md) · [Home](../README.md) · [Source register](sources.md) · [CSV](../data/cross_vendor_leads.csv)

2026-11-26. **Desk research only; no original hardware tests.** The prior v0.4.0 prediction list was conditioned on discovery through NVIDIA CMP. That is a selection bias, not a demonstrated property of HBM technology. The new lead order is cross-vendor and ranks the value of a concrete capacity-related suspicion to investigate, rather than measured probabilities of recovery. Physical excess, health, reversible access and supply causation are different claims.

| Priority | Candidate | Nominal capacity | Conditional total / physical finding | Why suspicious | Strongest alternative / limitation |
| ---: | --- | --- | --- | --- | --- |
| 1 | Intel GPU Max 1100 | 48 GB | one physically present disabled stack; 64 GB total only if that stack is 16 GB | Official datasheet identifies four physical stacks, three enabled 16 GB stacks; inactive position varies. | Permanent disable and possible yield harvesting; no evidence of a healthy or recoverable fourth stack. |
| 2 | NVIDIA CMP 100-200 | ~6 GB class | 12 GB class if larger assembly exists | Low-capacity Volta mining SKU and prior CMP capacity-limit precedent. | Actual width/density unknown; normal low-density or partially active assembly. |
| 3 | NVIDIA A30 | 24 GB | 32 or 40 GB class if additional 8 GB-class regions populated | Reduced GA100 memory configuration permits shared-package hypothesis. | Ordinary 24 GB population or defective excluded regions; compute recovery is not memory recovery. |
| 4 | NVIDIA DRIVE A100 / PG199 | 32 GB class reported | 64 GB class if four 16 GB-class stacks populated | OEM-specific GA100 configuration and possible package reuse. | Ordinary four-by-8 GB assembly; count/density unverified. |
| 5 | AMD Instinct MI50 16 GB | 16 GB | 32 GB class if four 8 GB-class stacks populated | Vendor lists 16 and 32 GB MI50 with the same 4096-bit interface and 1 TB/s bandwidth; known 32 GB assembly in same SKU family. | Ordinary 4 GB stacks explain 16 GB; FRU-name mismatch is not a stock access restriction; refurbished boards may differ. |
| 6 | AMD RX Vega 56 / 64 8 GB | 8 GB | 16 GB class if two 8 GB-class stacks populated | Common PCB with 16 GB Vega Frontier Edition; 2017 documented HBM2 production expansion and reported supply/yield difficulties. | Teardown reports different soldered packages; normal two-by-4 GB assembly; high-density HBM also scarce. |
| 7 | NVIDIA CMP 100-210 | 16 GB class | 32 GB class only if higher-density assembly exists | Distinct board/firmware families provide a concrete cohort axis. | Investigated 1df4 unit has ordinary 16 GB V100 origin; performance improvement is not capacity gain. |
| 8 | AMD / XFX BC-160 | 8 GB | 16 GB class only if two 8 GB-class stacks populated | 2021 Navi 12 HBM2 mining product; relevant market context. | 8 GB / 2048-bit ordinary; official V520 comparator also 8 GB; no verified shipping 16 GB Navi 12 counterpart in reviewed sources. |
| 9 | NVIDIA A30X | 24 GB | 48 GB class if three 16 GB-class stacks and partial exposure | Special converged HBM2e SKU and hypothetical density substitution. | Ordinary 8 GB-class HBM2e explains capacity/bandwidth; width/density not established. |

Intel #1 is a **documented physical-excess case**, not a prediction that its extra memory is healthy. The five original NVIDIA predictions retain their relative ordering for traceability. AMD and Intel leads are inserted by comparative evidence and ordinary alternatives; the exact lower-order placements are editorial and can change. No positive rank weight from historical prices is included, because comparable market series remain missing. All capacity scenarios other than the stated documented population facts are conditional, not predictions of recoverable bytes. No new software recovery has been demonstrated here.

## Intel: strongest new physical lead

The [official datasheet, document 817799, §2.4, printed p.12](https://cdrdv2-public.intel.com/817799/817799_Intel%20Data%20Center%20GPU%20Max%201100%20Datasheet_Rev_1_0.pdf) reports four physical HBM stacks, three enabled 16 GB stacks, and one permanently disabled stack whose position can vary by card [S39]. If the fourth is also 16 GB, this is a nominal 64 GB physical assembly with 48 GB active. The text does not independently identify the fourth part number/density. The varying disabled position is compatible with yield harvesting, but does not establish the reason, the fourth stack's health, or any reversible mechanism. Do not treat BAR2's 64 GB aperture as capacity evidence; the same section distinguishes it. The manufacturer's permanent-disable description is substantial negative evidence for practical recovery, even though it is positive evidence of physical surplus. This is a direct counterexample to an NVIDIA-only physical-population model.

ARK gives 1228.8 GB/s and a 1024-bit interface entry [S40]; the datasheet's topology is three enabled stacks, and its p.11 bandwidth line appears inconsistent with ARK. Do not silently substitute the ARK interface entry as the aggregate active width, or use that inconsistency to infer capacity. Use the topology statement as the evidence.

Max 1350 (announced 96 GB, two compute stacks) is a separate watchlist hypothesis: 128 GB if eight 16 GB parts are physically installed and two are inactive. Neither the full physical population nor healthy extra memory is documented for 1350. Intel removed this SKU from its lineup in April 2023 [S41,S56]; actual production/availability remains uncertain. It is not appropriate to import the Max 1100 topology as a measured fact for 1350.

## AMD: same marketing SKU, genuine density options, and real historical restriction

* **MI50 16 GB (#5):** AMD lists both 16 and 32 GB with the same 4096-bit and 1 TB/s interface, 60 CUs [S42]. Ordinary different-density stacks are sufficient; owner reports support that ordinary explanation [S43]. A 2026 owner reported a board with 16 GB FRU name and ~32 GiB already exposed by the driver [S44]. This is a useful provenance/metadata anomaly, not capacity recovery or proof that an original 16 GB SKU contained 32 GB. The prediction concerns authentic low-capacity units with actually higher-density parts; refurbishing and stale FRU strings are alternatives. Compare original OEM assemblies. Radeon Pro VII 16 GB remains a sibling watchlist rather than an independent positive.
* **RX Vega 56/64 (#6):** RX Vega 64 8 GB has 2048-bit and 484 GB/s [S45]. A contemporaneous board analysis reports a common PCB with 16 GB Frontier Edition but different soldered packages [S46]; physical analysis of Frontier Edition reports two 8 GB stacks [S48]. Samsung expanded 8 GB HBM2 production in July 2017 [S47], while contemporaneous reports describe Vega packaging/supply difficulty [S49]. The 16 GB scenario assumes a qualified larger package was allocated to an 8 GB SKU and retained a healthy excluded subset. No such cohort is established. High-density parts could themselves be scarce, so the direction of substitution is not determined. Study actual package markings by production period rather than board appearance.
* **BC-160 (#8):** A real 2021 HBM2 mining product, reported as 8 GB / 2048-bit [S50]. The official V520 also has ordinary 8 GB HBM2 / 2048-bit / 512 GB/s [S51]. A secondary article mentions up to 16 GB for Navi 12 but does not establish a shipping 16 GB product or BC-160 compatibility [S52]. The conditional 16 GB scenario is weak. Mining specialization is a research motive, not a capacity anomaly.

### Historical positive control outside HBM: AMD RX 480 4 GB

AMD announced 4 GB and 8 GB GDDR5 SKUs in June 2016 [S53]. TechPowerUp bought a retail 4 GB card, identified eight 8 Gbit chips, and reported 8 GB operation and benchmarks [S54]. A contemporary launch-day report attributes the early over-populated cards to component sourcing difficulty [S55]. The physical and functional report is much stronger than the causal attribution; no internal procurement record is available. This is a cross-vendor precedent for a capacity-limited launch cohort and makes the supply-substitution hypothesis historically motivated. It is not an HBM result and not proof that every RX 480 4 GB unit is equivalent.

## Other architectures and exclusions

| Device | Observed comparison | Interpretation |
| --- | --- | --- |
| Huawei Ascend 910B4 | CSET reports 32 GB / 800 GB/s vs 64 GB / 1600 GB/s in 910B1–3 [S57] | Candidate for physical topology research: 64 GB conditional if all four 16 GB stacks physically present. A normal two-stack assembly explains both values; physical population unverified. NPU, separate from GPU ranking. |
| AMD MI300A vs MI300X | 128 GB vs 192 GB, equal 5.3 TB/s-class bandwidth; eight real stacks each in published topology [S58] | Known density difference. No positive reason to infer higher-density parts in MI300A from bandwidth. |
| AMD MI300A runtime allocation | AMD documents default 96 GiB HIP allocation of advertised 128 GiB unified HBM [S59] | Documented policy limit, not hidden physical memory beyond the advertised capacity. |
| Intel Gaudi, Biren, MetaX, Iluvatar CoreX, Cambricon, HBM FPGAs | Further source survey required | Not excluded; no sufficiently specific evidence assessed here to rank. Different device classes must be clearly labeled. |

## How this changes the method

Use three evidence routes: (1) physical topology statements even when the capacity-to-bandwidth ratio looks ordinary; (2) capacity-specific configuration discrepancies and known higher-density siblings; (3) sourced manufacturing transitions, shortage timing and compatible package reuse. Do not infer healthy memory from physical presence, a permanent-disable flag, an EEPROM label, or a shared PCB. The AMD RX 480 example supports the mechanism across manufacturers, not the assumption that it occurred on any particular HBM SKU. Search part numbers, PCNs, official datasheets, original board photographs and contemporaneous supply coverage across vendors. Treat an unobserved lot as unknown; do not invent a favorable production date.

See the [historical NVIDIA-only forecast](candidates.md) for v0.4.0 assumptions and the [ranking method](ranking-method.md) for comparative reasoning. The expanded list is non-exhaustive, lacks representative samples and has no calibrated recovery probability or verified price trend. A negative result on one known lot does not reject every lot, but lack of data is not positive evidence. All new sources [S39–S59] are in the [source register](sources.md).

