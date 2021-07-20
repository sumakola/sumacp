# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(x):
    if(rowsSum(x)==True and columnsSum(x)==True and diagonalsSum(x)==True):
        return True
    else:
        return False
		
def rowsSum(x):
    sumOfRows=sum(x[0])
    for i in x:
        value=sum(i)
        if value==sumOfRows:
            return True

def diagonalsSum(x):
    diagonalOne=0
    diagonalTwo=0
    for i in range(len(x)):
        diagonalOne+=x[i][1]
        diagonalTwo+=x[len(x)-i-1][len(x)-i-1]
    if diagonalOne==diagonalTwo:
        return True

def columnsSum(x):
    sumOfCols=0
    for i in range(len(x)):
        sumOfCols+=x[i][0]

    for i in range(len(x)):
        value=0
        for j in range(len(x)):
            value+=x[i][j]
        if value==sumOfCols:
            return True 

