
# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k)  or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.

def powersum(n, k):
    sum = 0
    #according to the question
    if(n<0 or k<0):
        return 0
    #power sum, iterating thro all n nos, adding the powers of digits
    for i in range(1, n + 1, 1):
        sum += pow(i, k)
    return sum
# Write your own test cases here...

#print ("All test cases passed...")
