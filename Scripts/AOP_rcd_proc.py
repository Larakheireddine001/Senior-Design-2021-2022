#!/usr/bin/python2
import sys
import os
sys.path.append("..")
import cmd
import time
import subprocess

def preset():
    subprocess.call(['sh','/home/team7/catkin_ws/src/DCA_Preset.sh'])

def recording_process():
    subprocess.call(['sh','/home/team7/catkin_ws/src/DCA_Proc.sh'])

if __name__ == "__main__":
    preset()
    cmd.launch_motors()
    cmd.motor_l5x()
    time.sleep(10)
    recording_process()
    with open ("/home/team7/DCA1000/SourceCode/Release/num.txt", "w") as f:
	    f.write(str(0))
	    f.close()
    subprocess.call(['sh', '/home/team7/catkin_ws/src/copy_data_file.sh'])
    for i in range(10):
	cmd.motor_r1x()
	recording_process()
	with open ("/home/team7/DCA1000/SourceCode/Release/num.txt", "w") as f:
	    f.write(str(i+1))
	    f.close()
	subprocess.call(['sh', '/home/team7/catkin_ws/src/copy_data_file.sh'])
    cmd.motor_l5x()
    print("--------------Recording Process Completed----------------")

