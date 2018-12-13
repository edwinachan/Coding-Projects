#Find the missing letter

#Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

#You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
#The array will always contain letters in only one case.

#Example:

#['a','b','c','d','f'] -> 'e'
#['O','Q','R','S'] -> 'P'

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def find_missing_letter(chars):
    lowerCase = [x.lower() for x in chars]

    lower = lowerCase[0] #define the 'smallest' letter
    lowerInAlpha = alphabet.index(lower) #this gives the position of the smallest letter in the alphabet
    upper = lowerCase[-1] #define the 'largest' letter
    upperInAlpha = alphabet.index(upper) #this gives the position of the largest letter in the alphabet
    #We now have the lower and upper bound of the range of chars


    for i in range(lowerInAlpha, upperInAlpha+1): #We must use upperinAlpha + 1 as the range(start,stop) function generates numbers up to but not including the figure which represents 'stop' 
        if alphabet[i] not in lowerCase:
            return alphabet[i]
#Why is this for loop incorrect when I use "not in chars"!?
 
chars = ['O','Q','R','S']

print(find_missing_letter(chars))
