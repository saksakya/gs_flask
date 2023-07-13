## Flask

## 紹介と使い方
- 今後pythonをメインで使っていく予定なので、flaskを使ってCRUD処理及びログイン機能を実装しました。
- 今週は余り時間を取れなかったので、最低限の機能しか実装できていません。

## 工夫した点
- 簡単なデータベースで並び替え等も実装していないので、普通のDBです。

## 苦戦した点
- laravelでCRUD処理をやっていたので、特に難しくはなかったです。
- 時間が取れなかったので、DRY原則を守れていません。

## 参考にした web サイトなど
- https://eh-career.com/engineerhub/entry/2023/05/29/093000

## Memo

- 使用しているライブラリ一覧取得
- pipreqs --encoding UTF8 .
- conda install -r requirements.txt

- ※migration
- 初期化
$ flask db init
- テーブル生成するためのコードを生成する
$ flask db migrate
- テーブル生成する
$ flask db upgrade