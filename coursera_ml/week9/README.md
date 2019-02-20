# ANOMALY DETECTION

## Density Estimation

#### Problem Motivation

* 与えられたデータセットに対して作られたモデルpによる確率が p(xtest)＜εなら異常、p(xtest)＞εなら正常

* 異常検知の例
  * ユーザの不正検知
    * ユーザのアクティビティの特徴x(i)を使う
    * データからモデルpを作成
    * pがある値ε以下かどうかチェックすることによって普通じゃないユーザを特定
  * 製造業
  * データセンターにあるコンピュータのモニタリング
    * マシンのフィーチャーx(i)を計算。どれだけメモリを使っているか、ディスクアクセス回数、CPU負荷など

#### Gaussian Distribution

* xはガウス分布であることを表す式。NはNormal(正規)を表す

![gaussian distribution](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-1-1.png)

* ガウス分布の式

![gaussian distribution](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-1-2.png)

* μとσを変化させたときのガウス分布の例

![gaussian distribution example](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-1-3.png)

* 平均 μ の式

![mean](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-1-4.png)

* 分散 σ二乗 の式

![distribution](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-1-5.png)

#### Algorithm

* アノマリー検出のアルゴリズム
  1. フィーチャーの選択
  2. パラメータμ1, ..., μn, σ1^2,..., σn^2のフィッティング
    * ![mean distribution](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-1-6.png)
    * ![distribution fitting](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-1-7.png)
  3. 新しいサンプルに対してpを計算し、p(x)＜εならアノマリー
    * ![probability](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-1-8.png)

## Building an Anomaly Detection System

#### Developing and Evaluating an Anomaly Detection System

* 実数によるアノマリー検出アルゴリズムの評価方法

* トレーニングセットにはアノマリーでないサンプルを用意。多少アノマリーが混ざっても構わない

* クロスバリデーションセットとテストセットはアノマリーかどうかのラベル情報も必要

* 航空機のエンジンの例
  * これまで工場で良いエンジン10000, 欠陥エンジン20くらいのエンジンを得ているとする
  * テストセットの分割方法
    * トレーニングセット: 良いエンジン6000(60%)
    * クロスバリデーションセット: 良いエンジン2000, 欠陥エンジン10(20%)
    * テストセット: 良いエンジン2000, 欠陥エンジン10(20%)

* アルゴリズムの評価
  * トレーニングセットでモデルpをフィッティング
  * クロスバリデーションセット、テストセットを使ってyがε以上か以下かでアノマリー予測
  * 評価のマトリックスとして以下を使う
    * True positive, false positive, true negative, false negative
    * 適合率(Precision)と再現率(Recall)
    * F1-score
  * εを選ぶためにクロスバリデーションセットを使う

#### Anomaly Detection vs. Supervised Learning

* どういう時にアノマリー検出を使って、どういう時に教師あり学習を使うか

* アノマリー検出を使う
  * アノマリーのpositiveサンプル(y=1)がとても少ないとき。0-20くらいの数
  * negativeサンプル(y=0)がとても多い時
  * 多くの異なる種類のアノマリーがある
  * 将来新種のアノマリーが発生する可能性があるとき

* 教師あり学習を使う
  * positiveサンプルとnegativeサンプルがとても多いとき
  * 将来現れるであろう陽性のサンプルがある程度似ているとわかっているとき

* アノマリー検出
  * 不正検知
  * 製造業
  * データセンターにあるマシンのモニタリング

* 教師あり学習
  * emailのスパム分類
  * 天気予測
  * がん予測

#### Choosing What Features to Use

* アノマリー検出で何のフィーチャーを使うかが重要

* ガウス分布でないフィーチャーをガウス分布に見えるように以下のように変換する
  * log(x)
  * log(x+c)
  * sqrt(x)
  * -n乗

* 誤差分析
  * 正常なサンプルのpが大きくなることを期待する
  * 新しいフィーチャーを追加して判別に失敗したサンプルを調べる
  * 新しい特徴を追加して判別に失敗したサンプルが正常なサンプルとアノマリーなサンプルを区別されているか確認

* フィーチャの選択例
  * CPUロードと高いネットワークトラフィックのフィーチャーで判別に失敗しているとする
  * 新しい特徴(cpu負荷/ネットワークトラフィック や (cpu負荷)^2/ネットワークトラフィックのようなもの)を作る

## Multivariate Gaussian Distribution

#### Multivariate Gaussian Distribution

* アノマリー検出の拡張

* 多変量ガウス(正規)分布
  * フィーチャーとしてn次元のxを持つ
  * p(x1), p(x2),...と分けずに、これらをまとめてp(x)をモデリング
  * パラメータとしてn次元のμとn×n次元の共分散行列Σを用いる

* 多変量ガウス分布の例
  * Σを変化させたとき
    * ![change sigmas](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-3-1.png)
  * Σの一方のみを変化させたとき
    * ![change one sigma](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-3-2.png)
  * データ同士の相関をモデリング(非対角成分を変化)
    * ![change non-diagonal](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-3-3.png)
  * μを変化
    * ![change mu](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-3-4.png)

#### Anomaly Detection using the Multivariate Gaussian Distribution

* 多変量ガウス分布を使ったアノマリー検出
1.  μとΣをセッティングすることによってトレーニングセットに対しモデルp(x)をフィッティングする
2. 新しい手本が与えられた時にp(x)を計算し、εより小さいかどうかでアノマリーのフラグ付けする

* オリジナルモデル
  * ![original model](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-3-5.png)

* 多変量ガウス分布
  * ![multivariate gaussian model](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-3-6.png)

* 多変量ガウス分布と元のモデルとの間の関係
  * オリジナルのモデルは多変量ガウス分布に制約を加えたものである
  * 制約は、共分散行列Σの非対角成分が0でなくてはならない
  * オリジナルのモデルは等高線が軸に沿ったものとなる

* オリジナルのモデルvs多変量ガウス分布のモデル
  * オリジナルモデル
    * 頻繁に用いられる
    * 異なるフィーチャー同士を組み合わせて自分でフィーチャーを追加する
    * 計算量が少ないので、大きなフィーチャーの数により良くスケールする。フィーチャーn=10,000-100,000でも普通に動く
    * トレーニングセットが少なくてもうまく機能する。mが50,100でもうまく機能する
  * 多変量ガウス分布モデル 
    * 多変量ガウス分布のモデルは自動的にフィーチャー同士の相関を捉えることができる
    * Σの逆行列を計算する必要があり計算量が多いので、大きいフィーチャーにはスケールしない
    * サンプルの数mはフィーチャーの数nより大きくなる必要がある。m>nが成り立たないと、行列Σが可逆じゃなくなる
    * m≫10n のときだけしか使わない
    * Σが特異行列もしくは非可逆となるとき
      * m>nを満たしていない
      * 冗長なフィーチャーがある(x1=x2やx3=x4+x5など)

# RECOMMENDER SYSTEMS


## Predicting Movie Ratings

#### Problem Formulation

* 機械学習の一番重要なアプリケーションとして最も多く聞く回答はレコメンダーシステム

* 記法
  * nu: ユーザの数
  * nm: 映画の数
  * r(i,j): ユーザjが映画iをレーティングしたら1
  * y(i, j): ユーザjが映画iに与えたレート。r(i,j)が1の時のみ定義される

* レーティングをしていないような欠けた値を自動的に埋めてくれるシステムが必要

#### Content Based Recommendations

* コンテントベースのレコメンデーションと呼ばれる

* 映画の例
1. 各ユーザに対しパラメータθベクトルを学習させる
2. ユーザjの映画iのレーティングを(θ(j)Tc(i))で予測

* 公式
  * θ(j): ユーザjのパラメータベクトル
  * x(i): 映画iのフィーチャーベクトル
  * ユーザjと映画iの予測: (θ(j))T(x(i))
  * m(j): ユーザjがレーティングした映画の数

* 目的関数の最適化
  * θ(j)の学習(ユーザjのパラメータ)
    * ![learn theta](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-4-1.png)
  * θ(1), θ(2), ..., θ(nu)の学習
    * ![learn thetas](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-4-2.png)

## Collaborative Filtering

#### Collaborative Filtering

* 協調フィルタリングを使ったレコメンダーシステムの構築

* 実際に誰かが見てそれを利用したフィーチャーありきの話だったが、今回は、ユーザごとのレーティングと、ユーザがどのジャンルの映画が好きかθがわかっている場合にフィーチャーベクトルxを求める

* θ(1), ..., θ(nu)が与えられたときにx(1), ..., x(nm)を学習

![learn x](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-5-1.png)

* 協調フィルタリング
  * x(1), ..., x(nm)と映画のレーティングが与えられたときはθ(1), ..., θ(nm)を見積もることができる
  *  θ(1), ..., θ(nm)が与えられたときはをx(1), ..., x(nm)を見積もることができる
  * ランダムにθの値を予測→xを予測→θを予測→xを予測→... を繰り返すことによって最適な値に収束する

#### Collaborative Filtering Algorithm

* θとxを繰り返し計算してxを解く代わりに、もっと効率的なアルゴリズムがある

* x(1), ..., x(nm)とθ(1), ..., θ(nu)を同時に最小化する目的関数。最初の項では全てのi,jのペアにわたって和を取る。二番目と三番目の項は正規化項。xとθに対して同時に最小化

![learn x and theta](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-5-2.png)

* 協調フィルタリングアルゴリズム
  1. x(1), ..., x(nm)とθ(1), ..., θ(nu)を小さなランダムな値に初期化
  2. 最小降下法もしくは別のアドバンスドなアルゴリズムを使ってを使ってJ(x(1), ..., x(nm), θ(1), ..., θ(nu))を最小化。x0やθ0はなく、xとθはn次のベクトル
    * ![update x and theta](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-5-3.png)
  3. ユーザのパラメータθと映画のフィーチャーxからθTxのレーティングを予測

## Low Rank Matrix Factorization

#### Vectorization: Low Rank Matrix Factorization

* ある映画に対して関連した映画を与える

* 低ランク行列分解。フィーチャーベクトルxの転置を列として積んだ行列Xとパラメータベクトルθの転置を列として積んだ行列Θを使ってXΘTを計算する

* 関連した映画は、各映画iからフィーチャーベクトルx(i)を学習し、フィーチャーベクトルの距離が近い映画jを推薦する||x(i) - x(j)||

#### Implementational Detail: Mean Normalization

* 平均標準化でアルゴリズムが少し良くなる

* 全くレーティングしていないユーザは協調フィルタリングでどのように扱われるのか→n=2とすると、予測をしていないのでy=0となり、θ(5)は0の2次元ベクトルとなってしまい、どの映画に対しても0と予測してしまう

* 平均標準化は各映画のレーティングを平均化したベクトルμを取る
  * 全映画のレーティングから平均のレーティングを引いた行列Yを求める
  * わかっていないYの要素は0
  * 各ユーザjの映画iを予測するために、θ(j)Tx(i)に先ほど引いた平均を加える。なんのレーティングもしていないユーザでこれまで0になってしまった結果は、平均を加える事によって平均値が与えられる

![mean normalization](https://github.com/wkodate/CourseraML/blob/master/week9/images/week9-6-1.png)
