# GPUを使うためのCUDAToolkitイメージ
FROM nvidia/cuda:10.2-cudnn7-runtime-ubuntu18.04

RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim
WORKDIR /opt
RUN wget https://repo.continuum.io/archive/Anaconda3-2019.10-Linux-x86_64.sh	&& \
    sh Anaconda3-2019.10-Linux-x86_64.sh -b -p /opt/anaconda3 && \
    rm -f Anaconda3-2019.10-Linux-x86_64.sh

ENV PATH /opt/anaconda3/bin:$PATH

RUN pip install --upgrade pip && pip install \
    keras==2.3 \
    scipy==1.4.1 \
    tensorflow-gpu==2.1 \
    torch torchvision torchaudio

WORKDIR /
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''"]
