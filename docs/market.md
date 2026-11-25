# Market evidence protocol

[Home](../README.md)

**v0.4.0 ranking use: no price-based adjustment.** The current observations do not establish a comparable transaction time series. The [prediction ranking](candidates.md) therefore uses theory and sourced product evidence without assigning market-price points.

Secondary-market observations are a hypothesis generator, never proof of hidden capacity. A new price on a multi-quantity listing does not identify the historical transaction price of earlier units. A disappearance may mean sale, withdrawal, relisting, or account closure. Do not assume it means inventory was purchased.

Use `data/market_observations.csv` and the market issue template. Record UTC observation time if available, source update time separately, listing ID, product/revision, exact SKU/condition/quantity, price type, currency, per-unit price, shipping and accessories, stock indication, sold-counter indication, actual transaction evidence and source URL. Separate new and used, and standalone modules from bundles. Preserve source text hashes or permitted snapshots without exposing personal identifiers. Never scrape in breach of platform terms or evade access controls.

### Initial observation

An archived eBay page for item 226540664379 displayed USD 109.99, used, out of stock, 4 sold, and a last-update timestamp of 2026-05-21. The page retrieved on 2026-11-25 was stale; the capture time was not supplied precisely. This is **one asking-price snapshot**, not four sales at that price, not a current offer, and not evidence of a price trend [S18]. Earlier conversation claims of a later USD 399 snapshot could not be revalidated for this release and are excluded. A second independently timestamped source is needed.

### Analysis once data exist

Compare matching region, variant, condition, lot size and bundle across time; compare actual per-unit sale prices separately from asks. Count distinct sellers and observations, detect repeated listings, show median and interquartile range where appropriate, and do not report a percent change when the baseline is missing. Compare against related accelerator controls to account for general demand, shipping cost, currency, and performance or adapter news. Examine whether selective demand for a revision predates public capacity news, without interpreting it as proof of a private discovery. Collect pre-announcement data where accessible; pre-specify comparisons to limit post hoc selection. No threshold is statistically calibrated in v0.4. Where a listing includes credible production provenance, join to cohort evidence only at that supported granularity; listing/update dates are not manufacturing dates. Keep the [historical supply events](../data/supply_events.csv) separate from secondary-market observations.
