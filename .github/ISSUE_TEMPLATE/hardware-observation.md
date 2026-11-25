---
name: Hardware observation (read-only)
about: Report a stock or existing GPU without making changes
title: "[Observation] "
---

## Minimum report / 最小報告

Start with what you already know. Unknown is acceptable; the detailed fields below are optional for an initial report.
既に分かる項目だけ記入してください。不明は不明のままで構いません。初回は詳細欄をすべて埋める必要はありません。

- Product and advertised capacity / 製品名・公称容量:
- Observation date / 観測日:
- What was actually observed, with exact units / 実際に確認した事実・正確な単位:
- Existing redacted output, photo, or source URL / 識別情報を伏せた既存ログ・写真・資料URL:
- Stock / previously modified or repaired / unknown / 未改造・改造修理済み・不明:
- Environment if known (driver, physical board or virtualization) / 分かる範囲の環境:
- Which hypothesis does this change, and what remains unknown? / 変わる前提・残る不明点:

Ordinary and uncertain results are useful. A driver reporting nominal capacity does not establish the absence of extra physical HBM. No purchase, disassembly or configuration change is required.
通常構成や未判定の報告も有用です。公称どおりの容量表示だけでは、物理的な余剰HBMを否定できません。購入・分解・設定変更は不要です。

## Optional: device identity / 任意の詳細情報

- Product / nominal capacity:
- PCI vendor:device and subsystem vendor:device:
- Board PN, PCB revision, GPU/DRAM markings if already available:
- Raw date code (redacted), date type (HBM/package/PCB/final assembly/etc.), earliest/latest supported date, precision and source:
- Documented cohort/lot token (non-identifying only), acquisition channel category, repair/rework history:
- HBM part/density evidence if already available (do not infer from width):
- Stock / previously modified / unknown:

## Optional: environment and observation

- OS, kernel, driver, runtime, VBIOS:
- MIG/vGPU, ECC and reservations if known:
- Reported total/free memory (exact units):
- Memory clock and transfer-rate source, temperature and power conditions:
- Read-only output (redacted) or permitted photo / source URL:

## Interpretation

- Observed facts (not assumptions):
- Uncertainties or contradictory evidence:
- Can an ordinary configuration explain this?

I have permission to share these data. I have removed serial numbers, UUIDs, private information and proprietary binaries. No modifications are requested.
