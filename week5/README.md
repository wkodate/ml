## Index

* [Cost Function and Backpropagation](#)
  * [Cost Function](#)
  * [Backpropagation Algorithm](#)
  * [Backpropagation Intuition](#)
* [Backpropagation in Practice](#)
  * [Implementation Note: Unrolling Parameters](#)
  * [Gradient Checking](#)
  * [Random Initialization](#)
  * [Putting It Together](#)
* [Application of Neural Networks](#)
  * [Autonomous Driving](#)

## Cost Function and Backpropagation

#### Cost Function

* バイナリ分類。出力ユニット一つ。(1次元のベクトルを出力)

* マルチクラス分類。出力ユニット3以上

* ニューラルネットワークのコスト関数

![ニューラルネットワークのコスト関数](https://github.com/wkodate/CourseraML/blob/master/week5/images/week5-1-1.png)

#### Backpropagation Algorithm

* コスト関数を最適化するアルゴリズムとしてバックプロパゲーション。コスト関数の偏微分項をどうやって計算するか

* 仮説からターゲットを引く

* 出力項から各ノードごとにデルタ項を計算していくことによって、偏微分の項を手早く計算できる

* 入力レイヤに対応した誤差はないので、δ0はなし

* アルゴリズム
  * フォワードプロパゲーションを使ってアクティベーションを計算
  * yを使ってアクティベーションとyの誤差を計算
  * Δを更新
  * 書くトレーニングセットに対して繰り返す

![アルゴリズム](https://github.com/wkodate/CourseraML/blob/master/week5/images/week5-1-2.png)

#### Backpropagation Intuition

* コスト関数はニューラルネットワークの出力と実際の値の差分の二乗と考えて良い

* コストのiはどのくらいのネットワークがうまく手本iを予測しているかを測っている

![コスト](https://github.com/wkodate/CourseraML/blob/master/week5/images/week5-1-3.png)

## Backpropagation in Practice

#### Implementation Note: Unrolling Parameters

* 行列からベクトルへのパラメータのアンロール

* costFunctionが返すgradientはこれまではベクトルだったが、ニューラルネットワークでは行列となる。

* これを一つのベクトルにアンロール(展開)する方法

![ベクトルをアンロール](https://github.com/wkodate/CourseraML/blob/master/week5/images/week5-2-1.png)

ベクトルから行列に戻す方法もある

![ベクトルを行列に戻す](https://github.com/wkodate/CourseraML/blob/master/week5/images/week5-2-2.png)

#### Gradient Checking

* Gradient Checkingを実装するとフォワードプロパゲーションやバックプロパゲーションのバグを見つけることができる

* バックプロパゲーションのgradと自分で計算した数値的な微分計算によってgradが近い値かどうかで確認する

![Gradient checking](https://github.com/wkodate/CourseraML/blob/master/week5/images/week5-2-3.png)

1. バックプロパゲーションを自走してDVecを計算
2. gradient checkingを計算
3. これらを小数第二位、第三位レベルで確認
4. バックプロパゲーションのコードが正しいとわかったら、gradient checkingを切って、学習にバックプロパゲーションのコードを用いる

#### Random Initialization

* ロジスティック回帰の時はθの初期化は全て0でうまくいったが、ニューラルネットワークではユニットの値が同じになってしまいうまくいかない

* 全てのユニットが同じフィーチャーとなる

* Θのランダムに初期化する

* Symmetry beaking : ランダム初期化で対称性を破る。randに-ε, εのウェイトを掛けてランダムに初期化

#### Putting It Together

* ネットワークアーキテクチャの選定。レイヤーとユニットの数を選定
  * 入力ユニット数: 特徴の次元数
  * 出力ユニット数: クラスの数
  * 隠れレイヤ: 基本1層。1層より多い場合は隠れユニットの数は各レイヤで同じにする。
    * 隠れユニットは多いほどいいが、計算量はその分多くなる
    * 各レイヤの隠れユニットの総数は、だいたいx次元と同じフィーチャーの数と同じもしくは2-4倍の適当な数

* ニューラルネットワークのトレーニング
  * ウェイトをランダムに初期化
  * xから仮説hを得るためにフォワードプロパゲーションを実装
  * コスト関数Jの計算のコードを実装
  * コスト関数の偏微分の項を計算するためにバックプロパゲーションを実装
    * サンプルに対してforを回してフォワードプロパゲーションとバックプロパゲーションの実装
    * アクティベーションとδを得る
    * Δのアップデート
  * バックプロパゲーションとgradient checking 偏微分項を比較。比較したらgtradient checkingをdiableにする
  * 最急降下法やL-BFGS, Conjugate, fminuncなどの最適なメソッドとバックプロパゲーションでコスト関数の最小化を試みる

## Application of Neural Networks

#### Autonomous Driving

* ニューラルネットワークの学習の例

* 道路の映像と人のステアリングから車が運転を学習する例

* 初期はランダムだが、1秒に12回、2分くらいトレーニングすると正確に模倣するようになる
