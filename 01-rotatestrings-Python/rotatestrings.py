# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k.
# If k is non-negative, the function returns the string s rotated k places to the left.
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')


def rotateStringLeft(s, n):
    k = len(s)
    n = n % k
    x = s[n:k]
    y = s[0: n]
    return (x + y)


def rotateStringRight(s, n):
    k = len(s)
    n1 = abs(n)
    n1 = n1 % k
    x = s[k-n1:k]
    y = s[0:k-n1]
    return (x+y)


def fun_rotatestrings(s, n):
    if(n > 0):
        return(rotateStringLeft(s, n))
    elif(n == 0):
        return(s)
    else:
        return(rotateStringRight(s, n))
