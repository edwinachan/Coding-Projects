#Write a function named firstNonRepeatingLetter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

#For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

#As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

#If a string contains all repeating characters, it should return the empty string ("").

def first_non_repeating_letter(string):

    count = 0

    stringLower = string.lower()

    if stringLower == '':
        return ''
    
    for i in range(len(string)):
        if stringLower.count(stringLower[i]) == 1:
            return string[i]

    for i in range(len(string)):
        if stringLower.count(stringLower[i]) == 2:
            count += 1
            if count == ((len(stringLower)+1)//2):
                return ''
            
  
#Test cases
#Test.describe('Basic Tests')
#Test.it('should handle simple tests')
#Test.assert_equals(first_non_repeating_letter('a'), 'a')
#Test.assert_equals(first_non_repeating_letter('stress'), 't')
#Test.assert_equals(first_non_repeating_letter('moonmen'), 'e')

#Test.it('should handle empty strings')
#Test.assert_equals(first_non_repeating_letter(''), '')

#Test.it('should handle all repeating strings') 
#Test.assert_equals(first_non_repeating_letter('abba'), '')
#Test.assert_equals(first_non_repeating_letter('aa'), '')

#Test.it('should handle odd characters')
#Test.assert_equals(first_non_repeating_letter('~><#~><'), '#')
#Test.assert_equals(first_non_repeating_letter('hello world, eh?'), 'w')

#Test.it('should handle letter cases')
#Test.assert_equals(first_non_repeating_letter('sTreSS'), 'T')
#Test.assert_equals(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')
