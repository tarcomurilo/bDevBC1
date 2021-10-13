#Write a Python program that takes user input 
#and runs it as a command using the os module.

import os

print(f'Enter a command (e.g. dir /p)') #start

command = input('> ') #input the command

os.system(command)