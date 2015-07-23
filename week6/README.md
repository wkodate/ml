## Index

* [Evaluating a Learning Algorithm](#)
  * [Deciding What to Try Next](#)
  * [Evaluating a Hypothesis](#)
  * [Model Selection and Train/Validation/Test Sets](#)

## Evaluating a Learning Algorithm

#### Deciding What to Try Next

* 予測と大きな誤差があったときに、以下のことをなんとなく試して時間を浪費してしまう
  * より多くのtraining exampleを取得
  * より少ない数のフィーチャーを使う
  * フィーチャーを追加する
  * フィーチャーの多項式を追加する
  * λを減らす
  * λを増やす

* Machine Leaarning Diagnostic: 機械学習診断 でパフォーマンスを改善するためのベストな方法を知ることができる

#### Evaluating a Hypothesis

* フィーチャーが増えてくると単純にプロットして仮説を評価するのは難しい

* データを2つの部分に分ける。最初はトレーニングセット、もう一方がテストセット
  * 割合は7:3くらい
  * 順番があるならランダムに選ぶ

*  線形回帰のトレーニングとテストの手順
  1. 全体の70%を使ってトレーニングデータからthetaを学習(トレーニング誤差Jの最小化)
  2. 全体の30%を使ってテストセットの誤差を計算

* ロジスティック回帰のトレーニングとテストの手順
  1. 全体の70%を使ってトレーニングデータからthetaを学習(トレーニング誤差Jの最小化)
  2. 全体の30%を使ってテストセットの誤差を計算
  3. 0,1の誤判別の誤差関数から平均テスト誤差で評価

![cost](https://github.com/wkodate/CourseraML/blob/master/week6/images/week6-1-1.png)

#### Model Selection and Train/Validation/Test Sets

*  何次の多項式まで含めてフィットさせたいか、つまり何のフィーチャーを使うか、ラムダをどうするか(モデル選択問題)

* モデル選択問題

多項式の次数d :degree of polynomial

1. トレーニングセットを使ってΘのパラメータを最適化
2. テストセットを使って最も誤差の少ないpolynomial degreeを見つける
3. Jtestのテストセットを使ってgeneralization error(汎化誤差)をを見積もる

* トレーニング誤差, クロスバリデーション誤差, テストセット誤差

を使う

1. トレーニングセットを使ってΘのパラメータを最適化(60%)
2. クロスバリデーションセットを使って最も誤差の少ないpolynomial degreeを見つける(20%)
3. Jtestのテストセットを使ってgeneralization error(汎化誤差)をを見積もる(20%)


## Bias vs. Variance

#### Diagnosing Bias vs. Variance

* 期待通りの結果が得られないときは、大体は高いバイアスの問題か高い分散の問題(アンダーフィッティングかオーバーフィッティングか)

* トレーニング誤差とクロスバリデーション誤差を次数と誤差の関係
  * トレーニング誤差は次数が増えるにつれて減少
  * クロスバリデーション誤差はある点まで減少した後、増加する

* うまくフィッティングしないときにアンダーフィッティングかオーバーフィッティングか
  * 高バイアス問題(アンダーフィット)のときはJtrainが高くJcvとJtrainはだいたい同じ
  * 高分散問題 Jtrainは低くなり、Jcv >> Jtrainとなる

![bias vs variance](https://github.com/wkodate/CourseraML/blob/master/week6/images/week6-2-1.png)

#### Regulation and Bias/Variance

* λの選択
  * Jtrain, Jcv, Jtestの正規化項なし
  * λ=0, 0.01, 0.02, 0.04, 0.08,...,10で順に試してminJ(Θ)となるΘでJcvを出す。
 * ここから一番クロスバリデーション誤差が小さい次数を選ぶ

* JtrainとJcvのラムダとJ(Θ)の関係

![regulation and bias/variance](https://github.com/wkodate/CourseraML/blob/master/week6/images/week6-2-2.png)

#### Learning Curves

* 学習曲線をプロットすると、アルゴリズムの妥当性やパフォーマンス改善に役立つ

* トレーニングサンプルの数に対する誤差。
  * トレーニング誤差Jtrain: トレーニングセットの賤が小さいほど誤差は小さくなり、大きいほど増える
誤差が大きくなると全てのトレーニングサンプルにフィットさせることが難しくなるため

  * クロスバリデーション誤差Jcv: トレーニングセットの数を大きくすることによって仮説はより正しくなり、フィッティングするようになる
    トレーニングセットの数が小さいほどテストセットの誤差は大きくなる

* 高バイアス(アンダーフィッティング)のときのトレーニングセット数に対する誤差
  * クロスバリデーション誤差Jcv: データがすごく少ないとき誤差は大きくなり、データを増やしても直線はあまり変わらない

  * トレーニング誤差Jtrain: データが少ないと誤差は少なく、データが増えるにつれてクロスバリデーション誤差と同じ漢字で高い

 * 高バイアスのときは、トレーニングデータを増やしてもあまり意味が無い

![LearningCurve-high bias](https://github.com/wkodate/CourseraML/blob/master/week6/images/week6-2-3.png)

* 高分散(オーバーフィッティング)の時のトレーニングセット数に対する誤差
  * トレーニング誤差Jtrain: トレーニングセットが小さいとフィットするので誤差は小さくなる。トレーニングセットを増やしても、多少は誤差は増えるがあまり変わらない

  * クロスバリデーション誤差Jcv: クロスバリデーション誤差は高いまま、ある程度増やしたとしても誤差は小さくはならない

  * トレーニング誤差とクロスバリデーション誤差には大きな差があるが、トレーニングセットを増やし続けると、トレーニング誤差とクロスバリデーション誤差は同じところに収束する

  * 高分散のときは、トレーニングデータを増やすのが良い

![LearningCurve-high variance](https://github.com/wkodate/CourseraML/blob/master/week6/images/week6-2-4.png)

* 学習曲線を書くことによって、問題が高バイアスか高分散かわかる

#### Deciding What to Do Next Revisited

* 仮説が正しくないときの対応と解決できる問題
  * トレーニングサンプルを増やす → 高分散をfix
  * フィーチャーを減らす → 高分散をfix
  * フィーチャーを追加する → 高バイアスをfix
  * 多項式のフィーチャーを増やす → 高バイアスをfix
  * λを減らす → 高バイアスをfix
  * λを増やす → 高分散をfix

* 小さなニューラルネットワーク(隠れ層が少ない)のときはパラメータが少なく、アンダーフィッティングになりがち

* 大きなニューラルネットワーク(隠れ層が多き)のときはパラメータが多く、オーバーフィッティングになりがち

