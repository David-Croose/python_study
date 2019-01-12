#!/usr/bin/env python

#===========================================================
#             
#      This is a TCP client, it connects to a TCP server 
#      then sends many data to the server, then quit 
#             
#===========================================================

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

s.connect((host, port))

# s.send("this is string: hello world")
s.send("\x11\x22\x33\x44\xaa\xbb\xcc")

s.close()

