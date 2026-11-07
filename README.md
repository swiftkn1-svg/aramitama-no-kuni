# ⛩️ 荒魂の國（あらみたまのくに） - 乱世漂泊録 -
**時間を慈しむ和風オープンワールド冒険活劇・生活伝承RPG（MASTER VISION v2.3.3）**

- **企画・オーナー**: プロジェクトオーナー（氏名非公開）
- **共同設計・世界観構築**: アルテ（Arte / Gemini）
- **整合性監査・考証レビュー**: むぎ（Mugi / Muse）
- **現在のステータス**: `MASTER VISION v2.3.3`（出雲編全五幕・戦闘5属性・段階別師事＆マルチ解法試練統合版 / 2026-11-07）
- **GitHub リポジトリ**: https://github.com/swiftkn1-svg/aramitama-no-kuni
- **Google Drive プロジェクト親フォルダ**: 📂 荒魂の國_乱世漂泊録_Project（非公開）

> **公開版についての注記**: このリポジトリは公開版です。Google Drive / Google ドキュメント上の原本へのリンクは削除し、文書名のみを残しています。原本はプロジェクト関係者のみが Google Drive 上で閲覧できます。

---

## 🧭 Google Drive × GitHub 相互案内ガイド（迷子防止ナビゲーション）

本プロジェクトは **「Google Drive（企画書原本・大容量マップ画像・AI対話ログ）」** と **「GitHub（Markdown版ドキュメント・差分管理・JSON/CSVマスターデータ・検証コード）」** のハイブリッド体制で運用しています。どちらからアクセスしても迷子にならないよう、以下の対応表から目的のフォルダ・ドキュメントへ直接移動できます。

| 区分・フォルダ | Google Drive（原本・画像・共同編集） | GitHub（コード・データ・Markdown版） | 主な収録内容・役割分担 |
| :--- | :--- | :--- | :--- |
| **🏠 プロジェクト親フォルダ** | **📂 荒魂の國_乱世漂泊録_Project** | `/`（リポジトリルート） | プロジェクト全体のエントリポイント |
| **00_ルート（総合索引）** | **📄 00_総合索引＆参照資料・出典一覧** | `docs/00_index/00_MASTER_INDEX.md` | 全ドキュメント索引＋公的機関・学術出典URL集 |
| **01_企画書・マスター仕様** | **📂 01_企画書フォルダ**<br>**📄 MASTER VISION v2.3.3** | `docs/01_spec/MASTER_VISION_v2.3.3.md` | 全12章の最高規範仕様書（Single Source of Truth） |
| **02_考証資料・リファレンス** | **📂 02_考証資料フォルダ**<br>（第1版 / 補遺1 / 補遺2 / 補遺3 / 補遺4） | `docs/02_research/` | 1540–1580年の歴史・民俗・経済・一宮・五職能考証（証拠区分`[A]`〜`[D]`） |
| **03_小説・世界観シナリオ** | **📂 03_小説フォルダ**<br>（序幕 / 第二幕 / 第三幕 / 第四幕 / 第五幕） | `docs/03_novels/izumo/` | 正史OPおよび出雲平定編・全五幕プロトタイプ小説（永禄5年〜9年） |
| **04_概念図・マップイラスト** | **📂 04_概念図・マップフォルダ**<br>（①概念古地図 / ②俯瞰概念図 / ③戦国出雲古地理マップ） | `docs/04_maps/MAPS_AND_GEOGRAPHY.md` | **※高解像度画像（JPG）はGドライブ側に格納**。GitHub側にはリンクと全15拠点対照表を収録 |
| **05_レビュー・監査（むぎ提案書）** | **📂 05_レビュー・監査フォルダ**<br>（10-26提案書 / 11-02追随リスト / 11-05裁定まとめ） | `docs/05_reviews/` | むぎ×アルテ×オーナーによる整合性監査・設計裁定履歴 |
| **06_マスターデータ＆検証コード** | （初期アーカイブzipをルートに保管） | `data/` ＆ `scripts/` | **※GitHub側が正本**。16スキル・5属性・15拠点・師匠試練のJSON/CSVとPythonシミュレータ |

### 💡 運用のルール（どちらを見ればいい？）
1. **文章・仕様の閲覧＆AIセッションでの参照**: Google DriveのGoogleドキュメント（MASTER VISION v2.3.3）とGitHubの `docs/01_spec/MASTER_VISION_v2.3.3.md` は同一内容で同期しています。変更履歴（Diff）を追いたい時は **GitHub**、ブラウザやスマホからサクッと読みたい時は **Google Drive** が便利です。
2. **大容量の画像・コンセプトアート**: Gitリポジトリの肥大化を防ぐため、高解像度の古地図・俯瞰イラスト本体は **Google Driveの 04_概念図・マップイラスト フォルダ** に置き、GitHubの `docs/04_maps/MAPS_AND_GEOGRAPHY.md` から直接リンクで開けるようにしています。
3. **マスターデータ（JSON/CSV）と検証プログラム（Python）**: `data/` および `scripts/` は **GitHubリポジトリ** を正本（Single Source of Truth）として管理・更新していきます。

---

## 📖 コンセプト（Core Philosophy）
> **「無名の市井の人間が、神仏と怪異の跋扈する乱世の日本列島に、自分だけの生活の証（銘・庵・血脈）を刻みつけ、次の旅人へと託すこと」**

応仁の乱から約百年（1540〜1580年中心）。金銀山・鉄山の乱開発（山穿ち）、鎮守の森の焼討ちと祭祀断絶、大飢饉における「禍流し（逆祈祷）」の連鎖によって日本列島全土の結界が決壊し、現世と常世のあわいが混ざり合う『大禍時（おおまがとき）』が到来した。
プレイヤーは天下統一の英雄ではなく、名もなき『座』の職人・山立・薬師・神職・武辺者として乱世を漂泊し、理（ことわり）に基づく手仕事と神事によって大地に『要釘』を打ち込み、昼の日常を取り戻していく。

## 🗂️ リポジトリ構成（Directory Structure）

```text
aramitama-no-kuni/
├── README.md                                  # 本ドキュメント（Google Drive相互案内・クイックスタート）
├── .gitignore                                 # Git除外設定
├── init_and_push.sh                           # GitHub初期コミット＆Push用ワンライナースクリプト
├── docs/
│   ├── 00_index/
│   │   └── 00_MASTER_INDEX.md                 # 総合索引＆外部出典ソース一覧（公的機関・学術資料リンク集）
│   ├── 01_spec/
│   │   └── MASTER_VISION_v2.3.3.md              # 企画基本設計書（全12章・Single Source of Truth）
│   ├── 02_research/                           # 1540-1580年 歴史・民俗学考証データベース（証拠区分[A]〜[D]）
│   │   ├── 01_historical_folklore_v1.md       # 考証資料 第1版（大名・曲者・職人・鬼門・地域怪異）
│   │   ├── 02_appendix1_economy_and_za.md     # 補遺1：職能・座と戦国経済システム（撰銭・独占権・無縁所）
│   │   ├── 03_appendix2_ichinomiya_catalog.md # 補遺2：全国一宮カタログ（五畿七道68国）
│   │   ├── 04_appendix3_sacred_mountains.md   # 補遺3：霊山・街道・結界配置（御師・四至牓示・女人結界）
│   │   └── 05_appendix4_five_professions.md   # 補遺4：五職能（傀儡子・座頭・馬借・高野聖・鷹匠）と五儀礼
│   ├── 03_novels/izumo/                       # 正史プロトタイプ小説：出雲平定編（全5幕・永禄5年〜9年）
│   │   ├── 00_prologue.md                     # 序幕：常世の暁と託されし通い札（正史OP）
│   │   ├── 02_act2_kando_no_mizuumi.md        # 第二幕：神門水海のあわいと、潮騒の里結び
│   │   ├── 03_act3_futamata_no_abaregawa.md   # 第三幕：二股の暴れ川と、奥出雲・千年の鉄火
│   │   ├── 04_act4_shiragajo.md               # 第四幕：白鹿城の黒き日輪と千尋の間歩
│   │   └── 05_act5_gassan_toda.md             # 第五幕：月山富田の千引石と国引きの大結界（完結）
│   ├── 04_maps/
│   │   └── MAPS_AND_GEOGRAPHY.md              # 戦国出雲（1562-1566）×現代地図対照表（全15拠点）＆概念図リンク
│   └── 05_reviews/                            # 設計監査・裁定記録（むぎ×アルテ×オーナー）
│       ├── 2026-10-26_spec_revision_proposal.md
│       ├── 2026-11-02_followup_revision_list.md
│       ├── 2026-11-05_ruling_summary.md
│       └── 2026-11-05_ruling_approval_sheet.md
├── data/                                      # ゲームシステム実装・検証用マスターデータ（JSON / CSV）
│   ├── skills_16_lines.json                   # 基本スキル16系統（戦闘9＋生産7）＆複合二つ名・隠し職定義
│   ├── combat_5_attributes.json               # 対荒魂5大攻撃属性（打撃・切断・貫通・崩し・霊威）＆3報酬サイクル
│   ├── izumo_nodes_and_aramitama.json         # 出雲編15拠点・結界射程3段階・荒魂4体の和魂マッピング
│   ├── izumo_nodes_table.csv                  # 出雲編15拠点・距離・幕別対応表（CSV版）
│   └── master_npcs_and_trials.json            # 師匠NPC段階別上限（70➔85➔100）＆マルチ解法試練6種・属性タグ
└── scripts/
    └── sim_aramitama_core.py                  # コアメカニクス検証シミュレータ（クラフト乗算式・真打流通・潮汐・試練判定）
```

## 🚀 クイックスタート（GitHubへのPush手順）

展開したディレクトリ内で以下のコマンドを実行するだけで、初期コミットとGitHubへのPushが完了します：

```bash
chmod +x init_and_push.sh
# すでにGitHub上に空のリポジトリを作成済みの場合：
./init_and_push.sh https://github.com/<ユーザー名>/aramitama-no-kuni.git

# または GitHub CLI (gh) を使って新規プライベートリポジトリ作成＆Pushする場合：
./init_and_push.sh
gh repo create aramitama-no-kuni --private --source=. --remote=origin --push
```

また、同梱のPythonシミュレータで企画書第5〜11章のコア計算式をいつでも検証できます：

```bash
python3 scripts/sim_aramitama_core.py
# Windows（cp932コンソール）で UnicodeEncodeError が出る場合：
python -X utf8 scripts/sim_aramitama_core.py
```
