## Index

* [Evaluating a Learning Algorithm](#)
  * [Deciding What to Try Next](#)
  * [Evaluating a Hypothesis](#)
  * [Model Selection and Train/Validation/Test Sets](#)
* [Bias vs. Variance](#)
  * [Diagnosing Bias vs. Variance](#)
  * [Regulation and Bias/Variance](#)
  * [Learning Curves](#)
  * [Deciding What to Do Next Revisited](#)
* [Building a Spam Classifier](#)
  * [Prioritizing What to Work On](#)
  * [Error Analysis](#)
* [Handling Skewed Data](#)
  * [Error Metrics for Skewed Classes](#)
  * [Trading Off Precision and Recall](#)
* [Using Large Data Sets](#)
  * [Data For Machine Learning](#)

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

## Building a Spam Classifier

#### Prioritizing What to Work On

* スパム分類器の構築は、頻出単語から10000-50000くらい選んでこれらをフィーチャーとして使う

* スパム分類器をより良くする上で、次に何を優先にして取り組むべきか
  * トレーニングデータとして利用するスパムのメールを多く集める
  * emailヘッダからemailルーティング情報に基づいたより洗練された特徴を見つける
  * メセージボディ(テキスト)から洗練されたフィーチャーを見つける。discountとdiscountsは同じ?dealとDealerは同じ？句読点や記号についての情報など
  * ミススペルを検出するための洗練されたアルゴリズムの開発。m0rtage, med1cine, w4tches

#### Error Analysis

エラー分析
* 学習の問題に取り組むべきアプローチ
  * シンプルなアルゴリズムで実装。クロスバリデーションデータでテスト
  * 多くのデータが必要か判断するために、学習曲線をプロット
  * エラー分析: クロスバリデーションセットをみて、誤分類となったデータを人力で見ていく。これらのサンプルにシステマティックなパターンが無いかみる

* エラー分析でエラーとなったサンプルを手動でカテゴライズ
  1. emailの種類は何なのか。スパムメールのなかでも薬関係、レプリカ販売、フィッシングなのか
    * 薬関係12, レプリカ4, フィッシング53, その他31だったとすると、フィッシングのメールに対してアルゴリズムがうまく機能していないのかがわかる
  2.  どんな手がかりがあれば、どんなフィーチャーがあればこれらをうまく分類できるのか
    * ミススペル、異常なルーティング、おかしい句読点など のカテゴライズから、検出アルゴリズムをより洗練することができる

* これらによってアルゴリズムの貧弱な部分を素早く見つけることができる

* アルゴリズムを数値的に評価するために、正確さやエラーなど何でもいいが単一の実数値が返ってくることが重要
  * ステミングソフトウェア(Porter stemmerなど)で文字列の一致を判断できるが、このアルゴリズムを使うべきかどうか。ステムありなしでクロスバリデーション誤差を見てみて、ステムを使うのが良いか判断できる
  * 大文字と小文字を区別するべきかどうかなどもそれぞれのクロスバリデーション誤差から判断
  * エラー分析を行うにあたってテストセットではなくクロスバリデーションセットを使うことを強く推奨

## Handling Skewed Data

#### Error Metrics for Skewed Classes

* がんの分類の例で、ロジスティック回帰モデルをトレーニングして、テストセットで1%のエラー。実際には0.5%の患者ががんであり、全ての入力に対してがんではない(y=0)と予測したほうが精度が高くなってしまう。陰性の手本が陰性の手本に比べて極端に少ない。これをスキュークラス

* エラー分析ではエラーを改善したかどうかを明らかにすることができない

* 別の評価指標、精度と再現率
  * y=1がレアなクラスでそれを検出したい
  * 実際のクラス(Actual class)のバイナリ分類と、予測のクラス(Predicted class)の2×2のテーブルで考える
  * Actual class=1, Predicted class=1はTrue positive(真陽性)と呼ばれる手本
  * Actual class=0, Predicted class=0はTrue negative(真陰性)と呼ばれる手本
  * Actual class=1, Predicted class=0はFalse positive(偽陽性)と呼ばれる手本
  * Actual class=0, Predicted class=1はFalse negative(偽陰性)と呼ばれる手本
  * Precisionはがんと予測した患者に対する実際にがんだった患者の割合 
    * True positive / #Predicted positive = True positive / (True pos + False pos)
  * Recallは全てのがん患者に対して、患者ががんだと予測できた割合
    * True positive / #Actual Positive = True positive / (True pos + False neg)

![Precision/Recall](https://github.com/wkodate/CourseraML/blob/master/week6/images/week6-4-1.png)

#### Trading Off Precision and Recall

* PrecisionとRecallのトレードオフ
  * hθ(x)の1,0のしきい値を0.5よりも上げる。確実にがんのときだけがんと告げる=Higher precision, lower recall
  * hθ(x)の1,0のしきい値を0.5よりも下げる。がんの可能性がある患者にはがんと告げる(がんの見逃しを避ける。)=Higher recall, lower precision

* どのようにPrecisionとRecallを決定すればよいか
  * Average: (Precision+Recall)/2は良い指標ではない。Precission=0.02, Recall=1.0でも0.5付近になってしまうため
  * FスコアでPrecisionとRecallの平均をとるものだが、どちらも一定以上の値でないと大きい値にならない。F1スコアとも呼ぶ。
  * P=0 or R=0 → F=0
  * P=1 and R=1 → F=1

![FScore](https://github.com/wkodate/CourseraML/blob/master/week6/images/week6-4-2.png)


## Using Large Data Sets

#### Data For Machine Learning

* 多くのパラメータをもった学習アルゴリズム(=低バイアスアルゴリズム)はJtrainがとても小さくなる

* ここで大量のトレーニングセットがあるときはJtrain(θ)=Jtest(θ)となる。低分散

* これら２つを合わせるとJtestは小さくなる。低バイアス、低分散のアルゴリズムとなる。大量にデータで大量にフィーチャーがあるとき、高いパフォーマンスの学習アルゴリズムを得る

