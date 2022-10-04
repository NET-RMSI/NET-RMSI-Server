#!/usr/bin/python3
import socket
import threading
from _global import *
from LoggerModule import *
from DataProcessing import *

global tcpsrv, tcpcli, address

def TCPSRVMAIN():

   LOGEVENTS_DEBUG("Starting TCPServer")
   
   tcpsrv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      tcpsrv.bind((IPADDRESS, PORT))
      LOGEVENTS_DEBUG("Bound to socket")
   except Exception as ex:
      LOGEVENTS_ERROR(f"{ex}")
      LOGEVENTS_CRITICAL(f"Terminating NET-RMSI_Srv_Py")
      quit(code=1)

   tcpsrv.listen(4)
   LOGEVENTS_DEBUG(f"TCPServer listening on {PORT}")
   
   print("Waiting for a client to connect")

   LOGEVENTS_DEBUG('Waiting for client to connect')
   
   while True:
      SRVACCEPTCON(tcpsrv)

def SRVACCEPTCON(tcpsrv):
   tcpcli, address = tcpsrv.accept()
   print(f"Connected to {address}")
   LOGEVENTS_DEBUG(f"Connected to {address}")
   threading.Thread(target=DATAPROCESSING(tcpcli)).start()
      
    