# HBM Anomaly Research

**An open, evidence-first investigation of potentially unaddressed GPU memory.**

[日本語](README.ja.md) · [Theory](docs/theory.md) · [Study design](docs/study-design.md) · [Manufacturing cohorts](docs/lot-history.md) · [Candidate register](docs/candidates.md) · [Validation protocol](docs/validation.md) · [Sources](docs/sources.md) · [Contribute](CONTRIBUTING.md)

**Status: v0.3.0 research framework — 2026-11-25.** This project has not performed its own GPU hardware tests. Its deliverables are sourced comparisons, an explicit physical model, a conditional manufacturing hypothesis, and a protocol for independent observations.

## Research question

Can unusual combinations of advertised memory capacity, effective memory bus width, memory bandwidth, manufacturing lineage and secondary-market behavior identify accelerator variants worth investigating for additional physically populated, functional HBM?

Earlier mining accelerators provide a reason to ask this question. Independent community projects report larger addressable capacities on selected CMP 170HX and CMP 100-100 boards. The relevant question is not whether a related GPU has a larger advertised capacity, but whether *this board revision* has extra populated, healthy, separately addressable memory.

## Four claims, four evidence requirements

| Claim | Evidence needed | What it does not establish |
| --- | --- | --- |
| Extra physical data capacity | Reliable memory-part identification tied to the actual assembly | Health, accessibility, or recoverability |
| Extra functional capacity | Verified distinct, simultaneously resident device data above an exact nominal baseline | All-unit reliability, prevalence, or manufacturing intent |
| Production-cohort association | Comparable dated variants, independent provenance, and negative observations | A supply shortage as the cause |
| Supply-driven substitution | Attributable part/cohort-specific evidence of a change and its reason | The same decision on every related product |

These are separate claims, not a universal ladder: functional testing can establish a storage lower bound before every package is identified, and a documented substitution need not yield healthy extra memory. Price behavior helps prioritize collection; it cannot establish any memory-capacity claim alone.

### Reading order

1. [Physical theory](docs/theory.md): assumptions, units, derivation, and why bandwidth cannot uniquely identify capacity.
2. [Manufacturing cohorts](docs/lot-history.md): conditions under which a qualified substitute may be economical, and what historical sources actually show.
3. [Study design](docs/study-design.md): bounded hypotheses, exact baselines, stopping rules, and separate verdicts.
4. [Candidate register](docs/candidates.md) and [owner protocol](docs/validation.md): choose the next missing observation and submit evidence.

The [Japanese research framework](docs/research-framework.ja.md) connects all four documents. The [call for participants](docs/call-for-participants.md) is ready for existing hardware owners.

## Why manufacturing date matters

The original SKU specification may remain unchanged while qualified components or completed packages vary across production cohorts. NVIDIA's FY2021/FY2022 filings document long lead times, supply commitments and inventory-mismatch risk [S21,S22]. Higher-capacity assembly substitution under shortages is therefore a testable **hypothesis**, not an observed NVIDIA BOM decision. It requires technical qualification and a favorable opportunity-cost comparison. We record historical context separately from individual production dates and physical observations. Compare early, transition and late cohorts rather than treating one failed board as a verdict on the whole SKU. See the [lot history and economic model](docs/lot-history.md), [dated event ledger](data/supply_events.csv), and [empty per-device observation register](data/lot_observations.csv).

## Where to start

| Device | Known or advertised capacity | Research objective | Evidence status |
| --- | ---: | --- | --- |
| CMP 170HX (8 / 10 GB variants) | 8 / 10 GB class | Positive control; community reports 64 / 40 GB class respectively, with variant exceptions | External reports; not tested here |
| CMP 100-100 (GP100) | 6 GiB | Positive control; 12 GiB reported; verify coverage and board differences | External logs, partial coverage |
| **CMP 100-200 (Volta)** | ~6 GB class | Obtain reliable bus width, board IDs, HBM identification and stock logs; 12 GB is a conditional hypothesis | High information priority; capacity recovery unverified |
| **A30 (GA100)** | 24 GB | Identify physical stack/partition topology and distinguish defects from intentional settings | High large-capacity research priority; no recovery established here |
| DRIVE A100 / PG199 | 32 GB class (reported) | Confirm exact variants and topology; document unsuccessful tests as well | Conditional; no recovery established here |
| CMP 100-210 (GV100) | 16 GB class | Compare 1df4 and 1d84 board families; investigate whether different physical densities exist | Performance restoration is not capacity restoration |
| A30X | 24 GB | Compare against A100X; examine whether normal 8 GB stacks fully explain it | Lower priority; negative owner report exists |

See [candidate register](docs/candidates.md) for conditional configurations, counterexamples, and source IDs. These are research priorities, not estimates of success probability. Do not buy hardware solely on this list.

## Why capacity and bandwidth matter

We compare nominal capacity per effective 1,024-data-lane equivalent against explicitly sourced reference densities. A low value is a lead, not a proof. Different stack densities can have the same external width and data rate [S01]. Disabling channels, empty or dummy sites, bad memory, and lower-density parts also explain reduced capacity. Dedicated ECC cells, BAR apertures and host-backed virtual memory must be excluded from extra data-capacity claims. See the [variable definitions, derivation and counterexamples](docs/theory.md).

## Call for independent owners

If you already own a CMP 100-200, A30, PG199, CMP 100-210 or another unusual HBM accelerator, please contribute **even a stock, read-only report**. No hardware purchase or modification is required. We particularly need PCI and subsystem IDs, board part/revision, firmware version, baseline memory and clocks, sources identifying memory packages, and documented manufacturing-date ranges or date codes (not VBIOS dates). Failed tests, ordinary low-density assemblies and null results are equally valuable.

- Use the **Hardware observation** issue template for read-only data.
- Use the **Bounded study proposal** template to specify the target, baseline, thresholds and stopping rules before collecting outcomes.
- Use the **Replication result** template for an already performed, independently designed test.
- Use the **New candidate / source correction** template for a source or a contradictory observation.
- Use the **Historical supply / lot evidence** template for sourced production change or allocation history.
- Use the **Market observation** template for dated listings or actual transactions; distinguish the two.

A new capacity displayed by a driver does not establish usable memory. Independent address-sensitive write/read tests, coverage accounting, error telemetry and repeatability are essential. See [validation](docs/validation.md). Do not expose serial numbers, UUIDs, hostnames, credentials, personal data, copyrighted firmware dumps or security exploit details in public issues.

## Reproduce the desk analysis

Requires Python 3.10+; standard library only. No GPU, driver, administrator privilege, network or device writes needed.

```sh
python3 tools/screen.py --input data/devices.csv
python3 tools/screen.py --input data/devices.csv --format csv
python3 -m unittest discover -s tests -v
```

Unknown and hypothetical bus widths are not silently converted into verified values. External community widths are calculated and explicitly labeled separately from vendor specifications. The screening utility calculates descriptive ratios only; it does not discover hardware capacity or estimate unlock probability. See [data dictionary](data/README.md).

## Project boundaries

This is independent research, not affiliated with NVIDIA or any other manufacturer. All measurements so far are external and attributed. No bypass code, firmware modification scripts, privileged register writes, fuse programming, overvolting or destructive experiment instructions are distributed here. Report potential security vulnerabilities privately to the relevant vendor. Respect ownership, warranties, applicable law and third-party licenses.

The goal is a reproducible negative result or positive result per identifiable variant — not a speculative list marketed as hidden VRAM. Contributions and corrections are welcome. Original repository content is MIT-licensed; external material retains its own rights.
