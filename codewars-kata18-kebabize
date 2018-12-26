#https://www.codewars.com/kata/kebabize/train/python

#Modify the kebabize function so that it converts a camel case string into a kebab case.

#kebabize('camelsHaveThreeHumps') // camels-have-three-humps
#kebabize('camelsHave3Humps') // camels-have-humps

#Test.assert_equals(kebabize('myCamelCasedString'), 'my-camel-cased-string')
#Test.assert_equals(kebabize('myCamelHas3Humps'), 'my-camel-has-humps')
#Test.assert_equals(kebabize('SOS'), 's-o-s')
#Test.assert_equals(kebabize('42'), '')
#Test.assert_equals(kebabize('CodeWars'), 'code-wars')

import re

numbers = '0123456789'

def kebabize(string):

    if string.isdigit():
        return '' #Handle a string that contains only digits
    
    newString = ''
    
    for char in string:
        if char not in numbers:
            newString += char #Get rid of any numbers in the string

    split = re.findall('[a-zA-Z][^A-Z]*', newString) #['my', 'Camel', 'Has', 'Humps']

    splitReunited = '-'.join(split)

    splitReunitedLower = splitReunited.lower()

    return splitReunitedLower
