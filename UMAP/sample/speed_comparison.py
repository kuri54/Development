"""
https://cpp-learning.com/pca-umap/
PCA、t-SNE、UMAPの速度比較
"""

import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style='white', context='notebook', rc={'figure.figsize':(14,10)})

X, y = load_digits(return_X_y=True)

def plot_gallery(images, labels, h=8, w=8, n_row=2, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.4 * n_col, 2.0 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(labels[i], size=16)
        plt.xticks(())
        plt.yticks(())

# 数枚を可視化
plot_gallery(X, y)

def plot_pca(x, y, colormap=plt.cm.Paired):
    '''Visualize features with PCA'''
    plt.figure(figsize=(8, 6))

    # clean the figure
    plt.clf()

    reducer = PCA(n_components=2, random_state=0)
    x_embedded = reducer.fit_transform(x)
    plt.scatter(x_embedded[:, 0], x_embedded[:, 1], c=y, cmap=colormap)
    plt.colorbar()

    plt.title("Embedding Space with PCA")
    plt.show()

def plot_tsne(x, y, colormap=plt.cm.Paired):
    '''Visualize features with t-SNE'''
    plt.figure(figsize=(8, 6))

    # clean the figure
    plt.clf()

    reducer = TSNE(n_components=2, random_state=0, perplexity=5)
    x_embedded = reducer.fit_transform(x)
    plt.scatter(x_embedded[:, 0], x_embedded[:, 1], c=y, cmap=colormap)
    plt.colorbar()

    plt.title("Embedding Space with t-SNE")
    plt.show()

def plot_umap(x, y, colormap=plt.cm.Paired):
    '''Visualize features with UMAP'''
    plt.figure(figsize=(8, 6))

    # clean the figure
    plt.clf()

    reducer = umap.UMAP(n_components=2, random_state=0, n_neighbors=5)
    x_embedded = reducer.fit_transform(x)
    plt.scatter(x_embedded[:, 0], x_embedded[:, 1], c=y, cmap=colormap)
    plt.colorbar()

    plt.title("Embedding Space with UMAP")
    plt.show()

def plot_pca_umap(x, y, colormap=plt.cm.Paired):
    '''Visualize features with PCA'''
    plt.figure(figsize=(8, 6))

    # clean the figure
    plt.clf()

    pca = PCA(n_components=40, random_state=0)
    reducer = umap.UMAP(n_components=2, random_state=0, n_neighbors=5)
    pca_x = pca.fit_transform(x)
    x_embedded = reducer.fit_transform(pca_x)

    plt.scatter(x_embedded[:, 0], x_embedded[:, 1], c=y, cmap=colormap)
    plt.colorbar()

    plt.title("Embedding Space with PCA and UMAP")
    plt.show()


# Visualize features
plot_pca(X, y , 'Spectral')
plot_tsne(X, y, 'Spectral')
plot_umap(X, y , 'Spectral')
plot_pca_umap(X, y, 'Spectral')
