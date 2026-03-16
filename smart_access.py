#!/usr/bin/env python3
name = input('Enter your name:')
age = int(input('Enter your age:'))
if age<0 or age>120:
	print('ALERT: logical impossibility detected. Terminating.')
elif age<18:
	print(f'Access restricted for {name}. Status:Minor')
else:
	print(f'Access granted for {name}. Status:Authorized')

