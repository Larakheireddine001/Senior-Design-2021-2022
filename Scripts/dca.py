#!/user/bin/python2
import roslaunch
import rospy
import sys
import os
sys.path.append("..")

def new_terminal():
    os.system("gnome-terminal -e 'bash -c \"cd ~/DCA1000/SourceCode/Release; exec bash\"'")
def step_1():
    os.system("./DCA1000EVM_CLI_Control fpga ./dcaconf.json")
def step_2():
    os.system("./DCA1000EVM_CLI_Control record ./dcaconf.json")
def step_3():
    os.system("./DCA1000EVM_CLI_Control start_record ./dcaconf.json")
def launch_sensor1():
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    global tracking_launch
    tracking_launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/team7/catkin_ws/mmwave_ti_ros/ros_driver/src/ti_mmwave_rospkg/launch/aop.launch"])
    tracking_launch.start()
    print("-----------------------------Done!-----------------------------")
def launch_sensor2():
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    global tracking_launch
    tracking_launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/team7/catkin_ws/mmwave_ti_ros/ros_driver/src/ti_mmwave_rospkg/launch/aop1_2.launch"])
    tracking_launch.start()
def step_5():
    os.system("./DCA1000EVM_CLI_Control stop_record ./dcaconf.json")
def choose_command():
    print("Please choose from below by type in the number and press ENTER:")
    print("[1]. FPGA")
    print("[2]. Set up Recording")
    print("[3]. Start Recording")
    print("[4]. Launch Sensor")
    print("[5]. Stop Recording")
    print("[0]. Shutdown")

    global choice_input
    choice_input = int(input('Make your choice: '))
    arr = [0, 1, 2, 3, 4, 5, 9]
    while choice_input not in arr:
        print("Wrong input! Please enter valid command such as '1' and press ENTER.")
        choice_input = int(input('Make your choice: '))


if __name__ == "__main__":
    os.system("chmod +x DCA1000EVM_CLI_Control")
    os.system("chmod +x DCA1000EVM_CLI_Record")
    os.system("export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$pwd")
    while True:
	print("---------------------Radar Data Sensor Recording.---------------------")
        choose_command()
	if choice_input == 1:
            print("Executing First Step")
	    step_1()
	elif choice_input == 2:
	    print("Executing Second Step")
	    step_2()
	elif choice_input == 3:
	    print("Executing Third Step")
	    step_3()
	elif choice_input == 4:
	    print("Executing Fourth Step. Launching Sensor")
	    launch_sensor1()
	    x = input("lanching sensor")
	    if x == 9:
	    	launch_sensor2()
	elif choice_input == 5:
	    print("Executing Last Step")
	    step_5()
	elif choice_input == 0:
	    break
	    
	
