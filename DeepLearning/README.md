## サーバーとリモート連携可能なdockerimage
1. SSHでサーバーに接続
    -> jupyter notebookを使用するのであれば、ポートフォワーディングしておく
        ex: ssh -i 鍵 -L 8888:localhost(あるいはリモートのIP):8888 user@remote
2. サーバーにDockerfileとdocker-compose.ymlを置く
3. ```docker-compose up --build``` でbuildとrunを一気に行う
4. ATOMの設定変更 \
[Hydrogenのリモート設定](https://blog.johannhuang.com/+Articles/analytics/20170825i) を参考にしてGatewaysの設定をする
5. ATOMで操作したいファイルを開く
6. ```⌘＋shift＋p``` でパレットを開く
7. パレットでHydrogen: Connect To Remote Kernel を選択
8. Dockerfileで設定しているtokenを入力してセッションを立ち上げる
