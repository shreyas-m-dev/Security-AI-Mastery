#!/usr/bin/env python3
while True:
	print('\n---- New Access Request ----')
	name = input("Enter name (or type 'exit' to stop):")
	if name.lower()=='exit':
		print('Shutting down monitor. Goodbye!')
		break
	try:
		age = int(input('Enter age:'))
		if age<0 or age>120:
			print('Alert! logical impossibility detected.')
		elif age<18:
			print(f'Access Restricted for {name}. Status: Minor')
		else:
			print(f'Access Granted for {name}. Status: Authorized')
	except ValueError:
		print('Error: Please enter a valid number of age.')

