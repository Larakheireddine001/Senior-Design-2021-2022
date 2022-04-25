#!/usr/bin/python2
import subprocess
import os
import time
import sys
sys.path.append("..")
import dca

def preset():
    print("-----------------------Pre-Setting-----------------------")
    dca.step_1()
    dca.step_2()
    # dca.launch_sensor1()
    os.system("gnome-terminal -e 'bash -c \"roslaunch ti_mmwave_rospkg aop.launch; exec bash\"'")
    time.sleep(5)
    print("------------------Pre-Setting Completed------------------")


if __name__ == "__main__":
    preset()
