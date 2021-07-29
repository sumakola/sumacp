# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both
# guaranteed to not contain any 0's, and
# returns True if x is a rotation of the digits of y and False otherwise. For example,
# 3412 is a rotation of 1234. Any number
# is a rotation of itself.

def isrotation(x, y):
    # Your code goes here
    size1 = len(str(x))
    size2 = len(str(y))
    temp = ''

    if size1 != size2:
        return False

    temp = str(x) + str(x)

    if (temp.count(str(y)) > 0):
        return True
    elif(str(y)[::-1] == str(x) or str(x)[::-1] == str(y)):
        return True
    else:
        return False
