# 使い方

## 1-a. プログラムの実行方法
```
$python3 All_simulation.py
```

結果は、my_simblock/results_graph/file(n)(n=1,2,…)ディレクトリ配下に格納されます。

nが大きいほど最新の実行結果です。

file(n)内には、自動的に実行時のパラメータ設定を記載したファイル（settings_note.txt）が保存されるようになっています。

> 項目[実行した時刻, interval, ノードの数, 変えたパラメータとその数値リスト]


2回目以降の実行は
```
$python3 dust.py
```
でシミュレーション過程で出力されたファイル群を消去してからお願いします。

**sesult_graphに出力されたグラフはすべて残るので、安心して消してください。**

## 1-b. 個別の実行方法
四段階に分かれています。

1から順に実行してください。2-1,2-2のみ順不同です。

1. シミュレーションの実行
```
$python3 repeat_simulation.py
```
2-1. フォーク確率の計算
```
$ python3 calculate_fork_probability.py ./blocklists/*
```
2-2. 平均ブロック伝搬時間の計算
```
$ python3 calculate_average_block_propagation_time.py ./stdouts/*
```
3. パフォーマンスの計算とグラフの出力
```
$ python3 analyse_results.py
```

## 2. パラメータの変更方法
### ◆para.pyから変えられるもの
**ブロック伝搬時間、ノード数、変更しているパラメータの数値範囲（リスト）（と変更しているパラメータの名前）**


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

## 3. 結果の見方
result_graphディレクトリに4つの結果（グラフ）が保存されます。

> result_graph内のfile(n)のnは、
> 1. シミュレーション実行時にresult_graph内にすでに存在するディレクトリ数を数える
> 2. その数に+1した数字を次の結果ファイルのnとする
> 
> といった形で決められています。
>
> ⇒　数字が新しいほど最新の実行結果です。
>
> 本当に最新の実行結果かどうか不安な場合は、settings_note.txtのタイムスタンプ欄から時刻の確認をお願いします。

### ◆ディレクトリの中身
+ M_time-plot.png : 横軸ブロックサイズ、縦軸平均ブロック伝搬時間M

+ avstd-plot.png : 横軸ブロックサイズ、縦軸平均ブロック伝搬時間の標準偏差

+ Pfork-plot.png : 横軸ブロックサイズ、縦軸フォーク確率Pfork

+ result.png : 横軸ブロックサイズ、縦軸パフォーマンスP

+ settings_note.txt : 実行時のパラメータについてのメモ（1.実行方法を参照）

## 4. 各プログラムの関係性
**メイン**

| プログラム名  | 役割 |
| ------------- | ------------- |
|  All_simulation.py  | repeat_simulation.pyとanalyse_results.pyをまとめて実行  |
| repeat_simulation.py  | シミュレーションの実行と、その結果を指定した場所に保存  |
| analyse_results.py  | calculate_average_block_propagation_time.pyとcalculate_fork_probability.pyの実行と、グラフの生成  |
| calculate_average_block_propagation_time.py  | 平均ブロック伝搬時間Mを計算し、Average_timeディレクトリに保存  |
| calculate_fork_probability.py  | フォーク確率Pforkを計算し、Fork_probabilityディレクトリに保存  |
| para.py  | パラメータの変更  |
| dust.py  | シミュレーションの過程で生成されたファイルを一括削除する  |


**サブ**
| プログラム名  | 役割 |
| ------------- | ------------- |
|  count.py  | ディレクトリの数や、ファイルの数を数えるための関数まとめ  |
| explain_text.py  | settings_note.txtに関するすべて  |
| for_plot.py | プロット関係のコードを一括管理  |
