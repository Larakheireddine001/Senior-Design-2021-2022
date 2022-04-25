#!/bin/bash
# file: RIGHT_5x.sh

# -1 at the end: publish for 3 seconds
# move forwards for 5mm
#echo "moving stepper motor left"
#rostopic pub myStepper std_msgs/Int16 "data: 50" -1

#rostopic pub myStepper std_msgs/Float32 "data: 5" -1
#pid2=$!
#wait $pid2
#kill $pid2
#pkill rostopic
#sleep 2
#kill $pid2

# -1 at the end: publish for 3 seconds
# move backwards for 5mm
echo "moving stepper motor right"
#rostopic pub myStpper std_msgs/Int16 "data: -50" -1
rostopic pub myStepper std_msgs/Float32 "data: -50" -1
sleep 15

exit 0
