#The goal of this exercise is to convert a string to a new string where each character in the new string is '('
#if that character appears only once in the original string, or ')' if that character appears more than once in the original string.
#Ignore capitalization when determining if a character is a duplicate.

#Examples:

#"din" => "((("

#"recede" => "()()()"

#"Success" => ")())())"

#"(( @" => "))(("

#Counter is a subclass of 'dict' and counts hashable objects in Python
#https://data-flair.training/blogs/python-counter/

from collections import Counter

def duplicate_encode(word):
    #Ignore capitalisation
    word = word.lower()
    #Start new list 
    new_word = ''
    #Initialise the counter by passing in variable
    c = Counter(word)
    for letter in word:
        if c[letter] == 1:
            letter = '('
        elif (c[letter] > 1):
            letter = ')'
        new_word += letter
    return new_word

print(duplicate_encode("din"))
