# communicaton module
# to use this make sure your requested end is always open
import socket
def send(command,host,port):
    host=host
    port=port
    # initializing socket object in this case s
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # connecting to the other end of the socket the port no. should be 8000 typically for tcp but some use 5560
    s.connect((host,port))
    command=command
    # this is a message but in this caseI setting up a command "GET" to retrieve the information I require which is stored on the raspberry pi.
    # we encode the message to make it suitable for transmission
    s.send(str.encode(command))
    reply =s.recv(1024)
    print(reply.decode('utf-8'))
    return (reply.decode('utf-8'))