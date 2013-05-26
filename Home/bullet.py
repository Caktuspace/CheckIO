The wall is represented by two coordinates W1 (xw1, yw1) and W2 (xw2, yw2) on a coordinate plane. The bullet flies from point "A" (xa, ya), and the direction of its flight is given by the second point "B" (xb, yb). Determine whether the bullet hits the wall or not if gravity is not a factor. A != B.
#Input: Four lists with coordinates--each one is a list of x and y coordinates--W1, W2, A, B (Integers).
#Output: Whether the bullet hits the wall or not, aka True or False.
#Example:
#checkio([[0, 0], [0, 2], [5, 1], [3, 1]]) == True
#checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False
#checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True
#checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False
#checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True
#checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False

def betweenTwo(data):
    a, x, y = data
    if x > y:
        return a >= y and a <= x
    else:
        return a <= y and a >= x
         
def checkio(data):
    xw1, yw1 = data[0]
    xw2, yw2 = data[1]
    xa, ya = data[2]
    xb, yb = data[3]
    v1 = xa == xb 
    v2 = xw1 ==xw2 
    if v1 == v2 == True:
        return False
    if v1:
        aWall = (yw2-yw1)/(xw2-xw1)
        bWall = yw1 - (aWall * xw1)
        y = aWall * xw1 + bWall
        if xw1 - xw2 > 0:
            return betweenTwo([y, ya, yb]) and xa >= xw1 
        return betweenTwo([y, ya, yb]) and xa <= xw1
    elif v2:
        aBullet = (yb-ya)/(xb-xa)
        bBullet = ya - (aBullet * xa)
        y = aBullet * xa + bBullet
        if xa - xb > 0:
            return betweenTwo([y, yw1, yw2]) and xa >= xw1
        return betweenTwo([y, yw1, yw2]) and xa <= xw1
    else:
        aWall = (yw2-yw1)/(xw2-xw1)
        bWall = yw1 - (aWall * xw1)
        aBullet = (yb-ya)/(xb-xa)
        bBullet = ya - (aBullet * xa)
         
    if aBullet == aWall:
        if xa - xb > 0:
            return bBullet == bWall and xa >= xw1
        return bBullet == bWall and xb <= xw1
    xCommun = round((bWall - bBullet) / (aBullet - aWall), 1)
    if xa - xb > 0:
        return betweenTwo([xCommun, xw1, xw2]) and betweenTwo([xCommun, xa , -1000])
    return betweenTwo([xCommun, xw1, xw2]) and betweenTwo([xCommun, xa, 1000])

 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0,0], [0,2], [5,1], [3,1]]) == True, "1st example"
    assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "2nd example"
    assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "3rd example"
    assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "4th example"
    assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "5th example"
    assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "6th example"