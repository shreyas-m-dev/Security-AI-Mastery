#!/usr/bin/env python3
import os
import socket
import datetime
import time
def block_attacker(attacker_ip):
 print(f"[!] Blocking Attacker: {attacker_ip}")
 command = f"sudo iptables -A INPUT -s {attacker_ip} -j DROP"
 os.system(command)
 
 with open("firewall_history.log", "a") as f:
  f.write(f"{datetime.datetime.now()}: Banned {attacker_ip}\n")
def trigger_alert(port, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"[{timestamp}] !!! ALERT !!! Unauthorized Port {port} Detected! Status: {status}\n"
    print(msg)
    with open("guardian_alerts.log", "a") as f:
        f.write(msg)
Allowed_Ports = [22, 80]
target = "127.0.0.1"
attacker_ip = "172.17.220.22"
print(f"[*] Guardian Wall Active. Monitoring {target}...")
while True:
    for port in range(1, 8900): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((target, port))
        if result == 0:
            if port not in Allowed_Ports:
                trigger_alert(port, "UNAUTHORIZED_PORT_DETECTED")
                block_attacker(attacker_ip)
        s.close()
    print("Scan cycle complete. Sleeping for 10 seconds...")
    time.sleep(10)
