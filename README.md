## PysonDiary
* 日記を書くアプリ。その日の記念日や明日の天気を表示することもできる。</br>
  (20241226追記 リポジトリ名がPythonDiaryでなくPysonDiaryになっていることに面談中に気づきました。</br>
  修正しようと思いましたが、2024年の評価シートに成果物として張ったリンクがすでに修正できないため、
  今回はこのままにしています。大変申し訳ございませんが何卒宜しくお願いいたします。)

## Description
1. 日記を作成（画像1枚登録可能）、編集、削除できる。
2. アクセスしたその日が世間で何の記念日か確認できる。
3. 明日の天気を確認できる。

## Background
* PythonでCRUD処理をどう作成するか、APIはどうやって使用するのか、スクレイピングの処理をどうするかを確認する個人的学習のために作成。

## Development environment
|種別|名称|
|----|----|
|開発言語|Python(ver 3.12.4)|
|フレームワーク|Django(ver 5.1.3)|
|マークアップ|HTML,CSS|
|DB|SQLite|

## Demo
* 日記作成と詳細画面　https://gyazo.com/5c9e96a0150589f0386814b8300da925
* 日記編集　https://gyazo.com/4840d57a84dee7e422a9316fe3cf7c9d
* 日記削除　https://gyazo.com/185da0253f804ebe698d349f76d32f59
* 今日は何の日？ メニュー押下　https://gyazo.com/18534dcfb5d90f1884abaa5689d6de50
* 明日の天気 メニュー押下　https://gyazo.com/528ba765a86e13eaa5706249a1a5c42a

## Usage
1.リポジトリをクローンする。`https://github.com/dorabby/PysonDiary.git`

2./PysonDiary/diary配下でサーバーを起動する。
```
python manage.py runserver
```
3.起動後、`http://127.0.0.1:8000/login`でログイン画面へアクセスする。ログインは以下のユーザーでログインできる。
```
 ユーザー名: test
 Password: tes10test
```

## Author
* Aoi Tokuzumi
* o68.tokuzumi.aoi@gmail.com
