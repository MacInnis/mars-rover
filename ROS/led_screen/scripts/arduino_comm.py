#!/usr/bin/env python
import time
import rospy
from osr_msgs.msg import Status
from std_msgs.msg import Int64MultiArray
from screen import LedScreen

screen = LedScreen()

face_mode = 0

def callback(data):
        global face_mode
        print(face_mode)
	#rospy.loginfo(data)
	#send usb-> ttl serial commands
	screen.build_msg(1,data.battery,data.error_status,data.temp,data.current,face_mode)
	screen.check_for_afffirm()

def cmd_callback(data):
        global face_mode
        if len(data.data) > 1:
                face_mode = data.data[0] % 3

def shutdown():
	screen.transistion_to_idle()
	return 0

if __name__ == "__main__":
	rospy.init_node("led_screen")
	rospy.loginfo("Starting the led_screen node")
	rospy.on_shutdown(shutdown)
	sub = rospy.Subscriber("/status", Status, callback)
        cmd = rospy.Subscriber("/led_cmds", Int64MultiArray, cmd_callback)
	rospy.spin()
