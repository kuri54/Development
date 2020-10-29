"""
https://qiita.com/dl_from_scratch/items/ef5e577cf197a09f98ad
結果のグループを調べる
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
digits = load_digits()
print(digits.data.shape)
print(digits.target.shape)
print(digits.images.shape)

def draw_digits(i_list, n_grid=(10, 10), annosize=10, figsize=(12, 12)):
    # assume: i_listは画像配列の番号をリストに入れたもの、annosize=Noneで画像列番と正解ラベルを非表示
    images = digits.images
    labels =digits.target

    fig = None
    i_ax = 0
    for i_img in i_list:

        if fig is None or i_ax >= n_grid[0] * n_grid[1]:
            fig = plt.figure(figsize=figsize)
            plt.subplots_adjust(hspace=0.02, wspace=0)
            i_ax = 0
        i_ax += 1

        ax = fig.add_subplot(n_grid[0], n_grid[1], i_ax)
        if i_img is None:
            ax.axis('off')
            continue

        ax.imshow(images[i_img], cmap='gray', interpolation='none')
        if annosize is not None: # if: 画像列番と正解ラベルを追記
            ax.annotate("%d" % i_img,
                xy=(0, 0.98), xycoords='axes fraction', ha='left', va='top', color='y', fontsize=annosize)
            ax.annotate("L:%d" % labels[i_img],
                xy=(1, 0.98), xycoords='axes fraction', ha='right', va='top', color='c', fontsize=annosize)
        ax.axis('off')

    plt.show()

draw_digits(list(range(24)))

import umap
from scipy.sparse.csgraph import connected_components

res_umap = umap.UMAP().fit_transform(digits.data)
print(res_umap.shape)

import matplotlib.cm as cm
plt.figure(figsize=(6, 6))
plt.scatter(res_umap[:,0], res_umap[:,1], s=3, c=digits.target, cmap=cm.tab10)
plt.colorbar()
plt.show()

plt.scatter(res_umap[:, 0], res_umap[:, 1], s=10, c=digits.target, cmap=cm.tab10)
plt.axis([-3, 1, 3, 5]); plt.grid(); plt.show()

i_list = np.where((-1.5 < res_umap[:, 0]) & (res_umap[:, 0] < -1) & (3.3 < res_umap[:, 1]) & (res_umap[:, 1] < 4))[0]
i_list

draw_digits(i_list)

def draw_digits_at_tsne(res, x_min, x_max, y_min, y_max,
    n_grid=(15, 15), annosize=8, figsize=(12, 12)):

    x_pitch = (x_max - x_min) / n_grid[1]
    y_pitch = (y_max - y_min) / n_grid[0]
    i_draw_list = []
    for i_y in range(n_grid[0]):
        y_i = y_max - y_pitch * i_y - y_pitch/2 # 格子中央点
        for i_x in range(n_grid[1]):
            x_i = x_min + x_pitch * i_x + x_pitch/2 # 格子中央点

            i_list = np.where((x_i-x_pitch/2 < res[:, 0]) & (res[:, 0] < x_i+x_pitch/2) & \
                              (y_i-y_pitch/2 < res[:, 1]) & (res[:, 1] < y_i+y_pitch/2))[0] # 格子内の点を集める
            res_i = res[i_list, :]
            if len(res_i) == 0: # if: 格子内に点なし
                i_draw_list.append(None)
                continue

            r2_i = ((res_i[:, 0] - x_i) / x_pitch)**2 + ((res_i[:, 1] - y_i) / y_pitch)**2 # 格子中央と点との距離
            i_min = i_list[np.argmin(r2_i)] # 格子中央に最も近い点
            i_draw_list.append(i_min)

    plt.figure(figsize=(6, 6))
    plt.scatter(res[:, 0], res[:, 1], s=10, c=digits.target, cmap=cm.tab10) # 指定範囲内の点の分布を描画
    plt.axis([x_min, x_max, y_min, y_max]); plt.grid(); plt.show()

    draw_digits(i_draw_list, n_grid=n_grid, annosize=annosize, figsize=figsize)

draw_digits_at_tsne(res_umap, -3, 1, 3, 5)
