#!/bin/bash
# file: LEFT_5x.sh

# -1 at the end: publish for 3 seconds
# move forwards for 5mm
echo "moving stepper motor left"
#rostopic pub myStepper std_msgs/Int16 "data: 50" -1

rostopic pub myStepper std_msgs/Float32 "data: 50" -1
sleep 15



# -1 at the end: publish for 3 seconds
# move backwards for 5mm
#echo "moving stepper motor right"
#rostopic pub myStpper std_msgs/Int16 "data: -50" -1
#rostopic pub myStepper std_msgs/Float32 "data: -5" -1
#pid3=$!
#wait $pid3
#kill $pid3
#sleep 3
#kill $pid3

exit 0
