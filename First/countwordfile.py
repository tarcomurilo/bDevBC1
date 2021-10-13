# 5 Write a Python program to count the frequency of words in a text file.
import re

print('Type the name of the text file: ')
filename = input('> ')

try:
    file = open(filename)
except:
    print('File do not exist!')
    exit()

text = file.read()
text = text.replace("\"", ' ')
text = text.replace(".", ' ')
text = text.replace(",", ' ')
text = text.replace(":", ' ')
text = text.replace("!", ' ')
text = text.replace("?", ' ')
text = text.replace(";", ' ')

text = text.split()

text_set = set(text)

for word in text_set:
    print(f'{word}: {text.count(word)}')
