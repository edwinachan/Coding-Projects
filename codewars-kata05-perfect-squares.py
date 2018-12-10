#Given an integral number, determine if it's a square number:

#In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

#The tests will always use some integral number, so don't worry about that in dynamic typed languages.

#Examples

#test.assert_equals(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
#test.assert_equals(is_square( 0), True, "0 is a square number")
#test.assert_equals(is_square( 3), False, "3 is not a square number")
#test.assert_equals(is_square( 4), True, "4 is a square number")
#test.assert_equals(is_square(25), True, "25 is a square number")
#test.assert_equals(is_square(26), False, "26 is not a square number")

import math

def is_square(n):
    if n >= 0:
        #The square root function gives a floating number so we must convert to an integer
        i = int(math.sqrt(n))
        if (n == i*i):
            print(str(n) + ' is a square number')
            return True
        elif (n != i*i):
            print(str(n) + ' is not a square number')
            return False    
    elif n < 0:
        print(str(n) + ': Negative numbers cannot be square number')
        return False
