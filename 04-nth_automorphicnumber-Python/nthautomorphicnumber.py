# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6,
# 76 and 890625 are all automorphic numbers.

def isAutomorphicNum(n):

    Num = n
    sq = Num * Num
    while (Num > 0):
        if(Num % 10 != sq % 10):
            return False
        Num = int(Num//10)
        sq = int(sq//10)
    return True


def nthautomorphicnumbers(n):
    # Your code goes here
    f = 2
    g = 0
    while(f <= n):
        g += 1
        if(isAutomorphicNum(g)):
            f += 1
    return g
