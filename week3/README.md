## Index

* [Classification and Representation](#classification-and-representation)
  * [Classification](#classification)
  * [Hypothesis Representation](#hypothesis-representation)
  * [Decision Boundary](#decision-boundary)
* [Logistic Regression Model](#logistic-regression-model)
  * [Cost Function](#cost-function)
  * [Simplified Cost Function and Gradient Descent](#simplified-cost-function-and-gradient-descent)
  * [Advanced Optimization](#advanced-optimization)
* [Multiclass Classification](#multiclass-classification)
  * [Multiclass Classification: One-vs-all](#multiclass-classification-one-vs-all) 
* [Solving the Problem of Overfitting](#solving-the-problem-of-overfitting)
  * [The Problem of Overfitting](#the-problem-of-overfitting) 
  * [Cost Function](#cost-function-1)
  * [Regularized Linear Regression](#regularized-linear-regression)
  * [Regularized Logistic Regression](#regularized-logistic-regression)

## Classification and Representation

#### Classification

* 分類問題。スパムかどうか、詐欺かどうかを調べる。yが0や1の離散値のときに使う。Negative class(0)とPositive class(1)に分類(バイナリ分類)。0,1,2,3などはマルチクラス分類という

* 分類問題に線形回帰を適用させるのは、多くの場合は良くない。

* ロジスティクス回帰は分類アルゴリズム。仮説は常に0から1の間

#### Hypothesis Representation

* 分類に対してどのように仮説の表現を使っていくか

* シグモイド関数、ロジスティック関数 g(z)

![シグモイド関数、ロジスティック関数](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-1-1.png)

* 仮説モデルの解釈。theraを求めて仮説を使うのは同じ

![仮説モデルの解釈](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-1-1.png)

#### Decision Boundary

* 仮説が0.5以上の時は1, 0.5より小さいときは0。すなわち、theta.'*xが正のときは1, theta.'*xが負のときは0

* 決定境界(Decision Boundary) theta=[-3; 1; 1]のときに-3+x1+x2が0以上のときが1, -3+x1+x2が0以下のときが0となり、x2=-x1+3の直線が決定境界 

* 非線形決定境界。仮説が高次の多項式となっても考え方は同じ。直線じゃなくて円ににもなり得る。

## Logistic Regression Model

#### Cost Function

* ロジスティック回帰で線形回帰のコスト関数を使うと、局所解がとても多い非凸関数(non-convex)になってしまう

![コスト関数](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-2-1.png)

* y=1のとき ロジスティック回帰のコスト関数。仮説が0に近づくにつれてコスト関数は無限大に近づく。仮説が1ならコスト関数は0

![線形回帰のコスト関数(y=1)](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-2-2.png)

* ・y=0のとき 仮説が0ならコスト関数は0。 仮説が1に近づくにつれてコスト関数は無限大に近づく

![線形回帰のコスト関数(y=0)](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-2-3.png)

#### Simplified Cost Function and Gradient Descent

* y=0とy=1のときのロジスティック回帰のコスト関数を一つの式に表す。どちらかの計算をするときにどちらかの項が消える。

![一般的なコスト関数](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-2-4.png)

* コスト関数Jを最小化するためのロジスティック回帰の最急降下法

![ロジスティック回帰の最急降下法](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-2-5.png)

#### Advanced Optimization

* 最急降下法の他にもコスト関数を最適化する方法: 共役勾配法、BFGS、L-BFGS
  * ラーニングレートαを選ぶ必要がない
  * ラインサーチアルゴリズムによって自動的に異なるαを選んで自動的に良いアルファを決定する→最急降下法より早く収束する
  * 最急降下法より複雑→自前で実装せずにソフトウェアライブラリを使うべき

* 実装の例.コスト関数を実装してfminunc(function minimization unconstrained: 制約なし関数最小化)を呼ぶ 

![実装の例](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-2-6.png)

* ロジスティック回帰への適用。コスト関数Jを扱う関数と偏微分を扱う関数を用意する

* 大規模な問題を扱うときは最急降下法ではなくアドバンスドな方法を用いる

## Multiclass Classification

#### Multiclass Classification: One-vs-all

* マルチクラスの分類問題にOne-vs-allアルゴリズムを適用

* 3つのクラスに分類→3つの異なる2クラス分類問題として考える
  * △□×があるとき、△とそれ以外、○とそれ以外、×とそれ以外の3つの2クラス分類問題を解く

## Solving the Problem of Overfitting

#### The Problem of Overfitting

* アンダーフィッティングとオーバーフィッティング。フィーテャーを最適な数にする

* 線形回帰、ロジスティック回帰で共に起こり得る

* オーバーフィッティングの対策
　　1. 特徴の数を減らす
    * 人力で特徴を選ぶ
    * 自動的に特徴の数を減らすアルゴリズム
   2. 正規化
     * 全ての特徴を維持してthetaの倍率を下げる

#### Cost Function

* オーバーフィッティングを防ぐための、正規化で使うコスト関数の話
  * パラメータが小さい値の場合、シンプルな仮説となる
  * 各パラメータを小さく保つ
  
* 正規化コスト関数

![正規化コスト関数](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-3-1.png)

* λ(正規化パラメータ)を大きくすると、コスト関数を最小化するためにθを小さくする必要があるため、仮説はシンプルになりアンダーフィッティングとなる

#### Regularized Linear Regression

* 正規化された最急降下法のアップデート関数

![正規化された最急降下法のアップデート関数](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-3-2.png)

* 各イテレーションごとにθjを少しだけ1より小さくしたものをかけて、いつもどおりの項を引いてアップデートする

* 正規化された正規方程式のアップデート関数 

![正規化された正規方程式のアップデート関数](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-3-3.png)

#### Regularized Logistic Regression

* 正規化されたロジスティック回帰のコスト関数

![正規化されたロジスティック回帰のコスト関数](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-3-4.png)

* 正規化されたロジスティック回帰最急降下法

![正規化されたロジスティック回帰の最急降下法](https://github.com/wkodate/CourseraML/blob/master/week3/images/week3-3-5.png)

