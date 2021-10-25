#Create a decorator that makes sure that all function
#arguments where it's applied will match the regex on the regex exercise above.

import os

os.chdir('.\\Fourth\\')

from t01_regex import searchRegex

def decor(func):
    retarg = []
    def capsule(*val):
        for item in val:
            if func(item) == []:
                pass
            else:
                retarg.append(item)

    return capsule


@decor
def myFunc(*args):
    for item in args:
    return searchRegex(args)

lista = ['a_b', 'b_a', "B_a"]

print(myFunc(*lista))
