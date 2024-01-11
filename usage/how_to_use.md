# 使い方
## 1. ディレクトリ構成
```
my_simblock
+-- Average_time
|   +-- average_time.txt
+-- Fork_probability
|   +-- forkprobability.txt
+-- Blocklists
|   +-- blockList-0000100000
|   +-- blockList-0000500000
|   :
|   +-- blockList-1000000000
+-- Stdouts
|   +-- result-0000100000
|   +-- result-0000500000
|   :
|   +-- result-1000000000
+-- Results_graph
|   +-- file(n)
+-- simblock
|   +-- ...

```

## 2-a. プログラムの実行方法
```
$python3 All_simulation.py
```

結果は、my_simblock/results_graph/file(n)(n=1,2,…)ディレクトリ配下に格納されます。

nが大きいほど最新の実行結果です。

file(n)内には、自動的に実行時のパラメータ設定を記載したファイル（settings_note.txt）が保存されるようになっています。

> 項目[実行した時刻, interval, ノードの数, 変えたパラメータとその数値リスト]

シミュレーション過程で出力されたファイル群を消去するコマンドも含まれたプログラムです。

以下のコマンドで削除のみを行うこともできます。
```
$python3 dust.py
```

**sesult_graphに出力されたグラフはすべて残るので、安心して消してください。**

## 2-b. 個別の実行方法
四段階に分かれています。

1から順に実行してください。2~4はまとめて実行することもできます。

1. シミュレーションの実行
```
$python3 repeat_simulation.py
```
2. フォーク確率の計算＋グラフの出力
```
$ python3 calculate_fork_probability.py ./blocklists/*
```
3. 平均ブロック伝搬時間の計算＋グラフの出力
```
$ python3 calculate_average_blockprop_time.py ./stdouts/*
```
4. パフォーマンスの計算＋グラフの出力
```
$ python3 calculate_performance.py
```
※2以降をまとめて実行
```
$ python3 run_analyses.py
```



## 3. パラメータの変更方法
### ◆para.pyから変えられるもの
**ブロック伝搬時間、伝搬率、ノード数、変更しているパラメータの数値範囲（リスト）（と変更しているパラメータの名前）**


+ parameter_list : 変更したパラメータの数値範囲を変更できます(単位B)
> 例:1KB～1MBにしたいとき
>
> parameter_list = [1000, 5000, 10000, 50000, ...]
> 
+ interval : ブロック伝搬時間間隔を変更できます(単位ms)
> 例:10分から5分にしたいとき
>
> interval = 1000×60×10 →　interval = 1000×60×5
>
+ propagation_rate : ノード全体に対して、どれくらいブロックを伝搬させるかを指定できます(割合で指定)
> 例:10割から5割にしたいとき
>
> propagation_rate = 1.0 → propagation_rate = 0.5
>
+ node_num : 任意のノード数を指定できます
> 例:300個から400個にしたいとき
>
> node_num = 300 → node_num = 400

+ paraname_list : ブロックサイズ以外のパラメータ変更をする場合、このリストに名前を追加してください。
> 例：Intervalを追加したいとき
> 
> [‘Blocksize’]→[‘Blocksize’, ‘Interval’,…]
> 
+ paranum : 上記リストの添え字です。どのパラメータを変更しているのかを指定します。出力されるファイルの名前等に影響します。
> 例1: Blocksizeを指定したいとき
>
> paranum = 0
>
> 例2: Intervalを指定したいとき
>
> paranum =1

### ◆その他
これ以外のシミュレーション時に固定するパラメータの数値はSimulationConfiguration.javaから直接変更してください。
> my_simblock/simblock/simulator/src/main/java/simblock/settings/

**横軸に取りたい値（今回のブロックサイズにあたるもの）を変更する場合はrepeat_simulation.pyの書き換えが必要です。**

## 4. 結果の見方
result_graphディレクトリに4つの結果（グラフ）と1つのテキストファイルが保存されます。

> result_graph内のfile(n)のnは、
> 1. シミュレーション実行時にresult_graph内にすでに存在するディレクトリ数を数える
> 2. その数に+1した数字を次の結果ファイルのnとする
> 
> といった形で決められています。
>
> ⇒　数字が新しいほど最新の実行結果です。
>
> 不安な場合は、settings_note.txtのタイムスタンプ欄から時刻の確認をお願いします。

### ◆ディレクトリの中身
+ M_time-plot.png : 横軸ブロックサイズ[B]、縦軸平均ブロック伝搬時間M[ms]

+ avstd-plot.png : 横軸ブロックサイズ[B]、縦軸平均ブロック伝搬時間の標準偏差

+ Pfork-plot.png : 横軸ブロックサイズ[B]、縦軸フォーク確率Pfork

+ result.png : 横軸ブロックサイズ[B]、縦軸パフォーマンスP

+ settings_note.txt : 実行時のタイムスタンプとパラメータについての記録（1.実行方法を参照）

## 5. 各プログラムの関係性
**メイン**

| プログラム名  | 役割 |
| ------------- | ------------- |
|  All_simulation.py  | repeat_simulation.pyとrun_analyses.pyを一括で実行  |
| repeat_simulation.py  | シミュレーションの実行と、その結果を指定した場所に保存  |
| run_analyses.py  | calculate_average_blockprop_time.pyとcalculate_fork_probability.pyとcalculate_performance.pyを一括で実行  |
| calculate_average_blockprop_time.py  | 平均ブロック伝搬時間Mを計算し、results_graphディレクトリへグラフの出力, 数値をAverage_timeディレクトリに保存 |
| calculate_fork_probability.py  | フォーク確率Pforkを計算し、results_graphディレクトリへグラフの出力, 数値をFork_probabilityディレクトリに保存  |
| calculate_performance.py  | パフォーマンスPを計算し、results_graphディレクトリへグラフの出力  |
| para.py  | パラメータの変更  |
| dust.py  | シミュレーションの過程で生成されたファイルを一括削除する  |


**サブ**
| プログラム名  | 役割 |
| ------------- | ------------- |
|  count.py  | ディレクトリ数や、ファイル数を数えるための関数を定義  |
| explain_text.py  | settings_note.txtに関係する関数の定義  |
| simple_cmd.py  | コマンド実行を簡略化する関数を定義  |
| for_plot.py | プロットに関する行をまとめた関数を定義  |

