# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...
# reference from https://www.geeksforgeeks.org/check-whether-a-matrix-is-a-latin-square-or-not/
def isLatinSquare(lst):
    # Your code goes here...
    a = len(lst)
    r = []
    for i in range(a):
        r.append(set([]))
    c = []
    for i in range(a):
        c.append(set([]))
    notValid = 0
    for i in range(a):
        for j in range(a):
            r[i].add(lst[i][j])
            c[j].add(lst[i][j])

            if (lst[i][j] > a or lst[i][j] <= 0):
                notValid += 1

    numOfRows = 0
    numOfCols = 0
    for i in range(a):
        if (len(r[i]) != a):
            numOfRows += 1
        if (len(c[i]) != a):
            numOfCols += 1
    if (numOfCols == 0 and numOfRows == 0 and notValid == 0):
        return True
    else:
        return False


lst = [[1, 2],
       [2, 1]]
assert(isLatinSquare(lst) == True)


lst = [[1, 2, 3],
       [3, 1, 2],
       [2, 3, 1]]

assert(isLatinSquare(lst) == True)

lst1 = [[1, 2, 3, 4],
        [4, 1, 2, 3],
        [3, 4, 1, 2],
        [2, 3, 4, 1]]

assert(isLatinSquare(lst1) == True)

lst2 = [[1, 2, 3, 4, 5],
        [2, 1, 3, 5, 4],
        [3, 4, 2, 1, 5],
        [4, 1, 3, 2, 6]]

assert(isLatinSquare(lst2) == False)
print("All test cases passed")
