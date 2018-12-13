#There is an array with some numbers. All numbers are equal except for one. Try to find it!

#findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
#findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
#It’s guaranteed that array contains more than 3 numbers.

#The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[len(arr)-1]
    elif arr[0] != arr[1]:
        return arr[0]

#An more elegant method:    
def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e
