# GPUを使うためのCUDAToolkitイメージ
FROM nvidia/cuda:11.4.1-cudnn8-runtime-ubuntu20.04

RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim \
    libgl1-mesa-dev \
    build-essential
    # openslide-tools \
    # python-openslide

WORKDIR /opt

RUN wget https://repo.continuum.io/archive/Anaconda3-2020.11-Linux-x86_64.sh	&& \
    sh Anaconda3-2020.11-Linux-x86_64.sh -b -p /opt/anaconda3 && \
    rm -f Anaconda3-2020.11-Linux-x86_64.sh

ENV PATH /opt/anaconda3/bin:$PATH

COPY requirements.txt ./

# インストールに時間がかかるので分離しておく
RUN pip install --upgrade pip && pip install opencv-contrib-python

RUN pip install -r requirements.txt

# Non administrative username
ENV USERNAME=kurita_10

# Add non administrative user
RUN useradd -m ${USERNAME} && \
echo ${USERNAME}:password | chpasswd

# Add example group
RUN groupadd -g 1003 kurita

# Change user id and group id
RUN usermod -u 1003 -g 1003 ${USERNAME}

# Change user
USER ${USERNAME}

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token='jupyter'"]
