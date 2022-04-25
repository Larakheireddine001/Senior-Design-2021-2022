#!/usr/bin/python2
import subprocess
import os
import sys
sys.path.append("..")
sys.path.append("~/catkin_ws/src")
import time
import dca
import cmd

def recording_process():
    print("---------------------Start Recording---------------------")
    dca.step_3()
    time.sleep(2)
    os.system("gnome-terminal -e 'roslaunch ti_mmwave_rospkg aop1_2.launch'")
    time.sleep(4)
    print("---------------------Stop Recording----------------------")
    dca.step_5()
    time.sleep(4)
    os.system("pkill -f DCA1000EVM_CLI_Record")
    

if __name__ == "__main__":
    recording_process()
