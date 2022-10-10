#!/bin/python3
# Syntax: python3 port_scanner.py <IP Addr>
# It will scan the ports and prints the open ports in the specific machine

import socket
import sys

def pretty_banner():
    print("=" * 50)
    print("||" + (" " * 46) + "||")
    print("||" + (" " * 46) + "||")
    print(f"||       Scanning ports on {target_machine} " + (" "*11) + "||")
    print("||" + (" " * 46) + "||")
    print("||" + (" " * 46) + "||")
    print("=" * 50)

#sys.argv contains the list of command line arguments passed to the script
#sys.argv[0] --> script name, [1] --> passed IP, ...
if len(sys.argv) == 2:
    target_machine = socket.gethostbyname(sys.argv[1])
else:
    print("Syntax: python3 port_scanner.py <IP>")
    sys.exit()

pretty_banner()
open_ports = []

try:
    for port in range(50, 85):
        socket.setdefaulttimeout(1) # will try to connect for 1s. Skips if not done
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target_machine, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    print(open_ports)
except KeyboardInterrupt:
    print("\nExiting Program...")
    sys.exit()
except socket.gaierror:
    print("\nHost can't be resolved.")
    sys.exit()
except socket.herror:
    print("\nUnable to connect to the server")
    sys.exit()



