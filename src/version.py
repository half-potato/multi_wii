from pyMultiwii import MultiWii

board = MultiWii("/dev/ttyUSB0")
board.sendCMD(0, MultiWii.IDENT, [])
