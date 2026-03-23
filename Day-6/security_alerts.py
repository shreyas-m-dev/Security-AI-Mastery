#!/usr/bin/env python3
import socket
from datetime import datetime
hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)
authorized_users = [ "Moni", "Shreyas", "Anu", "Bhuv", "Agustin", "Ags", "Agasthya" ]
def trigger_alert(name, ip, current_status):
 print('!!!!!ALERT!!!!!')
 timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
 with open("security_alert.log","a") as alert:
  alrt_msg = f"[{timestamp}] - IP: {ip} - Status: {current_status} Alert: User {name} flagged as suspicious on Host {hostname}\n"
  alert.write(alrt_msg)
while True:
 name = input("Enter your name (or type'exit' to stop): ")
 if name.lower() == 'exit':
  break
 if name in authorized_users:
  status = 'Granted'
 else:
  status = 'Denied'
  trigger_alert(name,ip_addr,status)
 timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
 with open("network_access.log","a") as f:
  log_msg = f"[{timestamp}] - IP: {ip_addr} - User: {name} - Status: {status} - Host: {hostname}\n"
  f.write(log_msg)
 print(f"Log updated: Access {status} for {name}.")
