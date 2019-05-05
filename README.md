# crawlTwitterImages
Twitter上で特定のユーザーの画像をGoogleDriveにダウンロードします。

## 使い方
1. 必要なライブラリのインストール
```
$ pip install -r pipfile.txt
```

1. `test_scripts/engine` と `app/engine` に`config.yml` を作成します
```config.yml

client_config:
  client_id: <GoogleAPIのAPI KEY>
  client_secret: <GoogleAPIのAPI SECRET>
client_config_backend: settings
get_refresh_token: true
oauth_scope:
- https://www.googleapis.com/auth/drive.file
- https://www.googleapis.com/auth/drive.install
save_credentials: true
save_credentials_backend: file
save_credentials_file: credentials.json
screen_names_and_last_id:
  <取得したいTwitterアカウントのscreen_name>: ''
  .
  .
twitter:
  access_token: <TwitterのACCESS TOKEN>
  access_token_secret: <TwitterのACCESS TOKEN SECRET>
  api_key: <TwitterのAPI KEY>
  api_secret: <TwitterのAPI SECRET>
```
1. `test_scripts/make_folder.py` を実行
```
$ python make_folder.py
```

1. 自分のGoogleDriveに `TwitterImageCrawl` フォルダーができていることを確認

1. 2つの `config.yml` に以下を追加
```config.yml
root_folder_id: <TwitterImageCrawlのID>
```

1. `/app` 上で `service.py` を実行
```
$ python service.py
```

