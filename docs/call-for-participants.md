# Help improve the HBM predictions

[日本語](call-for-participants.ja.md) · [Current ranking](current-ranking.md) · [Sources](sources.md) · [Contributing](../CONTRIBUTING.md)

**Can a specific accelerator or production lot contain ordinary-data HBM beyond its advertised capacity?** This project publishes explicit, unverified predictions from specifications, product history and manufacturing constraints. Its main output is the reasoning and ranking. Physical presence, memory health and practical accessibility are separate claims.

We welcome **a useful source or counterexample**, as well as observations from people who already own relevant hardware. You do not need a GPU, a completed experiment or a positive result to contribute.

## Start with one piece of evidence

[Open a quick evidence issue](https://github.com/Unjuno/hbm-anomaly-research/issues/new?template=quick-evidence.md). Four things are enough to start:

1. The product or hypothesis the information concerns.
2. What the source or observation actually says.
3. A source URL and section, or an existing log or photo with identifiers removed.
4. What this changes in the prediction, and what remains unknown.

Unknown fields are acceptable. A dated official document, a part-number mapping, an ordinary low-density configuration or a reason to reverse two candidates can be more useful than a large collection of unexplained screenshots. A cited source does not necessarily endorse our prediction.

For a detailed prediction, use [New candidate / prediction / source correction](https://github.com/Unjuno/hbm-anomaly-research/issues/new?template=new-candidate.md). Existing owners can use [Hardware observation](https://github.com/Unjuno/hbm-anomaly-research/issues/new?template=hardware-observation.md); its extended fields are optional for an initial report.

## Which missing facts would help most?

The [current ranking](current-ranking.md) gives the reasoning, evidence status and competing explanations. The requests below describe information that could change it; they are not claims that additional capacity exists.

| Target | A useful next contribution | What it could distinguish |
| --- | --- | --- |
| H100 SXM5 64 GB HBM2e | Exact physical-board identity and existing documentation or readable markings for its HBM assembly | A real 64 GB board versus a virtual allocation; ordinary population versus a larger populated assembly |
| CMP 100-200 | A traceable roughly 6 GB-class unit with part-number or density evidence | Ordinary low-density memory versus partial exposure of a larger assembly; bandwidth alone cannot identify density |
| A30, PG199 / DRIVE A100, A800 40GB Active, H100 SXM5 80 GB | A part-number mapping or existing package evidence for an identified revision | Absent or dummy sites versus additional real HBM; nominal family resemblance is insufficient |
| AMD MI50 16 GB | Memory-part evidence tied to an identified unit, with repair or rework history if known | Normal 16 GB construction versus a higher-density assembly; a stale label on an already 32 GB card is not a capacity recovery |
| Intel GPU Max 1100 | A direct identification of the disabled fourth stack's density or a document clarifying its status | The documented inactive stack's size and condition; Intel's permanent-disable statement is not evidence of recoverability |
| H20 / MI308 supply watch | Public evidence identifying the reused material, destination product and manufacturing stage | A product-specific substitution versus resale, an unrelated material reuse or an accounting event |

## Existing owners: start with information you already have

Product name, nominal capacity, board part number, existing driver-reported capacity with units, stock/modified/unknown status and an observation date are useful. Add driver/runtime and physical-versus-virtual context when known. An already available memory-part marking or photo is especially valuable. Do not infer stack density from bus width or a visible package outline alone.

No purchase, disassembly, firmware change, clock change or driver replacement is needed. NVIDIA, AMD and Intel owners can use information already available through their installed tools or documentation. The [owner protocol](validation.md) is an optional reference for interpreting more detailed observations; completing it is not an entry requirement.

Keep manufacturing stages separate: an HBM date code, package date, board assembly date, firmware build date and purchase date do not mean the same thing. Record the source and precision of any date rather than guessing a lot from it.

## Negative and uncertain evidence are welcome

| Observation | What it supports | What it does not establish |
| --- | --- | --- |
| The driver reports the advertised capacity | The current exposed capacity under that configuration | That no extra physical HBM exists |
| All relevant ordinary-data memory components are identified and their total matches the nominal capacity | An ordinary physical configuration for that unit, if identification and coverage are complete | That every other revision or lot has the same construction |
| A larger real memory assembly is identified | Physical excess for the identified unit, subject to correct part identification | That the extra region is healthy or accessible |
| Initialization or allocation fails | Failure under the reported environment | Absence of extra components or permanent failure in every environment |
| An existing controlled read/write experiment reports extra resident capacity | Only the tested result under its stated scope; the [interpretation criteria](validation.md) matter | Universal health, all-lot prevalence or the manufacturer's reason for the configuration |

Retain ordinary, contradictory and incomplete cases. Mark a finding **unknown** when it cannot distinguish the competing explanations. Do not promote a display change into a functional result.

## Share only the evidence needed

Remove serial numbers, UUIDs, hostnames, personal details and other identifiers before posting. Share only material you are entitled to publish. Public links, concise excerpts within their rights, redacted observations and your own reasoning are enough; proprietary firmware or other vendor binaries are not needed.

The most useful contribution answers: **Which premise of this prediction changes because of this evidence?**
