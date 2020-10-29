"""
https://aotamasaki.hatenablog.com/entry/2018/07/28/220102
https://qiita.com/dl_from_scratch/items/ef5e577cf197a09f98ad#umapを試す
"""

import numpy as np
import pandas as pd
import sklearn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import matplotlib.pyplot as plt
import seaborn as sns

digits = load_digits()
print(digits.DESCR)

# データ内容をみてみる
for i in range(10):
    print("ラベル：",digits.target[i])
    plt.figure(figsize=(1,1))
    plt.imshow(digits.data[i].reshape(8,8))
    plt.show()

X_train, X_test, y_train, y_test = train_test_split(digits.data,
                                                    digits.target,
                                                    stratify=digits.target,
                                                    random_state=42)
print("訓練データの数",len(y_train),"\tテストデータの数",len(y_test))

import umap
%time trans = umap.UMAP(n_neighbors=5, random_state=42).fit(X_train)
# %time trans = umap.UMAP().fit(X_train)

plt.scatter(trans.embedding_[:, 0], trans.embedding_[:, 1], s= 5, c=y_train, cmap='tab10')
plt.title('Embedding of the training set by UMAP', fontsize=15)
plt.colorbar()
plt.show()

#SVMでの学習
svc = SVC().fit(trans.embedding_, y_train)
#k-近傍法での学習
knn = KNeighborsClassifier().fit(trans.embedding_, y_train)

%time test_embedding = trans.transform(X_test)

plt.scatter(test_embedding[:, 0], test_embedding[:, 1], s= 5, c=y_test, cmap='tab10')
plt.title('Embedding of the test set by UMAP', fontsize=15)
plt.colorbar()
plt.show()

print(
    "SVM:", svc.score(test_embedding, y_test),
    "\nk-近傍",knn.score(test_embedding, y_test))

# 7の領域だけみてみる
plt.scatter(test_embedding[:, 0], test_embedding[:, 1], s= 5, c=y_test, cmap='tab10')
plt.axis([-5, -3, -3, 2]) #7の領域だけ表示するようにaxisを入力
plt.show()

i_list = np.where((-4.5 < test_embedding[:, 0]) & (test_embedding[:, 0] < -4.25) & (0 < test_embedding[:, 1]) & (test_embedding[:, 1] < 2))[0]
i_list

for i in i_list:
    print("ID:", i)
    print("ラベル：", y_test[i])
    plt.figure(figsize=(1,1))
    plt.imshow(X_test[i].reshape(8,8))
    plt.show()
