#Moving Zeros To The End

#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

#Why do some tests fail!?

def move_zeros(array):
    newArray = []
    zeroCount = 0
    for element in array:
        if element != 0:
            newArray.append(element)
        else:
            zeroCount += 1

    zeroCountList = []
    for i in range(zeroCount):
        zeroCountList.append(0)
        
    return newArray + zeroCountList
