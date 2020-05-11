SERVER

#!usr/bin/python

import socket
host = socket.gethostname()
port = 12345
s = socket.socket()		# TCP socket object
s.bind((host,port))
s.listen(5)

print "Waiting for client..."
conn,addr = s.accept()	        # Accept connection when client connects
print "Connected by ", addr

while True:
	data = conn.recv(1024)	    # Receive client data
	if not data: break	        # exit from loop if no data
	conn.sendall(data)	        # Send the received data back to client
conn.close()

# CLIENT

#!usr/bin/python

import socket
host = socket.gethostname()
port = 12345
s = socket.socket()		# TCP socket object

s.connect((host,port))

s.sendall('This will be sent to server')    # Send This message to server

data = s.recv(1024)	    # Now, receive the echoed
					    # data from server

print data				# Print received(echoed) data
s.close()				# close the connection


# ADD SERVER

#!usr/bin/python

import socket
host = socket.gethostname()
port = 12345
s = socket.socket()		    # TCP socket object
s.bind((host,port))

s.listen(5)

conn, addr = s.accept()
print "Connected by ", addr
while True:
	data=conn.recv(1024)
	# Split the received string using ','
	# as separator and store in list 'd'
	d = data.split(",")	    
	
	# add the content after converting to 'int'
	data_add = int(d[0]) +int(d[1]) 
	
	conn.sendall(str(data_add))	    # Send added data as string
					                # String conversion is MUST!
conn.close()


# ADD CLIENT

#!usr/bin/python

import socket

host = socket.gethostname()
port = 12345

a = str(raw_input('Enter first number: '))	# Enter the numbers
b = str(raw_input('Enter second number: '))	# to be added
c = a+','+b					# Generate a string from numbers

print "Sending string {0} to server" .format(c)

s = socket.socket()
s.connect((host,port))

s.sendall(c)				# Send string 'c' to server
data = s.recv(1024)			# receive server response
print int(data)				# convert received dat to 'int'

s.close()					#Close the Connection


