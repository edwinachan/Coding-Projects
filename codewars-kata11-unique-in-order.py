#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

#For example:

#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(s):
    s = list(s)
    
    newList = []

    if s == []:
        return s #Be able to handle empty lists
    
    newList.append(s[0]) #As we're moving from left to right, the first value in s will always be valid
                        #This also gives us something to compare to on the 'left hand side'
                        #It means i in the loop variable will look at the previous value and won't go out of range

    for i in range(1,len(s)):
        if s[i] == s[i-1]: #As we've appended s[0], we are able to look backwards to compare
            continue
        elif s[i] != s[i-1]:
            newList.append(s[i])
    return newList

#A bit more elegant:

def unique_in_order(s):
    newList = []

    for i in s:
        if newList == []:
            newList.append(i)
        elif newList[-1] != i:
            newList.append(i)
    return newList
