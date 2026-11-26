# 容量と帯域から予想する

[English](diagnostic-inference.md) · [トップ](../README.ja.md) · [候補](current-ranking.ja.md) · [出典](sources.md)

## 170HXでは何が怪しかったか

| 公開された観測・部品モデル | 容量 | 幅 | 帯域 |
| --- | ---: | ---: | ---: |
| 2023年の170HXレビュー（S87） | 8 GB級 | 4096 bit | 実測1166～1355 GB/s |
| 2 GB / 2.0 Gb/s HBM2×4（S93） | 8 GB級 | 4096 bit | 上限1024 GB/s |
| 2 GB / 2.4 Gb/s×4（感度分析） | 8 GB級 | 4096 bit | 上限1228.8 GB/s |
| 8 GB / 3.2 Gb/s HBM2E×4（S01） | 32 GB級 | 4096 bit | 上限1638.4 GB/s |

**推論：** 公開部品の低密度・速度条件では、容量と帯域を同時に満たしにくい。高速な大容量部品の一部公開を仮定すれば説明できる。帯域を満たす低密度の特注品、定格外動作、キャッシュを含む測定などは対立説明として残る。

## 判定の式

| 変数 | 意味・定義 | 単位 | 前提・型 |
| --- | --- | --- | --- |
| $c_i$ | 実HBMスタックiの通常データ容量 | byte | 正、スカラー |
| $b_i$ | 同じスタックの帯域上限 | byte/s | 非負、スカラー |
| $\rho_{\max}$ | 対象に許す部品・速度条件における最大の帯域/容量 | s$^{-1}$ | 正・有限、スカラー |
| $B$ | 実DRAM帯域 | byte/s | 非負、スカラー |
| $C_p$ | 実装容量（全$c_i$の和） | byte | 正、スカラー |
| $n,i$ | 実スタック数と添字 | 1 | 正整数、$1\le i\le n$ |

許した部品条件を各実装が満たすと仮定する。最大比の定義より、各スタックで $b_i\le\rho_{\max}c_i$。DRAMの総帯域は個々の上限の合計以下だから、

$$B\le\sum_{i=1}^n b_i\le\rho_{\max}\sum_{i=1}^n c_i=\rho_{\max} C_p.$$

正の最大比で割れば、

$$C_p\ge B/\rho_{\max}.$$

単位：byte/s ÷ s$^{-1}$ = byte。実帯域の保守的な下限が、公称容量で作れる帯域の上限を超えたとき、その部品集合内の通常モデルを棄却できる。部品集合が不完全なら物理容量の確定ではない。

## この方法を他のGPUに使う

MI50 16 GBの約1 TB/sは4 GB・256 GB/s品4基で説明できる。A30Xの24 GB・1223 GB/sも8 GB・3.2 Gb/s品3基で説明できる。一方、CMP 100-200の約6 GBでは幅・帯域がまだ揃わない。こうした差を[候補一覧](current-ranking.ja.md)と[製造史](historical-context.ja.md)に反映する。

## 詳細

[部品資料](../data/hbm_part_constraints.csv) · [実測・公称値の台帳](../data/performance_gap_observations.csv) · [容量・幅の完全な導出](capacity-constraints.ja.md)

詳細な旧版：[v0.11時点の全文](https://github.com/Unjuno/hbm-anomaly-research/blob/36ac571449d3a26c44da46afb06fda97093e6e47/docs/diagnostic-inference.ja.md)。 測定条件、容量単位、誤差、感度分析の完全な説明はこちら。
