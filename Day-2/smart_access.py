#!/usr/bin/env python3
name = input("Enter name: ")
age = int(input("Enter age: ")) 
if age < 0 or age > 120:
    print("ALERT: Logical impossibility detected. Terminating.")
elif age < 18:
    print(f"Access Restricted for {name}. Status: Minor.")
else:
    print(f"Access Granted for {name}. Status: Authorized.")
