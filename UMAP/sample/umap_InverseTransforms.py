"""
https://umap-learn.readthedocs.io/en/latest/inverse_transform.html
公式リファレンス

UMAPは逆変換をサポートしている。
低次元埋め込み空間から高次元のデータサンプルを生成できる。
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns
import sklearn.datasets
import umap
import umap.plot

# MNISTデータを使用
data, labels = sklearn.datasets.fetch_openml('mnist_784', version=1, return_X_y=True)
data.shape

%time mapper = umap.UMAP(random_state=42, verbose=True).fit(data)
# rondom_stateを設定しておくとあとで結果が崩れない
# verboseをTrueにしておくと学習過程が見えて便利

umap.plot.points(mapper, labels=labels)
"""
それぞれの異なるクラスはちゃん分離されている。
逆変換演算を適用するためにはサンプルをembedding空間に落とし込む必要がある。
これを行うために、4点間を直線的に繋いだサンプルのグリッドを生成する。
-> 各頂点の座標を結ぶ（今回は左下：1、左上：7、右下：2、右上：0）

公式リファレンスの方法だと、グリッド値がわかりにくいので、https://qiita.com/khigashi02/items/17f69da4851c71d8a0dc
の方法でやってみる。
"""

x = mapper.embedding_

top_left = x[labels == '7', :][x[labels == '7', 0].argmin()]
btm_left = x[labels == '1', :][x[labels == '1', 1].argmin()]
top_right = x[labels == '0', :][x[labels == '0', 0].argmax()]
btm_right = x[labels == '2', :][x[labels == '2', 1].argmin()]

test_pts = np.array([
    (top_left*(1-x) + top_right*x)*(1-y) +
    (btm_left*(1-x) + btm_right*x)*y
    for y in np.linspace(0, 1, 10)
    for x in np.linspace(0, 1, 10)
])

print(top_left)
print(btm_left)
print(top_right)
print(btm_right)

# 逆変換を実行。inverse_transform関数に調べたい点の座標を与える。
inv_transformed_points = mapper.inverse_transform(test_pts)

fig = plt.figure(figsize=(12,6))
gs = GridSpec(10, 20, fig)
scatter_ax = fig.add_subplot(gs[:, :10])
digit_axes = np.zeros((10, 10), dtype=object)
for i in range(10):
    for j in range(10):
        digit_axes[i, j] = fig.add_subplot(gs[i, 10 + j])

scatter_ax.scatter(mapper.embedding_[:, 0], mapper.embedding_[:, 1],
                   c=labels.astype(np.int32), cmap='Spectral', s=0.1)
scatter_ax.set(xticks=[], yticks=[])

scatter_ax.scatter(test_pts[:, 0], test_pts[:, 1], marker='x', c='k', s=15)

for i in range(10):
    for j in range(10):
        digit_axes[i, j].imshow(inv_transformed_points[i*10 + j].reshape(28, 28))
        digit_axes[i, j].set(xticks=[], yticks=[])


"""
Fashion MNIST
"""
data_FM, labels_FM = sklearn.datasets.fetch_openml('Fashion-MNIST', version=1, return_X_y=True)
data_FM.shape
labels_FM

%time mapper_FM = umap.UMAP(random_state=42, verbose=True).fit(data_FM)

umap.plot.points(mapper_FM, labels=labels_FM)

x = mapper_FM.embedding_

top_left = x[labels_FM == '9', :][x[labels_FM == '9', 0].argmin()]
btm_left = x[labels_FM == '7', :][x[labels_FM == '7', 1].argmin()]
top_right = x[labels_FM == '3', :][x[labels_FM == '3', 0].argmax()]
btm_right = x[labels_FM == '4', :][x[labels_FM == '4', 1].argmin()]

test_pts = np.array([
    (top_left*(1-x) + top_right*x)*(1-y) +
    (btm_left*(1-x) + btm_right*x)*y
    for y in np.linspace(0, 1, 10)
    for x in np.linspace(0, 1, 10)
])

print(top_left)
print(btm_left)
print(top_right)
print(btm_right)

inv_transformed_points = mapper_FM.inverse_transform(test_pts)

fig = plt.figure(figsize=(12,6))
gs = GridSpec(10, 20, fig)
scatter_ax = fig.add_subplot(gs[:, :10])
digit_axes = np.zeros((10, 10), dtype=object)
for i in range(10):
    for j in range(10):
        digit_axes[i, j] = fig.add_subplot(gs[i, 10 + j])

scatter_ax.scatter(mapper_FM.embedding_[:, 0], mapper_FM.embedding_[:, 1],
                   c=labels_FM.astype(np.int32), cmap='Spectral', s=0.1)
scatter_ax.set(xticks=[], yticks=[])

scatter_ax.scatter(test_pts[:, 0], test_pts[:, 1], marker='x', c='k', s=15)

for i in range(10):
    for j in range(10):
        digit_axes[i, j].imshow(inv_transformed_points[i*10 + j].reshape(28, 28))
        digit_axes[i, j].set(xticks=[], yticks=[])

"""
上の方法だと、クラスが混ざっている部分（意図しない部分）に頂点を設定してしまっている。
右上のクラスタに設定が困難なため、公式の方法で描出する。
各頂点の座標はprintした座標を参考に、手動で設定する。
"""

corners = np.array([
    [-2, 6],
    [2, -2],
    [11, 13],
    [11, -5],
    ])

test_pts = np.array([
    (corners[0]*(1-x) + corners[1]*x)*(1-y) +
    (corners[2]*(1-x) + corners[3]*x)*y
    for y in np.linspace(0, 1, 10)
    for x in np.linspace(0, 1, 10)
])

inv_transformed_points = mapper_FM.inverse_transform(test_pts)

fig = plt.figure(figsize=(12,6))
gs = GridSpec(10, 20, fig)
scatter_ax = fig.add_subplot(gs[:, :10])
digit_axes = np.zeros((10, 10), dtype=object)
for i in range(10):
    for j in range(10):
        digit_axes[i, j] = fig.add_subplot(gs[i, 10 + j])

scatter_ax.scatter(mapper_FM.embedding_[:, 0], mapper_FM.embedding_[:, 1],
                   c=labels_FM.astype(np.int32), cmap='Spectral', s=0.1)
scatter_ax.set(xticks=[], yticks=[])

scatter_ax.scatter(test_pts[:, 0], test_pts[:, 1], marker='x', c='k', s=15)

for i in range(10):
    for j in range(10):
        digit_axes[i, j].imshow(inv_transformed_points[i*10 + j].reshape(28, 28))
        digit_axes[i, j].set(xticks=[], yticks=[])
