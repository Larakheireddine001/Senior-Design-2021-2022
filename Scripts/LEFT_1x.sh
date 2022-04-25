#!/bin/bash
# file: LEFT_1x.sh

rostopic pub myStepper std_msgs/Float32 "data: 10" -1
sleep 2

exit 0
