#04 Write a Python program to count the number of lines in a text file.

print('Type the name of the text file: ')
filename = input('> ')

try:
    file = open(filename)
except:
    print('File do not exist!')
    exit()

text = [] 

for line in file:
    text.append(line)

print(f'The text file has {len(text)} lines')