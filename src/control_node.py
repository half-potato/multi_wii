#!/usr/bin/env python

from pyMultiwii import MultiWii
import time
import rospy
from std_msgs.msg import String
from multi_wii.msg import IMU

board = MultiWii("/dev/ttyUSB0")

def talker():
    pub = rospy.Publisher("IMU", String, queue_size=50)
    rospy.init_node("IMU", anonymous=False)
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        data = [0,1,2,3]
        rospy.loginfo(data)#board.getData(MultiWii.ATTITUDE))
        pub.publish(data)
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

