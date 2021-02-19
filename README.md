# PortScanner

This is a Linux command line port scanner built using python.

To start the program, run the following command:

python3 portscanner.py

If at any time you want to exit the program, use Ctrl + C.

You are able to scan a range of IP addresses and a range of ports. Ex: 192.168.149.1-192.168.149.10 and ports 22-25.

Input the IP addresses to be scanned in the following format: XXX.XXX.XXX.XXX. Ex: 192.168.149.1

Input the port numbers as the number with no periods or extra characters. Ex: 22

The output will be printed to the commandline as well as to a text file called results.txt located in the same directory the script is located in. 

The results list will list each IP address and port and whether or not the port is open on that host. It also ends by telling how long the scan took. 



