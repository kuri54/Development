# ベースはubuntu
FROM ubuntu:latest

# 定型文と必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim

# Anacondaのインストール先を /opt に変更
WORKDIR /opt

# archiveから.shをダウンロードし、インストール
RUN wget https://repo.continuum.io/archive/Anaconda3-2019.10-Linux-x86_64.sh && \
    sh Anaconda3-2019.10-Linux-x86_64.sh -b -p /opt/anaconda3 && \
    rm -f Anaconda3-2019.10-Linux-x86_64.sh

# pythonのPATHを通す
ENV PATH /opt/anaconda3/bin:$PATH

# ついでにpipもインストールしておく
RUN pip install --upgrade pip && pip install \
    jupyter_kernel_gateway

# ディレクトリを戻す
WORKDIR /

# jupytelabがATOMと連携可能なようにしておく：上書き可能
CMD ["jupyter", "kernelgateway", "--KernelGatewayApp.ip=0.0.0.0", "--KernelGatewayApp.port=8888"]
