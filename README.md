Pythonで書かれた最寄りの避難場所(直線距離)を教えてくれるスクリプトです 勝手に使ってください  
## 使い方
```
   python Finder.py
```
すると座標を聞かれるので、
```
N(緯度)
E(経度)
```
の形で入力します。
その後、災害タイプを聞かれるので入力してEnterを押すだけです。

## 実装
見ての通り言語はPython、避難場所のデータは[国土地理院のデータベース](http://maps.gsi.go.jp/development/ichiran.html#skhb)から取って、  
座標で直線距離を計算して最小の場所を返してるだけのごく単純なものです。
緯度経度とタイル(xy方式)の変換には、[こちらの記事](https://qiita.com/kobakou/items/4a5840542e74860a6b1b)を参考にさせていただきました。