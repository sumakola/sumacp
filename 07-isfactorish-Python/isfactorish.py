# Write the function fun_isfactorish(n) that takes a value int n,
# and returns True if n is a (possibly-negative) integer with exactly 3 unique digits
# (so no two digits are the same), where each of the digits is a factor of the number
# n itself. In all other cases, the function returns False (without crashing).
# For example:
#  assert(fun_isfactorish(412) == True) # 4, 1, and 2 are all factors of 412
#  assert(fun_isfactorish(-412) == True) # Must work for negative numbers!
#  assert(fun_isfactorish(4128) == False) # 4128 has more than 3 digits
#  assert(fun_isfactorish(112) == False) # 112 has duplicate digits (two 1's)
#  assert(fun_isfactorish(420) == False) # 420 has a 0 (0 is not a factor)
#  assert(fun_isfactorish(42) == False) # 42 has a leading 0 (only 2 unique digits)


def digitCount(n):
    count = 0
    while(n > 0):
        n = n//10
        count += 1
    return count


def fun_isfactorish(n):
    t = n
    if (n < 0):
        n = -n

    if(digitCount(n) != 3):
        return False
    digitOne = n % 10
    n = n // 10
    digitTwo = n % 10
    n = n // 10
    digitThree = n % 10

    if(digitOne == 0 or digitTwo == 0 or digitThree == 0):
        return False
    elif(digitOne == digitTwo or digitTwo == digitThree or digitThree == digitOne):
        return False
    elif (t % digitOne == 0 and t % digitTwo == 0 or t % digitThree == 0):
        return True
    else:
        return False
