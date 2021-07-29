# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value,
# which is the value of the middle element, or the average of the two middle elements if there is no single middle
# element. If the list is empty, return None.

def median(a):
    # your code goes here
    newA = sorted(a)
    b = len(a)
    index = (b - 1) // 2
    if(b == 0):
        return None
    if (b % 2 != 0):
        return newA[index]
    else:
        return (newA[index] + newA[index + 1])/2.0
