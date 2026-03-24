#!/usr/bin/env python3
import socket
target = "127.0.0.1"
print(f'Scanning target....{target}')
for port in range (1,9024):
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.settimeout(0.5)
 result = s.connect_ex((target, port))
 if result == 0:
  print(f'[!]Port {port} is Open on {target}')
 s.close()
print('Scan Complete.')
