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

parser = argparse.ArgumentParser(description="A simple Python Port Scanner \
                                 that checks if any are open.")

parser.add_argument("first_IP", type=str, help="Starting IP address of the \
                    scan.")
parser.add_argument("last_IP", type=str, help="Last IP address to scan.")
parser.add_argument("-p", "--port", type=int, help="Set the last port to scan.\
                     Default is 1024.", required=False)
parser.add_argument("-v", "--version", type=int, help="Specify if you are \
                    testing IPv4 or IPv6 addresses. IPv4 is default.",
                    required=False)
parser.add_argument("-u", "--udp", help="Selects UDP as the underlying \
                    protocol for testing.")

args = parser.parse_args()

# 2. Loop through the IP range and check for connections.


# 3. Print results.