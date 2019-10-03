# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 23:05:47 2019

@author: Borko
"""

# 1. Parse input from the console:
#   1) IP Address
#   2) Port range   - optional
#   3) IPv          - optional
#   4) TCP/UDP      - optional
import argparse
import ipaddress
import socket

parser = argparse.ArgumentParser(description="A simple Python Port Scanner \
                                 that checks if any are open.")

parser.add_argument("first_ip", type=str, help="Starting IP address of the \
                    scan.")
parser.add_argument("last_ip", type=str, help="Last IP address to scan.")
parser.add_argument("-p", "--port", type=int, help="Set the last port to scan.\
                     Default is 1024.", required=False, default=1024)
parser.add_argument("-v", "--version", type=int, help="Specify if you are \
                    testing IPv4 or IPv6 addresses. IPv4 is default.",
                    required=False, default=4)
parser.add_argument("-u", "--udp", help="Selects UDP as the underlying \
                    protocol for testing.")
parser.add_argument("-t", "--timeout", help="Set the timeout in seconds for \
                    each port scan. Default is 3.", default=3, type=int)

args = parser.parse_args()

# 2. Loop through the IP range and check for connections.
# 3. Print results

start_ip    = ipaddress.IPv4Address(args.first_ip)
end_ip      = ipaddress.IPv4Address(args.last_ip)

for current_ip in range(int(start_ip), int(end_ip)+1):
    print("\r\n" + "***"*15)
    print("Open ports on {}:".format(ipaddress.IPv4Address(current_ip)))
    none = True

    for port in range(1, args.port+1):
        sock        = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(args.timeout)
        connection  = sock.connect_ex((str(ipaddress.IPv4Address(current_ip)), port))

        if connection == 0:
            print("Port {} is OPEN!".format(port))
            none = False
        sock.close()

    if none:
        print("No open ports found.")

    print("---"*15)