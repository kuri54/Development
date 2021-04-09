## サーバーとリモート連携可能なdockerimage
1. SSHでサーバーに接続
2. サーバーにDockerfileとdocker-compose.ymlを置く
3. ```docker-compose up --build``` でbuildとrunを一気に行う
　 ~> 自動的にローカルのworkが共有されている~  <span style="color: red; "><- はずだがまだできていない</span>  
    マウント先を変更したい場合はdocker-compose.ymlを変更し、  
    ```docker-compose up --build```
4. ターミナル上に表示されているjupyterのtokenをコピーする
5. ターミナルで新しくウィンドウを立ち上げ、```ssh -L 8888:localhost:8888 kurita_10@10.202.18.10```としてPort Forwardingで接続する<span style="color: red; "><- ボリュームのマウント設定がうまくいけば初っ端からそういけるかも</span>
6. ATOMの設定変更 \
[Hydrogenのリモート設定](https://blog.johannhuang.com/+Articles/analytics/20170825i) を参考にしてGatewaysの設定をする
7. ATOMで操作したいファイルを開く
8. ```⌘＋shift＋p``` でパレットを開く
9. パレットでHydrogen: Connect To Remote Kernel を選択
10. コピーしたtokenを貼り付けてセッションを立ち上げる
