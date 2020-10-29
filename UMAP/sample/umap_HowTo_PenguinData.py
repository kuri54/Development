"""
https://umap-learn.readthedocs.io/en/latest/basic_usage.html
公式リファレンス
"""
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style='white', context='notebook', rc={'figure.figsize':(14,10)})

penguins = pd.read_csv("https://github.com/allisonhorst/palmerpenguins/raw/5b5891f01b52ae26ad8cb9755ec93672f49328a8/data/penguins_size.csv")
penguins.head()

penguins = penguins.dropna() # NA除去
penguins.species_short.value_counts()

"""
データセットの詳細：https://umap-learn.readthedocs.io/en/latest/basic_usage.html
3種のペンギン：Adelie、Gentoo、Chinstrap
ヒレの長さ、体重、性別、クチバシの長さ/厚みなどのデータを含んでいる
"""

# 種ごとの全データを一括してプロット
sns.pairplot(penguins, hue='species_short')

"""
UMAPで次元削減し、データ構造を可視化する。

UMAPオブジェクトを作成
データをきれいにする
・NA値は必要ない。
・測定値だけが必要。
・各特徴をz-score（平均が0、標準偏差 (SD) が1になるように変換したもの）に変換。
"""

import umap
reducer = umap.UMAP()
penguin_data = penguins[["culmen_length_mm", "culmen_depth_mm", "flipper_length_mm", "body_mass_g", ]].values
scaled_penguin_data = StandardScaler().fit_transform(penguin_data)

embedding = reducer.fit_transform(scaled_penguin_data)
embedding.shape
"""
上の結果 -> (334, 2)：334の配列と2つの特徴列
最初は特徴が4つあったが、2つに次元削減された
結果、標準的な散布図にプロットできるようになった
"""

plt.scatter(
    embedding[:, 0],
    embedding[:, 1],
    c=[sns.color_palette()[x] for x in penguins.species_short.map({"Adelie":0, "Chinstrap":1, "Gentoo":2})])
plt.gca().set_aspect('equal', 'datalim')
plt.title('UMAP projection of the Penguin dataset', fontsize=24)
