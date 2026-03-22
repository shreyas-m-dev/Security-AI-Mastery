#!/usr/bin/env python3
authorized_users = [ "Moni", "Shreyas", "Anu", "Bhuv", "Agustin", "Ags", "Agasthya" ]
while True:
 print(' ----New Access Request---- ')
 name = input("Enter your name (or type'exit' to stop): ")
 if name.lower() == 'exit':
  print('Shutting down.. Goodbye!')
  break
 try:
  if name in authorized_users:
   age = int(input('Enter your age: '))
   if age<0 or age>120:
    print('Access denied: Logical impossibility')
   elif age<18:
    print(f'Access Restricted for {name}. Status: Minor')
   else:
    print(f'Access Granted for {name}. Status: Authorized')
  else:
   print(f'Access Denied for {name}. Status: Unauthorized User')
 except ValueError:
  print('Error! Enter a valid no for age')
