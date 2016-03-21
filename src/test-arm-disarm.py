#!/usr/bin/env python

"""test-send.py: Test script to send RC commands to a MultiWii Board."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2014 Aldux.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

from pyMultiwii import MultiWii
from sys import stdout
import time

if __name__ == "__main__":

    #board = MultiWii("/dev/tty.usbserial-AM016WP4")
    board = MultiWii("/dev/ttyUSB0")
    try:
        board.holdStick([1500]*2+[1000, 2000], 0.5)
        print "Board is armed now!"
        print "In 4 seconds it will disarm..."
        board.holdStick([1500]*2+[2000, 2000]+[1500]*4, 3.0) board.holdStick([1500]*2+[1000, 1000], 0.5)
        print "Disarmed."

    except Exception,error:
        print "Error on Main: "+str(error)
