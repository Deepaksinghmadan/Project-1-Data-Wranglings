#Socket Object

import socket
s = socket.socket()
s.bind(('192.168.225.65','5000'))
s.listen()
c_addr, other =s.accept()
while True:
	(TCP Command)send()/recv() CHOICE (UDP Command)sendto()/receivefrom()
TCP:EG Email # connection oriented
UDP:EG Intrusion, VoiP
close the server socket


#Client Object
#
#
#
#
s.connect((host,port))

while True:
send()/recv()
close the client socket