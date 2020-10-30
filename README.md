# Development
開発環境置き場 \
フォルダを作ってそれぞれにDockerfileを置いていく \
clone後に各フォルダに移動してからbuildするようにする予定

|                                                | Base                                        | Python                         | Overview                         |       
| ---------------------------------------------- | ------------------------------------------- | ------------------------------ | -------------------------------- | 
| Jupyterlab                                     | [ubuntu](https://hub.docker.com/_/ubuntu):latest | Anaconda3-2019.10-Linux-x86_64<br>[Anaconda installer archive](https://repo.anaconda.com/archive/) | Localhost:8888でJupyterlabが開く | 
| Jupiter_atomtemote                             | [ubuntu](https://hub.docker.com/_/ubuntu):latest | Anaconda3-2019.10-Linux-x86_64<br>[Anaconda installer archive](https://repo.anaconda.com/archive/) | ATOMとのリモート対応             | 
| UMAP                                           | [ubuntu](https://hub.docker.com/_/ubuntu):latest | Anaconda3-2019.10-Linux-x86_64<br>[Anaconda installer archive](https://repo.anaconda.com/archive/) | [公式HP](https://umap-learn.readthedocs.io/en/latest/index.html)<br>[GitHub](https://github.com/lmcinnes/umap)                           | 
| OpenSlide<br>（未着手）                        | -                                           | -                              | [公式HP](https://openslide.org)                           | 
| DeepLearning<br>（Dockerfileのみ追加：未検証） | [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda):10.1-cudnn7-runtime-ubuntu18.04| Anaconda3-2019.10-Linux-x86_64 |                                  | 
| Darknet<br>（未着手）                          | -                                           | -                              | [公式HP](https://pjreddie.com/darknet/)                           | 
