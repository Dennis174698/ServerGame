"""
This is a simple example of a client program written in Python.
Again, this is a very basic example to complement the 'basic_server.c' example.


When testing, start by initiating a connection with the server by sending the "init" message outlined in 
the specification document. Then, wait for the server to send you a message saying the game has begun. 

Once this message has been read, plan out a couple of turns on paper and hard-code these messages to
and from the server (i.e. play a few rounds of the 'dice game' where you know what the right and wrong 
dice rolls are). You will be able to edit this trivially later on; it is often easier to debug the code
if you know exactly what your expected values are. 

From this, you should be able to bootstrap message-parsing to and from the server whilst making it easy to debug.
Then, start to add functions in the server code that actually 'run' the game in the background. 
"""
import random
import socket
from time import sleep
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 4444)
print ('connecting to %s port %s' % server_address)
sock.connect(server_address)
def act1():
    sock.sendall('%d,MOV,EVEN'.encode() %id)
def act2():
    sock.sendall('%d,MOV,DOUB'.encode()%id)

def act3():
    sock.sendall('%d,MOV,ODD'.encode()%id)
def act4():
    sock.sendall('%d,MOV,CON,%d'.encode() %(id, random.randrange(1,6)))

acts = [act1,act2,act3,act4]
count=0
id = 111
#message = 'INIT'.encode()
message = 'INIT'.encode()
print ('sending "%s"' % message)
sock.sendall(message)
try:
    while True:
    
        exit = False
        # Send data
        
 
        	

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(1024)
            amount_received += len(data)
            mess = data.decode()
            
      
		
            if "START" in mess:
                print("The games have begun")
                
                print( 'received "%s"' % mess)
                
                from random import choice
                choice(acts)()
            elif "PASS" in mess:
                print("Continue")
                
                from random import choice
                choice(acts)()
            elif "FAIL" in mess:
                print("fail but continue")
                
                from random import choice
                choice(acts)()
            elif "VICT" in mess:
                print("you win!!")
                exit = True
                break
            elif "ELIM" in mess:
                print("We lost, closing connection")
                exit = True
                break
            elif "CANCEL" in mess:
                print("Game cancle")
                exit = True
                break
            elif "REJECT" in mess:
                print("You are late")
                exit = True
                break
            else:
                print ( 'received "%s"' % mess)
        if exit:
            break
finally:    
    print ('closing socket')
    sock.close()
