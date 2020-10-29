"""
https://umap-learn.readthedocs.io/en/latest/plotting.html#plotting-larger-datasets
公式リファレンス
"""

import sklearn.datasets
import pandas as pd
import numpy as np
import umap

pendigits = sklearn.datasets.load_digits()
mnist = sklearn.datasets.fetch_openml('mnist_784')
fmnist = sklearn.datasets.fetch_openml('Fashion-MNIST')

%time mapper_mnist = umap.UMAP().fit(pendigits.data)

import umap.plot
umap.plot.points(mapper_mnist) # ただプロットするだけ

umap.plot.points(mapper_mnist, labels=pendigits.target) # 色別にプロット

"""
themeを指定することで簡単にお洒落にすることも可能
fire, viridis, inferno, blue, red, green, darkblue, darkred, darkgreen
"""
umap.plot.points(mapper_mnist, values=pendigits.data.mean(axis=1), theme='fire')

# カラーマップと背景色を指定することも可能
umap.plot.points(mapper_mnist, labels=pendigits.target, color_key_cmap='Paired', background='black')



"""
大きなデータのプロット
umap.plotはデータセットが大きくなると自動的にdatashaderをレンダリングに使用するように切り替える
>>点同士のオーバープロットに騙されなくなる
"""

%time mapper_fmnist = umap.UMAP().fit(fmnist.data)
umap.plot.points(mapper_fmnist)

umap.plot.points(mapper_fmnist, labels=fmnist.target)

"""
インタラクティブなプロットとホバーツール
"""
%time mapper_fmnist30000 = umap.UMAP().fit(fmnist.data[:30000])

# ホバー情報を作成するために全てのデータをデータフレームへ構築する
hover_data = pd.DataFrame({'index':np.arange(30000),
                           'label':fmnist.target[:30000]})

hover_data['item'] = hover_data.label.map(
    {
        '0':'T-shirt/top',
        '1':'Trouser',
        '2':'Pullover',
        '3':'Dress',
        '4':'Coat',
        '5':'Sandal',
        '6':'Shirt',
        '7':'Sneaker',
        '8':'Bag',
        '9':'Ankle Boot',
    }
)

from bokeh.plotting import show, save, output_notebook, output_file
p = umap.plot.interactive(mapper_fmnist30000, labels=fmnist.target[:30000], hover_data=hover_data)
output_file('plot.html')
save(p)


"""
重み付きグラフ
"""
umap.plot.connectivity(mapper_fmnist30000, show_points=True)


"""
診断プロット
"""
"""
主成分分析
公式の直訳
ここで求めているのは、全体的に滑らかな色の遷移と、色の遷移を広く尊重した全体的なレイアウト。このケースでは、左下のクラスターは下から上にかけて濃い緑から青に変化しているが、これは右上のクラスター（真ん中？）とよく一致していて、下の方で青の濃淡があり、その後シアンと青に変化している。右下のクラスター（真ん中下？）は上から下に向かって紫がかったピンク色から緑色に変化しているが、上のクラスタは下端が緑よりも紫がかった色になっており、最適化処理中にこれらのクラスタのうちの1つまたはもう1つが垂直方向に反転してしまい、これが修正されなかったことを示唆している。
"""

%time mapper = umap.UMAP().fit(mnist.data)
umap.plot.diagnostic(mapper, diagnostic_type='pca')

"""
ベクトル量子化
データの3つの代表的な中心を見つけ、各ポイントをこれらの中心からの距離で描出する。
"""
umap.plot.diagnostic(mapper, diagnostic_type='vq')

# 下の2つはよーわからん
local_dims = umap.plot.diagnostic(mapper, diagnostic_type='local_dim')

umap.plot.diagnostic(mapper, diagnostic_type='neighborhood')
