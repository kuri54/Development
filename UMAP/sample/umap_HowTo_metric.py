"""
https://umap-learn.readthedocs.io/en/latest/supervised.html#using-labels-to-separate-classes-supervised-umap
公式リファレンス

MNISTデータを使うために "https://pypi.org/project/python-mnist/" を参照してダウンロード、インストールしておく

教師付き次元削減とMetric learning
"""
import numpy as np
from mnist.loader import MNIST
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='white', context='poster')

mndata = MNIST('/Users/hamamatsuikadaigakubyouribu/UMAP_python/python-mnist/data')
mndata
train, train_labels = mndata.load_training()
test, test_labels = mndata.load_testing()
data = np.array(np.vstack([train, test]), dtype=np.float64) / 255.0
target = np.hstack([train_labels, test_labels])
classes = [
    'T-shirt/top',
    'Trouser',
    'Pullover',
    'Dress',
    'Coat',
    'Sandal',
    'Shirt',
    'Sneaker',
    'Bag',
    'Ankle boot']

import umap

"""
教師なし次元削減
"""
%time embedding = umap.UMAP(n_neighbors=5, verbose=True).fit_transform(data)

fig, ax = plt.subplots(1, figsize=(14, 10))
plt.scatter(*embedding.T, s=0.3, c=target, cmap='Spectral', alpha=1.0)
plt.setp(ax, xticks=[], yticks=[])
cbar = plt.colorbar(boundaries=np.arange(11)-0.5)
cbar.set_ticks(np.arange(10))
cbar.set_ticklabels(classes)
plt.title('Fashion MNIST Embedded via UMAP');
"""
結果
多くのクラスをきれいに分離できたが、分離がうまくいっていないものもみられる
（T-shirt, shirt, dress, pullover, coat）
少なくともdressは大きく分かれていて、T-shirtはほとんどが大きな塊になっているが、他のものと区別がつかない
coat、shirt、pulloverはそれぞれが混ざり合っている
公式と生成画像が違う・・・・
"""

"""
教師あり次元削減
"""
%time embedding = umap.UMAP(verbose=True).fit_transform(data, y=target)
"""
上のものより時間がかかる
-> より大きなn_neighborsを設定しているため（教師付き次元削減を行うデフォルト値：15）
"""

# 可視化
fig, ax = plt.subplots(1, figsize=(14, 10))
plt.scatter(*embedding.T, s=0.1, c=target, cmap='Spectral', alpha=1.0)
plt.setp(ax, xticks=[], yticks=[])
cbar = plt.colorbar(boundaries=np.arange(11)-0.5)
cbar.set_ticks(np.arange(10))
cbar.set_ticklabels(classes)
plt.title('Fashion MNIST Embedded via UMAP using Labels');
"""
きれいに分離されたクラスのセットができた
-> 少しの浮遊ノイズがあるが、グループ化されないように十分に離れている

重要ポイント
・個々のクラスの内部構造を保持している
・グローバルな構造も保持している
-> データの重要な構造特性が保持されつつ、既知のクラスがきれいに分離されている
"""

"""
半教師あり次元削減

データの一部にしかラベルがついていない場合
-> 持っているラベル情報を利用したい
"""
# いくつかのラベルをランダムにマスク -> -1に置き換える
masked_target = target.copy().astype(np.int8)
masked_target[np.random.choice(70000, size=10000, replace=False)] = -1

# UMAPは-1ラベルをラベルのない点として解釈する
%time fitter = umap.UMAP(verbose=True).fit(data, y=masked_target)
embedding = fitter.embedding_

fig, ax = plt.subplots(1, figsize=(14, 10))
plt.scatter(*embedding.T, s=0.1, c=target, cmap='Spectral', alpha=1.0)
plt.setp(ax, xticks=[], yticks=[])
cbar = plt.colorbar(boundaries=np.arange(11)-0.5)
cbar.set_ticks(np.arange(10))
cbar.set_ticklabels(classes)
plt.title('Fashion MNIST Embedded via UMAP using Partial Labels');
"""
結果
教師付きのようにきれいに分離できたわけではないが、よりきれいにはっきりとしたものになった。
この半教師付きのアプローチはラベリングの作業量が多い可能性がある場合や、ラベルより多くのデータを持っていてその余分なデータを利用したい場合に有用。
"""

"""
ラベル付き学習とラベルなしテストデータの埋め込み
UMAPによるMetric Learning

教師付き学習をした場合、その結果を使ってラベル付されていない新しい点をその空間に埋め込む
-> Metric Learning
   ラベル付けされた学習データをラベル付されていないデータ間の尺度として用いる
"""
train_data = np.array(train)
test_data = np.array(test)

%time mapper = umap.UMAP(n_neighbors=10, verbose=True).fit(train_data, np.array(train_labels))

# ↑で学習させた空間にラベルデータを渡さず配置させる
%time test_embedding = mapper.transform(test_data)
"""
いくつかのアプローチほど高速ではないが、かなり効率的に学習した
"""

# 可視化
fig, ax = plt.subplots(1, figsize=(14, 10))
plt.scatter(*mapper.embedding_.T, s=0.3, c=np.array(train_labels), cmap='Spectral', alpha=1.0)
plt.setp(ax, xticks=[], yticks=[])
cbar = plt.colorbar(boundaries=np.arange(11)-0.5)
cbar.set_ticks(np.arange(10))
cbar.set_ticklabels(classes)
plt.title('Fashion MNIST Train Digits Embedded via UMAP Transform');
"""
他のアプローチと同様の挙動
内部構造と全体的なグローバル構造の両方を保ったまま別々のクラスを埋め込むことができた
次に、ラベル情報をもっていないテストデータがtransform()メソッドによってどのように埋め込まれたか見てみる
"""

fig, ax = plt.subplots(1, figsize=(14, 10))
plt.scatter(*test_embedding.T, s=2, c=np.array(test_labels), cmap='Spectral', alpha=1.0)
plt.setp(ax, xticks=[], yticks=[])
cbar = plt.colorbar(boundaries=np.arange(11)-0.5)
cbar.set_ticks(np.arange(10))
cbar.set_ticklabels(classes)
plt.title('Fashion MNIST Train Digits Embedded via UMAP');
