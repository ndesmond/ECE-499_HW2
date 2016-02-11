import socket
import struct

UDP_IP = "192.168.0.100"
UDP_PORT = 5005

print " "

print "UDP target IP:", UDP_IP
print "UDP target prot:", UDP_PORT

sock = socket.socket(socket.AF_INET, # internet
			socket.SOCK_DGRAM) # UDP

# first set of values:

LW = 213
RW = 187

print "\nFirst set of commands:"
print "Left wheel:", LW
print "Right wheel:", RW

CMDMSG = struct.pack("ii",LW,RW)

sock.sendto(CMDMSG, (UDP_IP, UDP_PORT))

LW = 22
RW = 115

print "\nSecond set of commands:"
print "Left wheel:", LW
print "Right wheel:", RW

CMDMSG = struct.pack("ii",LW,RW)

sock.sendto(CMDMSG, (UDP_IP, UDP_PORT))

LW = 93
RW = 27

print "\nThird set of commands:"
print "Left wheel:", LW
print "Right wheel:", RW

CMDMSG = struct.pack("ii",LW,RW)

sock.sendto(CMDMSG, (UDP_IP, UDP_PORT))

print " "

