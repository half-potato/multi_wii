#!/usr/bin/env python

from pyMultiwii import MultiWii
import time

import roslib; roslib.load_manifest("multi_wii")
import rospy
from multi_wii.msg import IMU
from sys import stdout


def talker():
    pub = rospy.Publisher("IMU", IMU, queue_size=10)
    rospy.init_node("IMU", anonymous=False)
    port = rospy.get_param("~port")
    board = MultiWii(port)
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        board.getData(MultiWii.RAW_IMU)
        msg = IMU()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "/world";
        msg.ax = board.rawIMU["ax"]
        msg.ay = board.rawIMU["ay"]
        msg.az = board.rawIMU["az"]
        msg.gx = board.rawIMU["gx"]
        msg.gy = board.rawIMU["gy"]
        msg.gz = board.rawIMU["gz"]
        msg.timestamp = float(board.attitude["timestamp"])
        pub.publish(msg)
        output = "ax = {:+.2f} \t ay = {:+.2f} \t az = {:+.2f} \t gx = {:+.2f} \t gy = {:+.2f} \t gz = {:+.2f} \t".format(msg.ax, msg.ay, msg.az, msg.gx, msg.gy, msg.gz)
        stdout.write("\r%s" % output)
        stdout.flush()
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

print("\n")
