## Index

* [Introduction](#introduction)
  * [Welcome](#welcome)
  * [Supervised Learning(教師あり学習)](#supervised-learning教師あり学習)
  * [Unsupervised Learning(教師なし学習)](#unsupervised-learning教師なし学習)
* [Model and Cost Function](#model-and-cost-function)
  * [Model Representation](#model-representation)
  * [Cost Function(目的関数)](#cost-function目的関数)
  * [Cost Function - Intuition Ⅰ](#cost-function---intuition-Ⅰ)
  * [Cost Function - Intuition Ⅱ](#cost-function---intuition-Ⅱ)

## Introduction

#### Welcome

* 機械学習はAI、人口知能の分野から派生

```
Tom Mitchell provides a more modern definition: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."
```

* 例

  * データベースマイニング - webクリックデータ、電子カルテ、生物学、エンジニアリング

  * 手作業が不可能なアプリケーション - ヘリコプターの自動操作、手書き認識、自然言語処理、コンピュータビジョン

  * 自己カスタマイズプログラム - レコメンデーション
  
  * 人間の学習の理解(AI)

#### Supervised Learning(教師あり学習)

* 教師あり学習は、**データセットのすべてのサンプルについて正しい答えが与えられており、アルゴリズムに予測させる**
  * **回帰問題(regression problems)は連続出力の予測**
  * **分類問題(classification problems)は離散値出力の予測**

* 家の大きさと値段の一覧(正しい答え)から、特定の大きさの値段を予測。回帰(Regression, 連続的な属性の値を予測)問題とも言う。
  * 腫瘍のサイズに対する良性0、悪性1のデータから分類
  * 腫瘍のサイズに対するその人の年齢のデータ群から直線を引いて、友人のがんを予測。年齢のほか日も腫瘍の厚み、サイズの均一性などの特徴も使える

#### Unsupervised Learning(教師なし学習)

* 教師なし学習アルゴリズムは、**ラベル付けされていないデータセットをクラスタリングする**

* news.google.comでは、取得してきたニュースをクラスタリングしてまとめている

* コンピュータクラスタの最適化、ソーシャルネットワーク解析、マーケット・セグメンテーション、天文学データ解析

* 2つ声が録音されたのマイクロフォンの録音を、教師なし学習で分離。カクテルパーティ効果という。Octaveのプログラムで1行で書ける

```
[W,s,v] = svd((repmat(sum(x.*x,1),size(x,1),1).*x)*x');
```

## Model and Cost Function

#### Model Representation

*  線形回帰のモデル

![線形回帰のモデル](https://github.com/wkodate/CourseraML/blob/master/week1/images/week1-2-1.png)

*  このコースの記号表記方法

![このコースの記号表記方法](https://github.com/wkodate/CourseraML/blob/master/week1/images/week1-2-2.png)

m: 訓練サンプルの数, x's: 入力変数/特徴, y's: 出力変数/目的変数, (x,y): 1件の訓練サンプル, (x(i),y(i)): i番目の訓練サンプル

* 訓練セットを学習アルゴリズムに読み込ませある関数hを出力。hはhypothesis(仮説)。この関数hに、例えば家のサイズを入力すると見積もられる値段が返ってくる

```
  hθ(x) = θ0 + θ1 * x
  θi: モデルパラメータ
```
 
* yをxの線形関数として予測する という意味

* theta i をモデルパラメータという
  
* **このモデルを線形回帰と呼び、変数がひとつの場合の線形回帰であり、その変数はxとなる。全ての価格を一つの変数xのみで予測。単回帰ともいう**

![線形回帰のモデル](https://github.com/wkodate/CourseraML/blob/master/week1/images/week1-2-3.png)

#### Cost Function(目的関数)

* 目的関数を定義する。これは、データに対しどのように最適な直線を当てはめるかを算出するために役立つ。 

![定義](https://github.com/wkodate/CourseraML/blob/master/week1/images/week1-2-4.png)

* θ0とθ1の値を見つける目的関数

平均ではなく、実際には1/2mを掛ける二乗誤差の総和が最小化されるようにするのが条件。差は、訓練セットに対する予測値から訓練セットの実際の家の価格を引いたもの

最小化するパラメータはtheta0, theta1, 目的関数はJ(theta0, theta1)。目的関数は、二乗誤差関数、二乗誤差目的関数と呼ばれる。

![目的関数](https://github.com/wkodate/CourseraML/blob/master/week1/images/week1-2-5.png)

#### Cost Function - Intuition Ⅰ

* いくつかの具体例で、目的関数が何をしていてなぜそれを使いたいのかを説明。今回はtheta0を0に固定してtheta1のみで考える

![目的関数をシンプルに考える](https://github.com/wkodate/CourseraML/blob/master/week1/images/week1-2-6.png)

* theta 1のそれぞれの値は異なる仮説に対応。学習アルゴリズムの最適化の目的は、目的関数を最小化するためのtheta 1を選択すること。予測値と実測値との差分が最も小さいtheta0, theta1を求める。theta1に対する目的関数は二次関数の曲線のグラフになる

![目的関数のグラフ](https://github.com/wkodate/CourseraML/blob/master/week1/images/week1-2-7.png)

#### Cost Function - Intuition Ⅱ

* 等高線でtheta0, theta1の両方を変化させたときの目的関数の可視化

* theta0, theta1に対する目的関数は3次元的なグラフになる

![目的関数の3次元グラフ](https://github.com/wkodate/CourseraML/blob/master/week1/images/week1-2-8.png)

* これらのグラフを書いて目視で最小値を見つけるのはダメ。自動的に目的関数Jを最小化するようなtheta0, theta1を見つけるアルゴリズムがほしい
