# Using historical context to identify manufacturing routes and cohorts

[日本語](historical-context.ja.md) · [Current assessment](current-ranking.md) · [Candidate CSV](../data/history_assessments.csv) · [Event ledger](../data/supply_events.csv) · [Manufacturing causes](manufacturing-causality.md) · [Sources](sources.md)

**v0.11.0 — 2026-11-26 JST. Documentary forecasts; no independent hardware measurements.**

## 1. What advanced

**Three distinct routes became more specific: later GA100 market reassignment, MI50 capacity variants, and Vega-era supply expansion plans.** Relevant events and decisions still changeable at those dates matter more than a shared manufacturer or general semiconductor shortage.

History can update plausibility without hardware, but the proposition must be explicit. **A motive for reassignment, a useful period for comparing parts, and evidence of extra physical HBM are different outcomes.** New sources mainly advance the first two; capacity, bandwidth and part comparisons connect them to the third. The similarity-based tiers withdrawn in v0.10 remain withdrawn.

## 2. NVIDIA in late 2022: a concrete reassignment motive

**Fact.** For the period ended 2022-10-30, NVIDIA reported a USD 702 million inventory charge, largely related to lower China Data Center demand: 354 million for inventory on hand and 348 million for excess purchase obligations. The same filing, submitted 2022-11-18, described offering alternatives including A800 outside the then-applicable licensing requirements [S96]. ELSA announced Japanese handling of A800 40GB Active on 2023-11-02; actual shipment dates required inquiry [S99].

**Inference.** Documented demand and selling-condition changes created pressure to sell through another product category. Investigating reassignment of compatible material or completed packages in later GA100 derivatives now has a more specific motivation.

**Hypothesis.** Some A800 40GB Active or later A30 units received existing compatible larger-capacity packages with fewer resources exposed. This predicts links between original package identity and later product allocation/settings. **An older package date on a later board is compatible with reassignment.**

**Alternatives and limits.** The charge identifies neither HBM density nor assembly stage. Ordinary 40 GB construction satisfies the specifications [S71], and A800's existence has a selling-condition explanation. The 2022 export-market A800 and later 40GB Active are not treated as one SKU. Reassignment merits investigation; excess 80 GB packages sold as 40 GB are not established.

## 3. AMD: different periods and motives

### MI50: compare around the addition of 32 GB

**Fact.** AMD's 2018-11-06 announcement specified MI50 16 GB, with shipments expected by the end of Q1 2019 [S103]. An AMD direct response published on 2019-10-15 explained that customers wanted MI60 capacity at MI50 pricing, motivating MI50 32 GB; MI60 shipments continued [S104]. This establishes public acknowledgment by that date, not manufacturing start.

**Inference.** A larger-capacity product route within MI50 makes shared parts a concrete question. But an official 32 GB outlet weakens the claim that capacity had to be hidden to sell it. SK hynix also described deployed 4 GB and 8 GB HBM2 in 2019 [S101]; lower-density construction had not demonstrably disappeared.

**Predicted cohort.** Compare factory-original 16 GB units around the 32 GB introduction by OEM, package number and revision. Common-part substitution should cluster density differences within particular families. Do not set the factory transition to 2019-10-15; independently documented earlier manufacture remains relevant. Where software already reports 32 GB despite a 16 GB label, examine stale labelling first [S43,S44].

### Vega: compare supply changes in late 2017

**Fact.** On 2017-07-18, Samsung announced increased 8 GB HBM2 production to meet growing demand, forecasting over half its HBM2 production by H1 2018 [S47]. On 2017-10-26, SK hynix planned HBM2 supply in Q4 [S100]. Neither plan proves fulfillment or adoption in a particular RX Vega.

**Inference.** Late 2017–2018 offers a specific period for comparing suppliers and packages in RX Vega 8 GB. Denser substitution would predict density differences tied to package groups. Growing demand does not establish surplus; different suppliers do not establish different densities.

**Alternative.** Two ordinary 4 GB stacks can provide 8 GB [S90]. Existing board analysis distinguishes a shared RX/Frontier Edition PCB from different installed GPU/HBM packages [S46]. Shared boards do not establish 16 GB population.

### BC-160: an ordinary 8 GB precursor route

AMD announced 5600M with 8 GB HBM2 in one GPU package on 2020-06-15 [S105]. AWS announced V520 adoption that December; AMD separately specifies its ordinary 8 GB capacity [S109,S51]. **Reuse of existing RDNA/HBM products** can therefore involve ordinary 8 GB.

A hidden-16-GB hypothesis needs a distinct higher-density package route. These sources establish neither 5600M/BC-160 physical compatibility nor actual reuse. Mining use alone does not transfer NVIDIA CMP's capacity restrictions to AMD.

## 4. Three histories whose starting points matter

| Event | Established fact | Consequence |
| --- | --- | --- |
| **CMP revenue decline** | USD 266m, 105m and 24m for quarters ended 2021-08-01, 2021-10-31 and 2022-01-30; decline preceded the September 2022 Merge [S95,S27] | Releases of existing finished stock can explain later cheap supply. Revenue does not identify units, unit prices, inventory or CMP100 manufacture |
| **CMP170HX circulation and performance changes** | A 2026 court record lists four October–November 2021 imports and a subsequent NVIDIA-provided VBIOS performance update [S94] | Same-unit settings can change performance. Separate import, manufacture and update dates; physical HBM total remains unresolved |
| **Products with an earlier intended use** | A30X description/early-access registration on 2021-11-10 [S97]; PG199 in DRIVE documentation updated 2023-02-03 [S98] | The 2022 mining decline postdates A30X's concept. The 2023 CoWoS statement does not establish a cause in 2021; an earlier constraint needs separate dated evidence. PG199 has an ordinary OEM-use explanation. Later configuration changes remain separate hypotheses |

AMD's 2018-10-24 results likewise document declining blockchain sales, high channel inventory and lower GPU ASP [S102]. They inform that market period, not inventories of the subsequently announced MI50 or loose HBM surplus.

## 5. Conditions behind “use larger parts during shortages”

**Fact.** Samsung's 2020-02-04 Flashbolt announcement said 8 GB Aquabolt supply would continue alongside 16 GB Flashbolt [S92]. SK hynix's 2022-06-08 announcement recorded both HBM3 mass production and completed NVIDIA sample evaluation [S106]. Part introduction and customer qualification are distinct milestones.

**Actual supply-end comparison.** Intel's 2023-09-30 notice discontinued listed Stratix 10 MX/NX 16 GB products because its supplier was ending HBM2 supply. Altera's 2024-09-30 notice covered listed 8 GB MX/NX/DX 2100 products. Neither offered replacements; both announced 2029-03-31 as the last-shipment cutoff [S107,S108]. These are total FPGA-product capacities, not per-stack densities.

Here the larger-capacity products received notice first; lower density does not universally disappear first. Responses include final purchases, discontinuation and redesign. Conversely, **existing compatible completed packages can retain extra memory if reassignment is attractive.** TSMC's 2023 CoWoS constraint [S83] makes the distinction relevant: obtaining denser loose HBM does not bypass required assembly.

Discontinuation, final orders and backlog repricing also affect prices [S108]. Accounting revenue and discontinuation notices are not used as a secondhand GPU price series. Verified transaction histories remain insufficient; see [market analysis](market.md).

## 6. Historical updates for eleven candidates

“Strengthened” applies only to the **named route or alternative**, not to a numerical probability of excess population.

| Candidate | Update | Cohort to compare |
| --- | --- | --- |
| **A800 40GB Active** | Specific reassignment motive; ordinary 40 GB fits. The 2022 A800 selling-condition response concerns a separate SKU [S96,S99,S71] | Link original packages to allocation from late 2022 onward; purchase year is insufficient |
| **A30** | Separate initial 2021 units from later allocation. Continued 8 GB supply weakens forced higher-density substitution [S26,S92,S96] | Original ordinary construction versus documented later revisions/allocations |
| **MI50 16 GB** | Official 32 GB route clarified; coexisting lower density and legitimate 32 GB sales oppose forced substitution [S103,S104,S101] | Factory-original 16 GB OEM/package families around 32 GB introduction |
| **RX Vega 56/64 8 GB** | Comparison period set to investigate supplier/part changes; denser surplus unconfirmed [S47,S100,S46] | Attributable supplier/package changes during late 2017–2018 |
| **CMP100-200** | Higher-capacity Volta existed in 2018; undated CMP manufacture prevents linking it to later stock reuse [S111,S95,S93] | Package, width and bandwidth from the same approximately 6 GB unit; ordinary 2 GB-stack model as control |
| **CMP100-210** | Compare ordinary V100 16/32 GB and declining CMP sales separately; performance change differs from capacity recovery [S08,S111,S95,S94] | Original 16 GB board families, split by package and VBIOS |
| **PG199** | Original DRIVE purpose strengthens an ordinary origin [S98,S12] | Original OEM modules versus converted, repaired or relabelled cards |
| **A30X** | Planned original-purpose explanation strengthened [S97,S01,S10] | Developer-kit, production and attributable later revisions |
| **H100 64 GB HBM2e** | 2023 document lists 64/94 GB HBM2e; HBM3 evaluation does not explain HBM2e selection [S110,S106] | Exact Scout/partner-cooled SKU, package and effective width |
| **H100 80 GB** | No new target-specific historical evidence that site six contains HBM [S62,S63] | Site material by package revision; general shortage adds no support |
| **BC-160** | Ordinary 8 GB predecessors strengthen ordinary reuse [S105,S109,S51] | Identified distinct higher-density packages unexplained by ordinary 8 GB comparisons |

**Historical research now focuses on** A800 allocation, MI50 capacity-specific packages and Vega supply changes. These are three investigative choices, not hidden-capacity probability tiers. CMP100-200's performance-side question continues separately.

## 7. Documentary decision rules

| Item | Application |
| --- | --- |
| **H: falsifiable hypothesis** | Route hypothesis: an event changed still-changeable allocation/part choices in a specified cohort. Excess hypothesis: this retained population above the rating. Separate these claims, manufacture and allocation intervals |
| **T: minimum comparison** | Compare at least one attributable change record and one earlier/ordinary control: a starting comparison, not a statistical sample requirement. One direct part identification can advance a unit-specific claim. Stop that route when a decisive ordinary explanation resolves it |
| **D: decision** | Route-connection PASS requires sourced timing, parts and target links. Physical-excess PASS separately requires population evidence; health/access are further claims. FAIL a route requiring a later cause or incompatible parts. Publication date alone is not event onset. Retain unresolved branches as UNCERTAIN |
| **C: alternatives** | Dedicated lower-density package, resale, stale high-capacity-product label, firmware-only performance differences, discontinuation-related prices |
| **U: uncertainty** | Missing manufacture dates, qualification scope, inventory form, document revisions and repair history. No combined standard uncertainty or coverage factor without a numerical error model |

## 8. Applications and ERROR CHECK

**Computer architecture** supplies ordinary capacity/bandwidth models; **packaging/reliability engineering** distinguishes loose-part substitution from completed-package grading; **industrial economics/causal inference** links demand, allocation, resale and prices. The method also applies to FPGA, OEM-only and discontinued industrial boards.

- Candidate-specific updates include evidence favoring ordinary explanations.
- Announcement, plan, accounting period, import, revision, final order and manufacture remain distinct.
- Accounting amounts imply no invented HBM inventory, density or unit count.
- AMD's 2019 response is an attributed direct statement reproduced by a journalist.
- Surviving 2023 NVIDIA document rows are not automatically backdated to initial drafts or driver releases.
- FPGA-specific discontinuations are not extrapolated to global or earlier GPU supply.
- Physical-population, health and usability status for all eleven candidates remains unchanged.

**Next question:** compared with a world without that historical event, what difference should appear in the target's part numbers, package or settings?
