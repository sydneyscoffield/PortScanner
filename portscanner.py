#!/usr/bin/env python
import socket
import subprocess
import sys
import ipaddress
from datetime import datetime
from scapy.all import *
from webb import webb
from fpdf import FPDF

# Ask for host and port ranges to scan
hostBeginning = input("Please enter the beginning of the range of remote hosts to scan: ")
hostEnd       = input("Please enter the end of the range of remote hosts to scan: ")
#remoteServerIP  = socket.gethostbyname(remoteServer)
portInput      = input("Please enter the beginning port to scan: ")
portEnd        = input("Please enter the last port to scan: ")


portNumber = int(portInput)
portEnd = int(portEnd)
hostBeginning = ipaddress.IPv4Address(hostBeginning)
hostEnd = ipaddress.IPv4Address(hostEnd)

outF = open("results.txt", "w")

# Print information about the hosts and ports being scanned
print ("-" * 100)
print ("Now scanning ports", portNumber, "through", portEnd, "on remote hosts:", hostBeginning, "through", hostEnd)
print ("-" * 100)


outF.write("-" * 75)
outF.write("\n")
information = "Results of the scan of ports " + str(portNumber) + " through " + str(portEnd) + " on remote hosts: "+ str(hostBeginning) + " through " + str(hostEnd)
outF.write(information)
outF.write("-" * 75)
outF.write("\n")

# Check what time the scan started
t1 = datetime.now()

portEnd += 1
hostEnd = ipaddress.IPv4Address(hostEnd)+1

try:
    for remoteServerIP in range(int(hostBeginning), int(hostEnd)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for portNumber in range(int(portInput), int(portEnd)):
            result = sock.connect_ex((str(remoteServerIP), portNumber))
            if result == 0:
                print ("Port {}:         Open       ".format(portNumber), "on host",ipaddress.IPv4Address(remoteServerIP))

                openPort = "Port {}:        Open    ".format(portNumber)
                ipAddress = str(ipaddress.IPv4Address(remoteServerIP))
                data = openPort + " on host " + ipAddress
                outF.write(data)
                outF.write("\n")

               # sock.close()

            else:
                print ("The specified port", portNumber, "is not open on host", ipaddress.IPv4Address(remoteServerIP))
                outF.write("The specified port " + str(portNumber) + " is not open on host " + str(ipaddress.IPv4Address(remoteServerIP)))
                outF.write("\n")

    sock.close()


except KeyboardInterrupt:
    print ("You pressed Ctrl+C. Now exiting the program.")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("The server could not be connected to at this time. Please try again later.")
    
    # Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print ('Scanning Completed in: ', total)

outF.write("\n")
outF.write("Scanning Completed in: " + str(total))
outF.close()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)
f = open("results.txt", "r")
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
pdf.output("results.pdf")

