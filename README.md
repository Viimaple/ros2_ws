# ROS2 タイムゾーン情報通信プログラム

このプロジェクトは、ROS2を使用して日本標準時（JST）のタイムゾーン情報を送受信する2つのプログラムを提供します。

## 概要

- このプロジェクトには、以下の2つのROS 2ノードがあります：

 1.Listener：受信したタイムゾーン情報をログに出力します。  
 2.Talker：日本標準時（JST）に基づくタイムゾーン情報を定期的に送信します。

## インストール方法

このプロジェクトをローカルにインストールするには、以下の手順を実行してください。
    
1. リポジトリをクローンします：
```sh
$ https://github.com/Viimaple/ros2_ws/edit/kadai2
$ cd ros2_ws
```  
2. 必要な依存パッケージをインストールします：
```sh
$ pip install pytz
$ sudo apt install python3-pip
$ pip3 install pytz
```

## 使い方
実行方法:  
```sh
$ cd ~/ros2_ws
$ colcon build
$ source install/setup.bash
$ ros2 run mypkg talker
$ ros2 run mypkg listener
```
### プログラムの実行例
- 正しい入力例
```sh
[INFO] [1736545086.599539943] [listener]: Received time zone info: JST: UTC+9
[INFO] [1736545087.571690731] [listener]: Received time zone info: JST: UTC+9
[INFO] [1736545088.571684817] [listener]: Received time zone info: JST: UTC+9
[INFO] [1736545089.571791643] [listener]: Received time zone info: JST: UTC+9
...
..
.
```

## ライセンス

このプロジェクトはBSD-3-Clauseライセンスのもとで公開されています。

## クレジット
このプログラムの一部は上田 隆一先生のコードを利用にしています。ご貢献に感謝します。

## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7〜3.10
- ROS2
  
## テスト環境
- Ubuntu 22.04.5 LTS
 
© 2024 Mori Yoshizumi
