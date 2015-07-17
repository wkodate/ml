## Index

* [Motivations]()
  * [Non-linear Hypotheses]()
  * [Hypothesis Representation]()

## Motivations

#### Non-linear Hypotheses

* 非線形の分類ではfeatureの数が多くなり、オーバーフィットとなってしまう

* 例えばコンピュータが画像から車を認識するとき、ピクセル輝度のマトリックスを見て判断している

* 50pixels*50pixelsの小さい画像でもn=2500となる。RGBを使う場合は、0-255の値となるので、n=7500
二次の特徴(xi × xj)は3,000,000featuresまでになる
→ロジスティック回帰を非線形で学習させるには向いていない

#### Neurons and the Brain

* 脳が勝手に学習する→これを機械学習のアルゴリズムに応用

## Neural Networks

#### Model Representation Ⅰ

* ニューロンを単なるロジスティックの単位としてモデル化する

![ニューロンモデル](https://github.com/wkodate/CourseraML/blob/master/week4/images/week4-2-1.png)

* x0はバイアスユニットと呼ばれ、必ず1になる

* 用語の話
  * sigmoid関数はactivation関数と呼ぶ
  * モデルはweights(parameters)と呼ぶ
  * 最初のレイヤーxは入力レイヤー、最後のレイヤーyは出力レイヤー、あいだのレイヤーaは隠れたレイヤー
  * a(j)i: レイヤーjのニューロン(ユニット)iのアクティベーション(シグモイド)
  * θ(j): レイヤーjからレイヤーj+1のマッピング関数をコントロールする重みの行列

* 一つの隠れ層があるときの各アクティベーションノードと仮説

![隠れ層のアクティベーション](https://github.com/wkodate/CourseraML/blob/master/week4/images/week4-2-2.png)

![隠れ層のアクティベーション(詳細)](https://github.com/wkodate/CourseraML/blob/master/week4/images/week4-2-3.png)

* レイヤーjがsjユニット、レイヤーj+1が sj+1ユニット のネットワークでは、θ(j)はのsj+1×(sj +1)次元になる

#### Model Representation Ⅱ

* フォワードプロパゲーションのベクトル化

![フォワードプロパゲーションのベクトル化](https://github.com/wkodate/CourseraML/blob/master/week4/images/week4-2-4.png)

![フォワードプロパゲーションのベクトル化2](https://github.com/wkodate/CourseraML/blob/master/week4/images/week4-2-5.png)

* 最終的な仮説

![仮説の式](https://github.com/wkodate/CourseraML/blob/master/week4/images/week4-2-6.png)


* フォワードプロパゲーション: 入力から始めて、隠れ層に対して前方(フォワード)に伝搬(プロパゲート)させてアクティベーションを計算し、
それを更に前方へ伝搬させていって、出力レイヤーのアクティベーションを計算

* ニューラルネットワークはロジスティック回帰の入力をx1, x2, x3に制限する代わりに、独自のfeature a1, a2, a3を学習して、
それをロジスティック回帰として考える

* ニューラルネットワークがどう接続されるかはアーキテクチャと呼ばれる

## Application

#### Examples and Intuitions Ⅰ

* 非線形の決定境界。x1, x2がバイナリ(0 or 1)のときに、XOR/XNORやAND, ORで表すことができる

* AND: Θ = [-30, +20, +20], hΘ(x) = g(-30 + 20x1 + 20x2)

| x1 | x2 | hΘ(x)|
|----|----|-------|
| 0 | 0 | g(-30)→0 |
| 0 | 1 | g(-10)→0 |
| 1 | 0 | g(-10)→0 |
| 1 | 1 | g(10)→1 |

* OR: Θ = [-10, +20, +20], hΘ(x) = g(-10 + 20x1 + 20x2)

| x1 | x2 | hΘ(x)|
|----|----|-------|
| 0 | 0 | g(-10)→0 |
| 0 | 1 | g(10)→1 |
| 1 | 0 | g(10)→1 |
| 1 | 1 | g(30)→1 |

#### Examples and Intuitions Ⅱ

* NOT: Θ = [10, -20], hΘ(x) = g(10 - 20x1) 負の大きなウェイトを否定したい変数におく

| x1 | hΘ(x)|
|----|-------|
| 0 | g(10)→1 |
| 1 | g(-10)→0 |

* (NOT x1) AND (NOT x2): Θ=[-10, 20, 20]

* XOR

* 手書きの数字をニューラルネットワークで判別できる

#### Multiclass Classification

* マルチクラス分類: One-vs-allと同じ考え方。出力層が多次元。結果のクラスは以下のように定義される

![マルチクラス分類の結果](https://github.com/wkodate/CourseraML/blob/master/week4/images/week4-3-1.png)
