# 03 Write a Python program that accepts a filename from the user and prints the filename’s extension.
# Sample filename : abc.java
# Output : java

text_input = ''

while text_input != '0':

    print('Write a file name: ')
    text_input = input('> ')

    extension = text_input.split(sep='.')

    print(extension[len(extension) - 1])
