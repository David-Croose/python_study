#!/usr/bin/env python

#===========================================================
#
#      This is a TCP client, it connects to a TCP server
#      then sends many data(int format) to the server, then
#      quit
#
#===========================================================

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

s.connect((host, port))

buf = [1, 2, 3]
s.send(bytes(buf))

s.close()
