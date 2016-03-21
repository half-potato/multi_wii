#!/usr/bin/env python

from pyMultiwii import MultiWii
import time

import roslib; roslib.load_manifest("multi_wii")
import rospy
from multi_wii.msg import Attitude
from sys import stdout

def talker():
    pub = rospy.Publisher("Attitude", Attitude, queue_size=10)
    rospy.init_node("Attitude", anonymous=False)
    port = rospy.get_param("~port")
    board = MultiWii(port)
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        board.getData(MultiWii.ATTITUDE)
        msg = Attitude()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "/world";
        msg.anglex = board.attitude["angx"]
        msg.angley = board.attitude["angy"]
        msg.heading = board.attitude["heading"]
        msg.elapsed = board.attitude["elapsed"]
        output = "angle_x = {:+.2f} \t angle_y = {:+.2f} \t heading = {:+.2f} \t elapsed = {:+.2f} \t".format(msg.anglex, msg.angley, msg.heading, msg.elapsed)
        stdout.write("\r%s" % output)
        stdout.flush()
        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

print("\n")
