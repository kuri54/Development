# ベースはminiconda3
FROM continuumio/miniconda3:latest

# 定型文と必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    # 念の為入れとくパッケージ
    sudo \
    wget \
    vim

RUN pip install --upgrade pip && pip install \
    numpy \
    matplotlib \
    seaborn \
    pandas \
    jupyter_kernel_gateway \
    ipywidgets \
    # Pytorchのインストール
    torch==1.8.0+cpu torchvision==0.9.0+cpu torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html

# jupytelabがATOMと連携可能なようにしておく：上書き可能
CMD ["jupyter", "kernelgateway", "--KernelGatewayApp.ip=0.0.0.0", "--KernelGatewayApp.port=8888"]
