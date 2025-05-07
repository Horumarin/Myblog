# ブログ投稿アプリ（Django）

Python / Django を用いて作成した、ブログ投稿Webアプリケーションです。  
ポートフォリオとして、基本的な MVT 構成・バリデーション・PostgreSQLとの連携などの技術を取り入れました。

---

## 📌 機能一覧

- 記事の一覧表示
- 記事の新規登録（フォーム＋バリデーション）
- 記事の詳細表示
- 記事の編集機能
- 記事の削除機能
- ページネーション機能
- PostgreSQLへのデータ登録

---

## 🛠 使用技術

| 技術         | バージョン / 補足             |
|--------------|-------------------------------|
| Python       |  3.12.0                     |
| Django       |  5.1.6                       |
| PostgreSQL   | DB                          | 

---


## 📦 セットアップ手順

```bash
# クローン
git clone https://github.com/あなたのアカウント/Portfolio_Myblog
.git
cd Myblog


# manage.pyで起動
python manage.py runserver
