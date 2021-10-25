#Write a Python regex function to find sequences of lowercase letters joined with an underscore.

import re

def searchRegex(string):
   try:
      match = re.findall('[a-z]+_[a-z]+', string)
      return match
   except:
      match = ''
      return ''

