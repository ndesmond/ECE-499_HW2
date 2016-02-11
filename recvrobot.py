import socket
import struct
import time

UDP_IP = "192.168.0.100"
UDP_PORT = 5005

bsize = 1024

sock = socket.socket(socket.AF_INET, # internet
                        socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

print " "

while True:

        start = time.time()

        data, addr = sock.recvfrom(bsize) # buffer size is 1024 bytes

        end = time.time()

        denom = end-start

        if denom == 0:
                freq = 0
        else:
                freq = 1/denom

        kbitrate = freq*bsize/1000

        LW,RW = struct.unpack("ii",data)

        LW2x = 2*LW
        RW2x = 2*RW

        # print "received message:", data

        # values received:
        print "Left wheel : ", LW
        print "Right wheel: ", RW

        # twice the values:
        print "Twice left wheel : ", LW2x
        print "Twice right wheel: ", RW2x

        print "Bit Rate: %2.3f Kbps" % kbitrate

        print " "
