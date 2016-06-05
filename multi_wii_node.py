#!/usr/bin/env python

from pyMultiwii import MultiWii
from __future__ import print_function
import time
import rospy
from std_msgs.msg import String

board = MultiWii("tty1/usb")

def handle_controls(req):
    print("I've got it")

def server():
    rospy.init_node("control_server")
    s = rospy.Service("controls", 
'''
try:
	board.arm()
	print("Board is armed now!")
	time.sleep(3)
	board.disarm()
except Exception, error:
	print("Error: " + str(error))
'''

print(rospy.get_param("usb"))
