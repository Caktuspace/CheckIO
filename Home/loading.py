#You are given a list of integer weights. You need to distribute these weights into two sets, such that the difference between the total weight of each set is as low as possible.
#Input data: A list of the weights.
#Output data: A number representing the lowest possible weight difference.
#Example:
#checkio([10,10]) == 0
#checkio([10]) == 10
#checkio([5, 8, 13, 27, 14]) == 3
#checkio([5,5,6,5]) == 1
#checkio([12, 30, 30, 32, 42, 49]) == 9
#checkio([1, 1, 1, 3]) == 0

# return the absolute result of the difference between two value
def absolute(data):
    a, b = data
    if a - b > 0:
        return a - b
    else:
        return b - a
 
# return the minimum gap between 'sum' and the sum of every items in the array
# and it subarrays
# An optimization would be to not have same subarray twice
def sumSubArray(data):
    sum, elts = data
    # breaking case the array only have one element
    if elts.__len__() == 1:
        return absolute([sum, elts[0]])
    tmp = 0
    # calculate the sum of every item in the array
    for item in elts:
        tmp += item
    res = absolute ([sum, tmp])
    for item in elts:
        tmpElts = list(elts)
        tmpElts.remove(item)
        # do the same treatment on the subarrays
        tmpRes = sumSubArray([sum, tmpElts])
        if tmpRes < res:
            res = tmpRes
    return res
     
 
def checkio(data):
    if data.__len__() == 1:
        return data[0]
    sum = 0
    for elt in data:
        sum += elt
    sum /= 2
     
    res = sumSubArray([sum, data])
	
    return res * 2
 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"