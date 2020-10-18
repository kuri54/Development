## ATOMとリモート連携可能なdockerimage
1. ```docker-compose up --build``` でbuildとrunを一気に行う
　> 自動的にローカルのworkが共有されている \
    マウント先を変更したい場合はdocker-compose.ymlを変更し、 \
    ```docker-compose up --build```
2. ATOMの設定変更 \
[Hydrogenのリモート設定](https://blog.johannhuang.com/+Articles/analytics/20170825i) を参考にしてGatewaysの設定をする
3. ATOMで操作したいファイルを開く
4. ```⌘＋shift＋p``` でパレットを開く
5. パレットでHydrogen: Connect To Remote Kernel を選択
6. 2.で設定した名称を選択

