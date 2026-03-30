#!/usr/bin/env python3
import socket
import datetime
import time
def trigger_alert(port, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"[{timestamp}] !!! ALERT !!! Unauthorized Port {port} Detected! Status: {status}\n"
    print(msg)
    with open("guardian_alerts.log", "a") as f:
        f.write(msg)
Allowed_Ports = [22, 80]
target = "127.0.0.1"
print(f"Scanning for open ports in {target}...")
while True:
    for port in range(1, 8900): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((target, port))
        if result == 0:
            if port not in Allowed_Ports:
                trigger_alert(port, "UNAUTHORIZED_PORT_DETECTED")
        s.close()
    print("Scan cycle complete. Sleeping for 60 seconds...")
    time.sleep(60)
