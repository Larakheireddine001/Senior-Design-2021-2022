#!/bin/bash
# file: RIGHT_1x.sh

rostopic pub myStepper std_msgs/Float32 "data: -10" -1
sleep 3

exit 0
