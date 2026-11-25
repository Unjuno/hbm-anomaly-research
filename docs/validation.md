# Reproducible validation protocol

[Home](../README.md) · [Study design and decisions](study-design.md) · [Contribute](../CONTRIBUTING.md)

## Scope and safe baseline

Use hardware you own or are authorized to inspect. Existing stock-card observations are the priority. No purchase, disassembly, device modification, privileged register access or firmware image is required. Do not test production hosts. Use ordinary cooling, vendor-rated power and manufacturer-approved configuration. A test must never target another user's workloads.

Before interpreting new observations, freeze the target revision/cohort, exact baseline, material increase, environment, coverage and stopping criteria in a dated [study record](study-design.md). Classify physical excess, functional excess, cohort differences and supply causation separately. An experiment can support one while leaving the others unresolved.

### A. Read-only inventory

On Linux with an existing working driver, the following commands request ordinary metadata only; no root is required for the intended fields. A command can fail on an unsupported driver or environment; report the failure rather than forcing it. `nvidia-smi` memory fields are driver-reported, not physical measurements. Commands assume pciutils and an installed NVIDIA driver.

```sh
lspci -nn -d 10de:
nvidia-smi --query-gpu=index,name,pci.bus_id,memory.total,driver_version,vbios_version --format=csv
nvidia-smi --query-gpu=index,clocks.mem,temperature.gpu,power.draw --format=csv
```

Before sharing, replace PCI bus locations with stable local labels if sensitive; never include UUID, serial, hostname or other personal identifiers. Record the PCI device and subsystem IDs from the card's existing documentation/metadata, manufacturer board PN, revision, visible package markings if already available, date code, whether stock/modified/virtualized, firmware version, OS/kernel, driver, MIG/vGPU status, ECC, total/free memory and any warnings. If the cooler has not already been safely removed by a qualified owner, do not remove it for this project. Mark unknown fields unknown. Attach cropped photos only if you have the right to share them.

### A2. Production cohort information

Use [lot history](lot-history.md) and the [per-device schema](../data/lot_observations.csv). Identify the manufacturing stage to which a date refers, source, raw redacted code, date range and precision. Distinguish package, PCB and final board assembly from sale, firmware build and observation dates. Do not derive a date code convention without a source. Record repair or rework history, acquisition channel category and independent ownership; omit or redact sensitive labels. Compare documented early/transition/late cohorts, not just multiple units from one seller. Historical corporate supply events are recorded separately and cannot prove a specific lot substitution.

### B. Capacity verification criteria (for existing independent experiments)

A report that changes the capacity label is a *telemetry observation*, not a pass. If an owner has already independently performed a lawful test, collect:

- baseline and final reported capacity in exact MiB or bytes, with reserved/free/allocatable memory clearly separated; establish that the predeclared baseline and tested bytes use the same user-data accounting basis, excluding dedicated parity cells and spares;
- the exact device identifier and revision, driver/runtime/test software and version (or hash), ECC mode, configured clocks, power limit, temperature, allocation sizes, offsets/coverage, pattern seeds, repetitions, runtime and error counts;
- a test of distinct simultaneously resident device-memory addresses spanning baseline and added regions, using address-dependent patterns and re-reading earlier regions after writing later ones, so an address alias cannot masquerade as added memory;
- identify allocation API/backend and device residency controls; a device pointer or successful allocation alone does not exclude managed-memory migration, mapped host memory or other-device storage; count untested/reserved ranges and avoid claiming complete physical address coverage from virtual allocation coverage alone;
- check independent patterns and seeds, multiple passes, relevant ECC/Xid/driver errors and behavior after cold restart; distinguish failure to initialize or allocate from data mismatch. State the predeclared handling of corrected errors and unavailable telemetry. A no-error run over a subset only supports that subset.

Use documented cache/coherence behavior to ensure the checked values exercise the intended memory; a cache-resident result alone cannot establish HBM coverage. Record the data set size and the method's limits. Addressable does not mean healthy: defective cells can still respond to addresses. A passing test establishes observed functionality only over its stated coverage, patterns, time and conditions. See the [capacity definitions](theory.md) and the [NVIDIA CUDA memory API](https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/group__CUDART__MEMORY.html) for allocation distinctions.

No command here changes device settings. Use appropriate vendor-supported diagnostics or a test you can audit. No modification is required to contribute. Do not run unknown binaries or share exploit chains. The project does not prescribe fault injection, fuse changes, flash or hardware rework.

### C. Per-device functional verdict

Apply these labels to H-F, the functional experiment, with the exact scope recorded. Use the separate [claim decision table](study-design.md) for physical presence, cohort association or manufacturing cause.

| Verdict | Required evidence |
| --- | --- |
| PASS (extra verified under stated conditions) | Exact verified distinct resident capacity reaches the predeclared baseline plus material-increase threshold; reviewed read/write, alias and residency controls, zero data mismatches, and the predeclared repetition/error requirements. Report bytes, duration and limits. |
| FAIL (experiment-specific) | A reproducible reviewed data failure defeats the defined experiment under its documented conditions, or an independently substantiated physical upper bound makes the required capacity impossible. State which applies; this does not establish that other configurations or units fail. |
| UNCERTAIN | Only driver enumeration, ambiguous component ID, failed initialization, allocation limits, partial or unreviewable tests, or missing data. |

For replication, target at least two independently tested physical units of the same relevant variant. Record unsuccessful results and variant differences. Two owners can share a donor lot or method bias; document acquisition and analytical dependencies. Initial sample size is for reproducibility, not population inference; no estimate of the proportion of good units is justified from two owners. For a prevalence claim, specify sampling frame, representative sampling, inclusion/exclusion, dependence treatment and confidence method first. Do not exclude failures or stop a predeclared comparative collection on a favorable result alone. Report the closing date, planned/actual counts and incomplete coverage.

### D. Uncertainty and comparisons

Distinguish decimal GB from GiB, theoretical bandwidth from measured bandwidth and PCIe from HBM bandwidth. Record actual rather than assumed transfer rates, repeat measurements in the same workload and configuration, and give sample count, median and range. Calculate a combined measurement uncertainty only when calibration/repeated data and correlations are available. Retain raw redacted logs with SHA-256 if possible. An independent reviewer should reproduce arithmetic and identify any contradictory result before claims are promoted.

For categorical uncertainties such as an unidentified memory part or unverified residency, report the unresolved alternative directly. Do not replace it with an invented numerical error bar or coverage factor. An exact byte total does not resolve these evidential gaps.

**ERROR CHECK:** Telemetry is distinct from tested capacity; physical presence is distinct from observed function; negative outcomes retain their unit/environment scope; two devices do not establish prevalence; no hardware experiment is performed by this document.
