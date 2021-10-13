#6 Write a Python program that takes an input string from the user and counts the
#  frequency of characters in the string.
#Sample String : google.com
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

import re

text_input = '0'

while text_input != '':

    print('Press enter to exit or type a text, please: ')
    text_input = input('> ')

    text_set = set(text_input)

    for letter in text_set:
        print(f'{letter}: {text_input.count(letter)}')





