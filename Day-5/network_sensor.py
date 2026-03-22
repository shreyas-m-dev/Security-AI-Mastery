#!/usr/bin/env python3
import socket
from datetime import datetime
hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)
authorized_users = [ "Moni", "Shreyas", "Anu", "Bhuv", "Agustin", "Ags", "Agasthya" ]
while True:
 name = input("Enter your name (or type'exit' to stop): ")
 if name.lower() == 'exit':
  break
 if name in authorized_users:
  status = 'Granted'
 else:
  status = 'Denied'
 timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
 with open("network_access.log","a") as f:
  log_msg = f"[{timestamp}] - IP: {ip_addr} - User: {name} - Status: {status} - Host: {hostname}\n"
  f.write(log_msg)
 print(f"Log updated: Access {status} for {name}.")
