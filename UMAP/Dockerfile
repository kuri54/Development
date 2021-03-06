# ベースはminiconda3
FROM continuumio/miniconda3:latest

# 定型文と必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim

# ついでにpipもインストールしておく
RUN pip install --upgrade pip && pip install \
    seaborn \
    jupyter_kernel_gateway

# UMAPと関連ファイルのインストール
RUN conda install -y -c\
    conda-forge umap-learn \
    datashader \
    holoviews \
    bokeh

# ディレクトリを戻す
# WORKDIR /

# jupytelabがATOMと連携可能なようにしておく：上書き可能
CMD ["jupyter", "kernelgateway", "--KernelGatewayApp.ip=0.0.0.0", "--KernelGatewayApp.port=8888"]
