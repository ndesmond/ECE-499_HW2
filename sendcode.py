UDP target IP: 192.168.0.100
UDP target prot: 5005
student@ubuntu:~/neil/a2$ nano sf.py
student@ubuntu:~/neil/a2$ cat sf.py
import socket
import sys
import time

UDP_IP = "192.168.0.100"
UDP_PORT = 5005

bsize = 2048

invfreq = 0.2 # freq = 5 Hz

FileName = "robot1.bmp"

print " "

print "UDP target IP:", UDP_IP
print "UDP target prot:", UDP_PORT

file1 = open(FileName,"rb")

sendimg  = file1.read(bsize)

sock = socket.socket(socket.AF_INET, # internet
			socket.SOCK_DGRAM) # UDP

time.sleep(invfreq)

sock.sendto(FileName, (UDP_IP, UDP_PORT))
time.sleep(invfreq)

sock.sendto(sendimg, (UDP_IP, UDP_PORT))
time.sleep(invfreq)

while (sendimg):
	if (sock.sendto(sendimg,(UDP_IP, UDP_PORT))):
		sendimg = file1.read(bsize)
	time.sleep(invfreq)

sock.close()
file1.close()
