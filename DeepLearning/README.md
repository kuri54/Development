## サーバーとリモート連携可能なdockerimage
1. Dockerfile、docker-compose.ymlと同じディレクトリに`.env`を作成
2. サーバーにアクセスし、`id`コマンドでuidとgidを確認する
3. `.env`の内容を以下のように編集する
   ```YAML
   COMET_API_KEY='' # Comet.mlのAPI Key
   USERNAME='' # 自分のユーザー名
   GROUPNAME='' # 自分のグループ名
   UID=
   GID=
   ```
4. `docker-compose.yml`のGPU設定を確認、編集
5. `docker compose up --build -d`