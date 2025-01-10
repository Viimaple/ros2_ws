# 体重に基づいて2日に必要な水分摂取量を計算する簡単なプログラム

このプロジェクトは、体重に基づいて1日に必要な水分摂取量を計算する簡単なプログラムです。

## 概要

- このプロジェクトには、以下の2つのROS 2ノードがあります：

 1.Listener：受信したタイムゾーン情報をログに出力します。  
 2.Talker：日本標準時（JST）に基づくタイムゾーン情報を定期的に送信します。

## インストール方法

このプロジェクトをローカルにインストールするには、以下の手順を実行してください。
    
1. リポジトリをクローンします。
```sh
$ https://github.com/Viimaple/ros2_ws/edit/kadai2
$ cd ros2_ws
```  
2. 必要な権限を設定して実行可能にします：
```sh
$ chmod +x work
```

## 使い方

`work` は、ユーザーに体重を数字で入力させ、1日に必要な水分摂取量を計算します。　　

### プログラムの実行例
- 正しい入力例
```sh
$ echo 70 | ./work
$ 2.31
```
- 変な入力の例
```sh
$ echo a | ./work
# 結果：標準エラー出力にメッセージが表示され、エラーコード1を返します。
```
## ライセンス

このプロジェクトはBSD-3-Clauseライセンスのもとで公開されています。

## クレジット
このプログラムの一部————`water_test.bash`はRyuichi Ueda先生のコードを参考にしています。ご貢献に感謝します。

## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7〜3.10
  
## テスト環境
- Ubuntu 22.04.5 LTS
 
© 2024 Mori Yoshizumi
