#Write a Python function using list comprehension that receives a list of words and returns a 
# list that contains:
#The number of characters in each word if the word has 3 or more characters
#The string “x” if the word has fewer than 3 characters

def numList(wordlist):
    numListing = [len(item) if len(item) >= 3 else "x" for item in wordlist]
    return numListing

flag = True

print("Type a word or nothing to exit:")
wordlist = []

while flag:
    text = input("> ")
    if text == '':
        flag = False
    else: 
        wordlist.append(text)

print(numList(wordlist))
    