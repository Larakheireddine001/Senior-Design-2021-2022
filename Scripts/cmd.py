#!/usr/bin/python2
import roslaunch
import rospy
import subprocess
import time
import os
import sys
sys.path.append("..")
import cam

def launch_cam():
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    global tracking_launch
    tracking_launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/team7/catkin_ws/src/zed-ros-wrapper/zed_wrapper/launch/zedm.launch"])
    tracking_launch.start()
    print("-----------------------------Done!-----------------------------")

def launch_sensor():
    # os.system("/home/team7/catkin_ws/src/source_s.sh")
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    global tracking_launch
    tracking_launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/team7/catkin_ws/mmwave_ti_ros/ros_driver/src/ti_mmwave_rospkg/launch/aop.launch"])
    tracking_launch.start()
    print("-----------------------------Done!-----------------------------")

def launch_sensor1():
    # os.system("/home/team7/catkin_ws/src/source_s.sh")
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    global tracking_launch
    tracking_launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/team7/catkin_ws/mmwave_ti_ros/ros_driver/src/ti_mmwave_rospkg/launch/aop.launch"])
    tracking_launch.start()
    print("-----------------------------Done!-----------------------------")

def launch_sensor2():
    # os.system("/home/team7/catkin_ws/src/source_s.sh")
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    global tracking_launch
    tracking_launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/team7/catkin_ws/mmwave_ti_ros/ros_driver/src/ti_mmwave_rospkg/launch/aop1_2.launch"])
    tracking_launch.start()

def launch_motors():
    #os.system("/home/team7/catkin_ws/src/source_m.sh")
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    global tracking_launch
    tracking_launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/team7/catkin_ws/motors.launch"])
    tracking_launch.start()
    print("-----------------------------Done!-----------------------------")

def motor_l5x():
    subprocess.call(['sh','/home/team7/catkin_ws/src/LEFT_5x.sh'])
def motor_l1x():
    subprocess.call(['sh','/home/team7/catkin_ws/src/LEFT_1x.sh'])
def motor_r5x():
    subprocess.call(['sh','/home/team7/catkin_ws/src/RIGHT_5x.sh'])
def motor_r1x():
    subprocess.call(['sh','/home/team7/catkin_ws/src/RIGHT_1x.sh'])

def shutdown():
    tracking_launch.shutdown()
    print("-----------Done! Now you can choose the next service!----------")

def choose_cmd():
    print("Please choose from below by typing in the number and press ENTER:")
    print("[1]. Radar Sensor")
    print("[2]. Start ZEDmini")
    print("[3]. Data Analyzing for Camera")
    print("[4]. Data Capture Process for Sensor")
    print("[5]. Start Stepper Motors")
    print("[6]. Start Servo Motors")
    print("[9]. Something Magical")
    print("[0]. Shut Down")

    global choice
    choice = int(input('Make your choice: '))
    arr = [0, 1, 2, 3, 4, 5, 6, 9]
    while choice not in arr:
        print("Wrong input! Please enter valid command such as '1' and press ENTER.")
        choice = int(input('Make your choice: '))

if __name__ == "__main__":
    # os.system("/home/team7/catkin_ws/src/source_m.sh")
    print("---------------------Hello~This is Team7's auto robot! ;)---------------------")
    while True:
        choose_cmd()
	print("----------Good Choice! Please wait for a second. I am reaching it...----------")
        if choice == 1:
            print("---------------------Starting Radar Sensor---------------------")
            launch_sensor1()
	    time.sleep(5)
	    os.system("gnome-terminal -e 'bash -c \"roslaunch ti_mmwave_rospkg aop1_2.launch; exec bash\"'")
            print("Please select from below:")
            print("[q]. Quit")
            cam_in_radar = raw_input()
            if cam_in_radar == 'q':
		print("---Give me a moment. I am getting you back to the main menu.---")
                shutdown()
            else:
                print("Wrong input! Press 'q' then press ENTER to quit RVIZ.")
                cam_in_radar = raw_input()
        elif choice == 2:
	    print("------------------------Starting Camera------------------------")
            launch_cam()
            print("Please select from below:")
            print("[1]. Start Recording")
            print("[q]. Quit")
            cam_in = raw_input()
            if cam_in == 'q':
		print("---Give me a moment. I am getting you back to the main menu.---")
                shutdown()
	    elif cam_in == '1':
                cam.start_cam_recording()
                print("Press 2 to stop recording")
                cam_rec = raw_input()
                if cam_rec == '2':
                    cam.stop_cam_recording()
                    shutdown()
                else:
                    print("Wrong input! Press '2' to stop recording.")
		    cam_rec = raw_input()
            else:
                print("Wrong input! Press 'q' to quit or press 1 to start recording.")
                quit_rviz = raw_input()
        elif choice == 3:
            print("---------------------Analyzing Camera Data---------------------")
            cam.analysis()
	    print("---Give me a moment. I am getting you back to the main menu.---")
        elif choice == 4:
                print("Because the DCA card is not completed this command is only going to open terminal and jump to dirctory ~/DCA1000/ScourceCode/Release")
		subprocess.call(['sh','/home/team7/catkin_ws/src/DCA.sh'])
		print("---Give me a moment. I am getting you to a new terminal.---")  
	elif choice == 5:
            print("--------------------Starting Stepper Motors--------------------")
            launch_motors()
	    while True:
	    	print("Please select from below:")
	    	print("[1]. Move the Stepper Motor Right 5x")
	    	print("[2]. Move the Stepper Motor Left 5x")
                print("[3]. Move the Stepper Motor Right 1x")
	    	print("[4]. Move the Stepper Motor Left 1x")
	    	print("[q]. Quit")
	    	stepm_in = raw_input()
	    	if stepm_in == 'q':
		    print("---Give me a moment. I am getting you back to the main menu.---")
	            shutdown()
		    break
	   	elif stepm_in == '1':
            	    motor_r5x()
	    	elif stepm_in == '2':
		    motor_l5x()
		elif stepm_in == '3':
            	    motor_r1x()
	    	elif stepm_in == '4':
		    motor_l1x()
	    	else:
		    print("Wrong input! Press 'q' to quit or select from the menu options.")
		    quit_rviz = raw_input()
	elif choice == 6:
            print("---------------------Starting Servo Motors---------------------")
            launch_motors()
	    while True:
	        print("Please select from below:")
	        print("[1]. Down View")
	        print("[2]. Front View")
	        print("[q]. Quit")
	        servom_in = raw_input()
                if servom_in == 'q':
		    print("---Give me a moment. I am getting you back to the main menu.---")
		    shutdown()
		    break
	        elif servom_in == '1':
		    print("90 Degree")
		    #subprocess.call(['sh','/home/team7/catkin_ws/src/servom90.sh'])
	        elif servom_in == '2':
		    print("180 Degree")
	    	    #subprocess.call(['sh','/home/team7/catkin_ws/src/servom180.sh'])
	        else:
		    print("Wrong input! Press 'q' to quit or select from the menu options")	
		    quit_rviz = raw_input()
	elif choice == 9:
	    os.system("python2 AOP_rcd_proc.py")
        elif choice == 0:
	    print("--------------Oh you gonna leave me here alone :( Fine. Bye bye!--------------")
            break

