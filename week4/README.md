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
