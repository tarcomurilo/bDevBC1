#Create a decorator that makes sure that all function
#arguments where it's applied will match the regex on the regex exercise above.

import os

os.chdir('.\\Fourth\\')

from t01_regex import searchRegex

def decor(*args):
    
    def isInRegex(*args):
        for item in args:
            if searchRegex(item) != item:
                return False
            else:
                return True
    
    if isInRegex(args):
        return 

@decor
def myFunc(*args):
    for item in args:
        print(item)

lista = ['a_b', 'b_a']

myFunc(*lista)
