# ベースはminiconda3
FROM continuumio/miniconda3:latest

# 定型文と必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    # 念の為入れとくパッケージ
    sudo \
    wget \
    vim \
    libgl1-mesa-dev

COPY requirements.txt ./

# インストールに時間がかかるので分離しておく
RUN pip install --upgrade pip && pip install opencv-contrib-python

RUN pip install -r requirements.txt

# jupytelabがATOMと連携可能なようにしておく：上書き可能
CMD ["jupyter", "kernelgateway", "--KernelGatewayApp.ip=0.0.0.0", "--KernelGatewayApp.port=8888"]
