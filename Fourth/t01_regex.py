#Write a Python regex function to find sequences of lowercase letters joined with an underscore.

import re

def searchRegex(string):
   try:
      match = re.search('[a-z]+_[a-z]+', string)
      return match.group(0)
   except:
      match = ''
      return ''

