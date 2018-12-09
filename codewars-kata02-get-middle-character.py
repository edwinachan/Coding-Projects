#You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd,
#return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

#Kata.getMiddle("test") should return "es"

#Kata.getMiddle("testing") should return "t"

#Kata.getMiddle("middle") should return "dd"

#Kata.getMiddle("A") should return "A"

s = 'middle'
t = 'testing'
new = 'jRidkgLPfgwosh'

def get_middle(s):
    if len(s) % 2 == 0:
    #Be sure to do integer division. Using a single '/' gives a floating
        return s[len(s)//2] + s[(len(s)//2)-1]
    elif len(s) % 2 == 1:
        return s[(len(s) - 1)//2]

print(get_middle(s))

print(get_middle(t))

print(get_middle(new))

