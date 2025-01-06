#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"  

cd ~/ros2_ws
colcon build
source ~/.bashrc

timeout 10 ros2 launch mypkg talk_listen.launch.py | tee - /tmp/mypkg.log
cat /tmp/mypkg.log | grep 'Listen: 10'

