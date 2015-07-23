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

![ロジスティック回帰のトレーニングとテスト](https://github.com/wkodate/CourseraML/blob/master/week6/images/week6-1-1.png)

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

