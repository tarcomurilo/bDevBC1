#Write a Python program to count the number of 
# strings where the string length is 2 or more and the 
# first and last character are the same from a given list of strings.
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2

lista = ['eita', 'nossa,', 'saias', 'ele', 'aa', 'olho']

for string in lista:
    if (string[0] == string[-1]) and (len(string) > 2):
        print(string)