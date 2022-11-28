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

ARG USER_NAME
ARG GROUP_NAME
ARG GID
ARG UID

# Add non administrative user / Add example group / Change user id and group id
RUN useradd -m ${USER_NAME} && \
    echo ${USER_NAME}:password | chpasswd && \
    groupadd -g ${GID} ${GROUP_NAME} && \
    usermod -u ${UID} -g ${GID} ${USER_NAME}

# Change user
USER ${USER_NAME}

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token='jupyter'"]
