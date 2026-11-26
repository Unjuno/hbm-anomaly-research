# HBM Anomaly Research

[English](README.md) · [資料一覧](docs/README.md)

**公称より多くのHBMが載っているGPUを、性能・部品仕様・製造史から予想する研究です。**

## 出発点：CMP 170HX

2023年の実機レビューでは、8 GB級のCMP 170HXが4096-bit、実測1166～1355 GB/sを記録しています。当時の公表2 GB HBM2（2.0 Gb/s）を4基使う通常モデルでは1024 GB/sが上限です。高速な大容量HBMを一部だけ公開した構成なら、この不整合を説明できます。[分析・出典](docs/diagnostic-inference.ja.md)

## 今、注目している候補

| 製品 | 注目する理由 |
| --- | --- |
| **CMP 100-200** | 約6 GB。幅と帯域を調べ、170HXと同じ種類の不整合があるか確かめたい。 |
| **A800 40GB Active** | 2022年後半の在庫・販売先変更。完成パッケージの転用仮説。 |
| **AMD MI50 16 GB** | 32 GB版の追加前後で、元の16 GB品に部品変更があったか。 |
| **AMD RX Vega 56/64** | 2017年後半～2018年のHBM供給計画とパッケージ差。 |

**[全11候補と容量の予想 →](docs/current-ranking.ja.md)**

これらは調査中の仮説です。実機による独自検証はなく、条件付きの容量は利用可能容量の保証ではありません。

## 研究資料

- [理論：容量と帯域から何が分かるか](docs/diagnostic-inference.ja.md)
- [製造史：いつ、なぜ部品を転用し得たか](docs/historical-context.ja.md)
- [候補CSV](data/current_ranking.csv) · [出典](docs/sources.md) · [詳細資料・旧版](docs/README.md)

[情報提供・反例の投稿](docs/call-for-participants.ja.md) ｜ [MIT License](LICENSE)

<sub>v0.12.0 · 2026-11-27 · 公開情報による研究</sub>
