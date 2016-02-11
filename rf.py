import socket
import sys
import select
import time

UDP_IP = "192.168.0.100"
UDP_PORT = 5005

bsize = 2048 # packet bit size

wait = 5 # wait 5 seconds

sock = socket.socket(socket.AF_INET, # internet
                        socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

rcvimg,(UDP_IP, UDP_PORT) = sock.recvfrom(bsize)

filercv = open(rcvimg.strip(),'wb')

print " "

packets = 0

start = time.time()

rcvimg,(UDP_IP, UDP_PORT) = sock.recvfrom(bsize)

try:
        while(rcvimg):
                packets = packets + 1
                filercv.write(rcvimg)
                sock.settimeout(wait)
                rcvimg,(UDP_IP, UDP_PORT) = sock.recvfrom(bsize)

except socket.timeout:
        filercv.close()
        sock.close()

end = time.time()

denom = end-start-wait

if denom == 0:
        freq = 0
else:
        freq = packets/denom

kbitrate = freq*bsize/1000

print "Frequency: %2.3f Hz" % freq
print "Bit Rate : %2.3f Kbps" % kbitrate

print " "
