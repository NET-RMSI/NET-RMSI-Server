#!/usr/bin/python3
import socket






def TCPSRVINIT():

   global tcpconstatus
   tcpconstatus = False

   HOSTNAME = socket.gethostname()
   PORT = 13062
   IPADDRESS = socket.gethostbyname(HOSTNAME)
   tcpsrv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   tcpsrv.bind((IPADDRESS, PORT))

   tcpsrv.listen(1)
   print(f"Waiting for a client to connect")
   tcpcli, address = tcpsrv.accept()
   with tcpcli:
      print(f"Connected by {address}")
      tcpconstatus = True
      