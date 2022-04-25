import os
import roslaunch
import rospy

def start_cam_recording():
    os.system("rosservice call /zedm/zed_node/start_svo_recording /home/team7/camera.svo")

def stop_cam_recording():
    os.system("rosservice call /zedm/zed_n   ode/stop_svo_recording")

def analysis():
    os.system("python3 /home/team7/ZEDMINI/svo_export_v2_2.py '/home/team7/camera.svo' '/home/team7/camera_data' 3")
