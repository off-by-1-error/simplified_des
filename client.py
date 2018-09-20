import socket
import sys


def Main():
        host = '127.0.0.1'
        port = 60000
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = raw_input(" -> ")
         
        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                 

                if message[:5] == "send ":
                    print "making send request!"
                    print "filename: ", message[5:]
                 
                message = raw_input(" -> ")

        mySocket.close()
 
if __name__ == '__main__':
    Main()
