## Index

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
