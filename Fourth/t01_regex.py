#Write a Python regex function to find sequences of lowercase letters joined with an underscore.

import re

def searchRegex(string):
   try:
      match = re.findall('[a-z]+_[a-z]+', string)
      return match
   except:
      match = ''
      return ''

string = "aBcdeb_ghIjk_jkk_Op_o"

for item in searchRegex(string):
   print(item)
