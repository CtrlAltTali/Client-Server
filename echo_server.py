import socket
import sys
import thread
import threading

client_num = 0
def foofoo(connection, client_address):
    global client_num
    lock = threading.Lock()
    lock.acquire()
    try:
        client_num+=1
    finally:
        lock.release()
    print("number of clients: "+str(client_num))
    try:
        print >>sys.stderr, 'connection from', client_address
        print (str(connection.fileno()))
            # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                try:
                    connection.sendall(str(eval(data))+chr(10))
                except Exception as e:
                    connection.sendall(str(e)+chr(10))
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
    finally:
        # Clean up the connection
            connection.close()

        

def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('0.0.0.0', 10000)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()
        print (str(connection.fileno()))
       
        thread.start_new_thread(foofoo, (connection,client_address,))
        
            

if __name__=="__main__":
   main()
