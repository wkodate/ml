## Large Margin Classification

#### Optimization Objective

* SVM(サポートベクターマシーン)教師あり学習で人気のある機械学習アルゴリズム

* SVMのコスト関数は、ロジスティック回帰で使っていたコスト関数を近似した直線になる

![cost function](https://github.com/wkodate/CourseraML/blob/master/week7/images/week7-1-1.png)

![definition of cost](https://github.com/wkodate/CourseraML/blob/master/week7/images/week7-1-2.png)

* コスト関数を最小化したパラメータθを得て、ΘTxが0以上なら1, 0より小さければ0を返す

#### Large Margin Intuition

* パラメータCがとても大きいとき、サンプルとの最小距離が遠い(marginが大きい)決定境界が引ける。大きなマージン分類器(Large Margin Classificaion)と呼ばれる

* Cが大きいほど完全に分離する。これは数式では1/λの正規化パラメータが小さいことに相当

#### Mathematics Behind Margin Classification

* 2つのベクトルの角度が90度以上だとprojection(射影) p は負になる

* 大きいp(ギャップの大きさ)となるような決定境界を選ぶと、θのノルムが小さくすることができる

## Kernels

#### Kernels I

* 非線形の決定境界を引くためのカーネルと呼ばれるテクニック。ランドマークで新しいfeatureを定義

* xと手動で選んだ点landmarkとの類似度をsimilarity関数で測る。このsimilarity関数はガウスカーネル(単にカーネル)と呼ばれる

![similarity function](https://github.com/wkodate/CourseraML/blob/master/week7/images/week7-2-1.png)

* xとlandmarkが近いと、similarityはexp(0)=1に近づき、遠いとexp(-(large number))=0に近づく

* σの二乗は、大きくするほどfeatureはなだらかにゆっくり低下、小さくするほど急にfeatureが低下する

* landmarkの選ぶプロセス
  * xと各landmarkのsimilarityからfeatureを求める(近いとf=1、遠いとf=0)
  * 仮説関数を定義
  * 0より大きいか小さいかを判定して、y=0 or 1に分類
  * 決定境界が決まる

![hyposysis](https://github.com/wkodate/CourseraML/blob/master/week7/images/week7-2-2.png)

#### Kernels Ⅱ

* landmarkを手本と全く同じ場所に置く

* フィーチャーの類似性を各手本のと各featureに対してm+1(0からm)次元のベクトルとする。similarity(x(i), l(i))は必ず1。

* カーネルを用いたSVMの学習アルゴリズム

![SVM minimization algorithm](https://github.com/wkodate/CourseraML/blob/master/week7/images/week7-2-3.png)

* カーネルはロジスティック回帰で用いると実行速度が遅い

* SVMのパラメータ
  * Cが大きい(λ小さい)→低バイアス、高分散(アンダーフィッティング)
  * Cが小さい(ラムダ大きい)→高バイアス、低分散(オーバーフィッティング)
  * σの二乗が大きい→特徴がスムースに変化、高バイアス、低分散(オーバーフィッティング)
  * σの二乗が小さい→特徴がスムースな変化しない、低バイアス、高分散(アンダーフィッティング)

## SVMs in Practice

#### Using An SVM

* 自力で解かずに SVMソフトウェアを使ってパラメータθを解く
  * パラメータCの選択
  * 類似度関数カーネルの選択
    * 使わないときは線形カーネル
    * ガウスカーネル。パラメータσ二乗を選ぶ必要がある

* kernel関数を自分で実装するには、入力から類似度関数を計算して一つの実数を返すソフトウェアを書く

* ガウスカーネルを使う前にフィーチャースケーリングをする必要がある

* カーネルの選択
  * Mercerの定理を満たすカーネルを使う
  * 基本的に線形カーネルかガウスカーネルを使えば良い
  * その他のカーネル 
    * 多項カーネル
    * 文字列カーネル
    * ヒストグラムカーネル

* SVMでマルチちクラス分類をするときは、on vs allでやる。ほとんどのライブラリがビルトインで提供されている

* ロジスティック回帰とSVM
  * もしfeatureのnがトレーニングサイズmと比べて大きい場合(n=10,000, m=10-1000のとき)、ロジスティック回帰もしくは線形カーネルのSVMを使う
  * もしfeatureのnが小さくトレーニングサイズmが中くらいの大きさの場合(n=1-1000, m=10-10000)、ガウスカーネルを使ったSVMを使う
  * もしfeatureのnが小さく、トレーニングサンプルの数が大きい場合(n=1-1000, m=50000+)、手動でfeatureを追加して、ロジスティック回線か線形カーネルを使ったSVMを使う

* ロジスティック回帰とカーネルなしのSVMは似てる

* ニューラルネットワークはうまく機能するがトレーニングには遅い
