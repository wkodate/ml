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

[W,s,v] = svd((repmat(sum(x.*x,1),size(x,1),1).*x)*x');

