# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L
# contains any duplicate values (that is,
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
    # Your code goes here
    a = []
    counter = 0
    for i in range(len(L)):
        for j in range(len(L[0])):
            if(L[i][j] not in L):
                a.append(L[i][j])
                counter += 1

    a = set(a)
    lenA = len(a)
    if(lenA == counter):
        return False
    else:
        return True
