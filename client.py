#!/usr/bin/env python

#===========================================================
#             
#      This is a TCP client, it connects to a TCP server 
#      then waits severals bytes received, then quit 
#             
#===========================================================

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

s.connect((host, port))

msg = s.recv(10)

s.close()

print (msg.decode('utf-8'))

