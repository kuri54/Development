## docker-compose.ymlを使わない場合
1. ```docker build .```
2. ```docker run -it -v <clone先のworkのパス>:/work -p 8888:8888 <image名>```
3. ブラウザで```localhost:8888```にアクセス

## docker-compose.ymlを使う場合
1. ```docker-compose up --build``` でbuildとrunを一気に行う
2. ブラウザで```localhost:8888```にアクセス
