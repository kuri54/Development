# GPUを使うためのCUDAToolkitイメージ
FROM nvidia/cuda:11.2.2-cudnn8-runtime-ubuntu18.04

RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim \
    libgl1-mesa-dev
WORKDIR /opt
RUN wget https://repo.continuum.io/archive/Anaconda3-2019.10-Linux-x86_64.sh	&& \
    sh Anaconda3-2019.10-Linux-x86_64.sh -b -p /opt/anaconda3 && \
    rm -f Anaconda3-2019.10-Linux-x86_64.sh

ENV PATH /opt/anaconda3/bin:$PATH

RUN pip install --upgrade pip && pip install \
    keras==2.3 \
    scipy==1.4.1 \
    tensorflow-gpu==2.1 \
    comet_ml \
    albumentations \
    scikit-learn==0.24.2 \
    torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html \
    opencv-contrib-python

# Non administrative username
ENV USERNAME=kurita_10

# Add non administrative user
RUN useradd -m ${USERNAME}

# Add example group
RUN groupadd -g 1003 kurita

# Change user id and group id
RUN usermod -u 1003 -g 1003 ${USERNAME}

# Change user
USER ${USERNAME}

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token='jupyter'"]
