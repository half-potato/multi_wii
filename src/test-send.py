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
import random
from sys import stdout

if __name__ == "__main__":

    board = MultiWii("/dev/ttyUSB1")
    #board = MultiWii("/dev/tty.usbserial-A801WZA1")
    try:
        board.arm()
        while True:
        	#example of 8 RC channels to be send
            #data = [random.randrange(100, 1600) for i in range(8)]
            data = [1100] * 4
            
            # Old function 
            #board.sendCMD(16,MultiWii.SET_RAW_RC,data)

            #New function that will receive attitude after setting the rc commands
            board.sendCMDreceiveATT(16,MultiWii.SET_RAW_RC,data)
            board.getData(MultiWii.ATTITUDE)
            message = "angx = {:+.2f} \t angy = {:+.2f} \t heading = {:+.2f} \t elapsed = {:+.4f} \t".format(float(board.attitude['angx']),float(board.attitude['angy']),float(board.attitude['heading']),float(board.attitude['elapsed']))
            stdout.write("\r%s" % message )
            stdout.flush()
        board.disarm()
    except Exception,error:
        print "Error on Main: "+str(error)
        board.disarm()
