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

#### Platting Data

#### Control Statements: for, while, if statement

#### Vectorization

#### Normal Equation Noninvertibility
