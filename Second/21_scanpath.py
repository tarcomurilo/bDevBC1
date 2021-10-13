#Write a Python program to scan a specified 
#directory and identify the sub directories and files.

import os 

print(f'Enter a folder (e.g. C:\\Path\\)') #start

path = input('> ') #input the folder

os.chdir(path) #change working directory

print(f'Scanning: {os.getcwd()}') #erase

dirs = os.listdir(path)

for dir in dirs:
    print(dir)
