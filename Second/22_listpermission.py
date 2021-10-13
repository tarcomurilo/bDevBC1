#Write a Python program to get the size, permissions, owner, device, created, 
#last modified, and last accessed date time of a specified path.

import os
import time

print(f'Enter a file or folder (e.g. C:\\Path\\)') #start

path = input('> ') #input the folder

os.chdir(path) #change working directory

print(f'Accessing: {os.getcwd()}') #erase

print(f'Enter a filename:') #start

filename = input('> ') #input the folder

stats = os.stat(path+filename)
print(stats)

print(f'Size: {os.path.getsize(path + filename)} bytes')
print(f'Permissions: {oct(stats.st_mode)} ')
print(f'Owner: none')
print(f'Device: none')
print(f'Created: {time.ctime(os.path.getctime(path + filename))}')
print(f'Last modified: {time.ctime(os.path.getmtime(path + filename))}')
print(f'Last accessed: {time.ctime(os.path.getatime(path + filename))}')

