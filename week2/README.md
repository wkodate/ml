## Index

* [Multivariate Linear Regression](#multivariate-linear-regression)
  * [Multiple Features](#multiple-features)
  * [Gradient Descent for Multiple Variable](#gradient-descent-for-multiple-variable)
  * [Gradient Descent in Practice Ⅰ - Feature Scaling](#gradient-descent-in-practice-Ⅰ---feature-scaling)
  * [Gradient Descent in Practice Ⅱ - Learning Rate](#gradient-descent-in-practice-Ⅱ---learning-rate)
  * [Features and Polynomial Regression](#features-and-polynomial-regression)
* [Computing Parameters Analytically](#computing-parameters-analytically)
  * [Normal Equation](#normal-equation)
* [Octave Tutorial](#parameter-learning)
  * [Basic Operations](#basic-operations)
  * [Moving Data Around](#moving-data-around)
  * [Computing on Data](#computing-on-data)
  * [Plotting Data](#plotting-data)
  * [Control Statements: for, while, if statement](#control-statements-for-while-if-statement)
  * [Vectorization](#vectorization)
  * [Normal Equation Noninvertibility](#normal-equation-noninvertibility)
* [Submitting Programming Assignments](#submitting-programming-assignments)
  * [Working on and Submitting Programming Assignments](#working-on-and-submitting-programming-assignments) 

## Multivariate Linear Regression

#### Multiple Features

* 複数の変数、featureで線形回帰

* 訓練サンプルとfeatureを表す添字の表記の説明
 
![多変数](https://github.com/wkodate/CourseraML/blob/master/week2/images/week2-1-1.png)

* 多変量の目的関数はこれまでのtheta0に対応する変数をx0=1として、n+1次元のthetaの転置行列とxの内積として扱う

![多変数で一般化](https://github.com/wkodate/CourseraML/blob/master/week2/images/week2-1-2.png)

#### Gradient Descent for Multiple Variable

* 多変数の最急降下法におけるパラメータフィッティング

* 単変数と多変数の線形回帰の仮説と目的関数の式の違い。ベクトルで表す

![多変数の仮説と目的変数](https://github.com/wkodate/CourseraML/blob/master/week2/images/week2-1-3.png)

* 単変数と多変数の最急降下法の偏微分項の違い。xj(i)をつけて一般化。x0(i)は0なので等価になる

![多変数の最急降下法](https://github.com/wkodate/CourseraML/blob/master/week2/images/week2-1-4.png)

#### Gradient Descent in Practice Ⅰ - Feature Scaling

* 最急降下法をうまく使うためのテクニック。Feature Scaling

* feature scaling: 異なるfeatureが似たような値を取るように保証しておくと、最急降下法はより早く収束するというアイデア。x1はx2に対して範囲が広すぎるので、featureをスケールすると、等高線が歪まなくなり、収束が早くなる

![Feature Scaling](https://github.com/wkodate/CourseraML/blob/master/week2/images/week2-1-5.png)

* 一般的には、大体-1<=xi<=1の範囲でスケールさせる。x3のレンジが -100<=x3<=100 だとしたら、-1<=x3/100<=1 のようにする

* 完全に同じスケールである必要はない

* Mean normalization(平均正規化)は、xiを xi - μi が大体0になるように置き換える

```
xi <- (xi-ui) /si
```

ui は平均、siは最大から最小を引いた値 

![Mean normalization](https://github.com/wkodate/CourseraML/blob/master/week2/images/week2-1-6.png)

#### Gradient Descent in Practice Ⅱ - Learning Rate

* 最急降下法をうまく使うためのテクニック。Learning Rate

* 最急降下法が正しく烏合ているか確認する方法

* 試行回数に対するJが減少しているかどうかを図示する

* 自動収束テスト

* ラーニングレートが小さすぎると計算が遅い、大きすぎると減少しない

* アルファの値を0.001,0.003 0.01,0.03, 0.1,0.3,1と3倍しながら試していくのが良い

#### Features and Polynomial Regression

* 使うfeatureの選択

* 家の価格を決めるときに間口と奥行きの2つの特徴があった場合、実際に家の価格が決まるのは面積であるので、間口×奥行き=面積を特徴として使う。

* 多項式回帰。二次元のモデルをフィットさせる例

![二次元のモデルをフィットさせる例](https://github.com/wkodate/CourseraML/blob/master/week2/images/week2-1-7.png)

## Computing Parameters Analytically

#### Normal Equation

* 正規方程式: thetaの最適な値を1ステップで解くことができる 

![二次元のモデルをフィットさせる例](https://github.com/wkodate/CourseraML/blob/master/week2/images/week2-2-1.png)

* Octaveだと(X転置 X)の逆行列の計算は1行で記述できる

* 最急降下法と正規方程式の比較

|最急降下法|正規方程式|
|-----------|------------|
|学習率αの選択が必要|学習率αを必要としない|
|多くの繰り返し計算が必要|繰り返し計算を必要としない|
||(X転置 X)の逆行列の計算を必要とする|
|特徴が多い時にうまくいく|特徴が多い時に遅い。訓練セットが10000位になると遅くなり始める|

* フィーチャーがそんなに多くない(1000以下くらい)なら正規方程式、10000くらいから最急降下法を使うのがよい

## Octave Tutorial

#### Basic Operations

* Octaveの使い方の基本的な説明

* 四則演算

* boolean: 1==2 //false, 1~=2 // true 

* AND: 1&&0, OR: 1||0, XOR: xor(1,0)

* PS1を変更: PS1('>> ');

* 複雑なプリント出力: disp(a), disp(sprintf('2 decimals: %0.2f', a))

* 文字列の長さ指定: format short, format long: 

* 行列表示: A=[1 2;3 4;5 6]

* ベクトル表示: a=[1; 2; 3]

* ステップの増分を指定してベクトル: v=1:0.1:2

* 全ての要素が1の行列: ones(2,3)

* 全ての要素が0の行列: zeros(1,2)

* 0~1の乱数の行列: rand(1,3)

* ガウス分布に従った乱数の行列: randn(1,2)

* ヒストグラム表示: hist(A)

* 単位行列: eye(3)

* ヘルプ: help

#### Moving Data Around

* データの操作の説明

* 行列、ベクトルの大きさ: size, length

* ファイル読み込み: load

* メモリ上の変数を表示: who , 詳細表示whos

* メモリ上の変数をクリア: clear

* ファイル書き込み: save

* その行の全ての要素: A[2, :], その列の全ての要素: A[:, 2]

* 行列の連結: C=[A B], C=[A; B]

#### Computing on Data

* データの演算の説明

* 行列の掛け算: A*C

* 行列の要素単位の乗算: A.*B

* 行列の要素単位の二乗: A .^2

* ベクトルの要素単位の逆行列: 1 ./ v

* 行列の要素単位の逆行列: 1 ./ A

* 要素単位のべき乗: exp(A)

* 要素単位の絶対値: abs(A)

* 転置行列: A'

* ベクトルの最大値: max(v)

* aが3以下かどうかのboolean: a <3

* 魔法陣の行列: magic(3)

* 3以上の要素を見つける: find(A >=3)

* すべての要素の加算: sum(a)

* すべての要素の乗算: prod(a)

* 列単位の最大値: max(A, [], 2)

* 行列の要素の最大値: max(max(A))

* 逆行列: pinv(A)

#### Plotting Data

* データのプロットの説明

* プロット: plot(t, y1), プロットを閉じる: close

* データを重ねる: hold on

* グラフの色を変える: plot(t, y1, 'r')

* ラベル: xlabel('time'), ylabel('value'), タイトル:title('my plot') 

* 凡例: legend('sin', 'cos')

* グラフを保存: print -dpng 'myplot.png'

* グラフに番号を指定: figure(2)

* グラフを分割して表示: subplot()

* グラフのメモリ指定: axis([0.5 1 -1 1])

* グラフをクリア: clf

* 行列を可視化: imagesc(A)

* グラフのカラー指定: colorbar, カラーマップ: colormap gray

* 関数呼び出しの連鎖: a=1, b=2, c=3

#### Control Statements: for, while, if statement

* Octaveにおける制御分と関数定義

* for文: for i=1:10, v(i)=2^i; end;

* while文: i=1;while i<=5, v(i)=100;i=i+1;end;

* if文: i=1;while true, v(i)=999; i=i+1; if i== 6, break;end;end;

* 関数の定義:

```
function y squareThisNumber(x)
y=x^2;
```

* Octaveにパス追加: addpath('/User/wkodate')

#### Vectorization

* 計算式をベクトル化して計算を簡単にする話

* 1からnまでの合計を計算(非ベクトル化)→thetaの転置行列との内積を計算(ベクトル化)

* Gradient descentをベクトル化して計算

#### Normal Equation Noninvertibility

* 正規方程式と非可逆性の説明。おまけの題材

* 擬似逆行列pinv, 逆行列inv

* 転置XとXが非可逆(非正則行列) とは？

  1. 学習の問題に対して何らかの冗長なfeatureがある。それぞれのfeatureがが依存しているなど
  2. 大量のfeatureに何らかのアルゴリズムを実行している(featureに対して訓練サンプル数が少ない)
 
## Submitting Programming Assignments

#### Working on and Submitting Programming Assignments

* 課題の取り組み方、宿題の提出の仕方
 1. ml-class-ex1ディレクトリを開く
 2. PDFファイルを読んで提出システムに慣れる
 3. Octaveからディレクトリに移動して関数を実行して確認
 4. submit()の提出スクリプトを実行して提出したいパートを選択
 5. 開いたウィンドウに書いてある提出用のパスワードを入力
 6. Congratulations が出てきたら答えが正しい

