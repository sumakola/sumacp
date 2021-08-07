# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem.

# reference from https://stackoverflow.com/questions/26689929/power-function-using-recursion
def powersof3ton(n, a):
    if(n < a):
        return []
    elif(3**a <= n):
        return [3**a]+powersof3ton(n, a+1)
    else:
        return []


def recursion_powersof3ton(n):
    # Your code goes here
    if n < 1:
        return None
    elif(n == 1):
        return[int(n)]
    else:
        return powersof3ton(n, a=0)
