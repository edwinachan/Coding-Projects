#Given an array, find the int that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.

#test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

def find_it(seq):
    for num in seq:
        count = seq.count(num)
        if count % 2 == 1:
            return num
        else:
            continue
