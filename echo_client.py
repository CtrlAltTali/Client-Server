import socket
import sys
import time
import details
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip = details.host()
server_address = (ip, 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
sock.setblocking(0)
try:
    
    # Send data
    message = raw_input("user@"+ip+"-> ")
    while(message!="exit"):
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message)

        # Look for the response
        data_received = ""
        data = " "
        while ord(data)!=10:
            try:  
                data = sock.recv(1)
            except:
                time.sleep(1)
            data_received += data
        print (data_received[1:])
        message = raw_input("user@"+ip+"-> ")
    
    print >>sys.stderr, 'closing socket'
    sock.close()

except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
    
