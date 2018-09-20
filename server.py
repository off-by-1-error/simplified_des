import socket
import thread

def Main():
    host = "127.0.0.1"
    port = 60000
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))

            if data[:5] == "send ":
                print "rcvd send request!"
                
                f = open("file.txt", "wb")
                conn.send("Begin sending!")
                bytes = conn.recv(1024)
                while len(bytes) != 0:
                    print "in the loop"
                    f.write(bytes)
                    bytes = conn.recv(1024)

                f.close()
             
            data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()
        
