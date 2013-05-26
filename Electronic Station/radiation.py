#We have a matrix A NxN (3<=N<=10). The numbers 1 through 5 are used to label the different kinds of spare parts--the elements of A. Find the largest group of identical numbers adjacently joined to each other and point out both the quantity of the spare parts within the group and the number of the spare part itself.
#Input: A list of lists. Each list contains integers
#Output: A list of two integers -- size and mark of biggest union.
#Example:
#checkio([
# [1,2,3,4,5],
# [1,1,1,2,3],
# [1,1,1,2,2],
# [1,2,2,2,1],
# [1,1,1,1,1]
#])==[14,1]

def search(x, y, grid, watch):
    if grid[x][y] != watch:
        return 0
    if grid[x][y] == watch + 10:
        return 0
  
    # mark as visited
    grid[x][y] = watch + 10
     
    sum = 1
    # explore neighbors
    if x < len(grid)-1:
        sum += search(x+1, y, grid, watch)
    if y < len(grid)-1:
        sum += search(x, y+1, grid, watch)
    if x > 0:
        sum += search(x-1, y, grid, watch)
    if y > 0:
        sum += search(x, y-1, grid, watch)
    return sum
 
def checkio(matrix):
    res = [0, 0]
    tmp = 0
    i = 0
    j = 0
     
    while 1:
        while matrix[i][j] > 5:
            print(i,j)
            if j == matrix[i].__len__() - 1:
                j = 0
                if i == matrix.__len__() - 1:
                    return res
                else:
                    i += 1
            else:
                j += 1
        tmp = matrix[i][j]
        size = search(i, j, matrix, matrix[i][j])
        if size > res[0]:
            res = [size, tmp]
        j = 0
        i = 0
 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"
 
    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'