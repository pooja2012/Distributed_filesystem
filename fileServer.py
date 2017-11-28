import socket
import threading
import os
from threading import Thread
## Retrieving file
def RetrFile(name,sock):
    filename=sock.recv(1024)
    if os.path.isfile(filename):
        sock.send("EXISTS"+str(os.path.getsize(b'filename')))
        userResponse=sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(filename,'rb') as f:
                bytesToSend= f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend=f.read(1024)
                    sock.send(bytesToSend)
    else:
          sock.send("ERR")
          sock.close()
def Main():
    host='127.0.0.1'
    port=5000
    s=socket.socket()
    s.bind((host,port))
    s.listen(5)
    print("Server started")
    while True:
        c,addr = s.accept()
        print("Client connected the ip:<"+str(addr) + ">")
        print("------------------------")
        t=threading.Thread(target=RetrFile,args=("retrThread",c))
        t.start()
        print("Got the thread")

    s.close()
if __name__ == '__main__':
    Main()
