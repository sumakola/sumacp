# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a
# number n is a product of x and (x+1).

# 12--> 3*4

def pronicnum(n):
    for i in range(1, n+1):
        if(i*(i+1) == n):
            return True
    return False


def nthpronicnumber(n):
    # Your code goes here
    x = 1
    y = 0
    while(x <= n):
        y += 1
        if(pronicnum(y)):
            x += 1
    return y
