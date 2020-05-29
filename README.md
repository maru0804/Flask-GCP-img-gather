# Flask img gather
 
flaskとGCPを使用して手書き画像収集webサイトを作成

手書き入力された画像はGCSにフォルダ分けして保存される
 
# DEMO
 
# Requirement
 
requirements.txtファイルで必要なものを指定
 
# Usage

- ファイルに必要事項を追加する
 - your project name:GCPのプロジェクト名の記入
 - your backet name:GCSのbacket名を記入
 - your GCP URL:GCPの実行時に作成されるURLを記入
 
google cloud consoleにファイルをアップロードして以下のコマンドを入力して実行する

- 初期化コマンド
```bash
gcloud init
```
- 実行コマンド
```bash
gcloud app deploy
```

 
# Note
 
注意点などがあれば書く
