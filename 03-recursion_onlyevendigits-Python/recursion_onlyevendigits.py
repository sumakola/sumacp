# Without using iteration and without using strings,
# write the recursive function onlyEvenDigits(L),
# that takes a list L of non-negative integers
# (you may assume that), and returns a new list of
# the same numbers only without their odd digits
# (if that leaves no digits, then replace the number with 0).
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844].
# Also the function returns the empty list if the original list is empty.
# Remember to not use strings. You may not use loops/iteration in this problem.


def fun_recursion_onlyevendigits(l, finl=None, count=0):
    if finl == None:
        finl = []
    if l == [] and count == 0:
        return l
    if len(l) == 0:
        return finl
    else:
        count += 1
        # we will call our helper fuction on every number to convert them into
        # numbers made of only even numbers
        newNum = checkForEvens(l[0])
        finl.append(newNum)
        return fun_recursion_onlyevendigits(l[1:], finl, count)


def checkForEvens(number, newNum=0, powers=1):
    # base case checks if we have already loooped through the whole number
    digit = number % 10
    if number <= 0:
        return newNum
    else:
        # first we get the number from the very left
        if digit % 2 == 0:
            # add the firstDigit to our newNum
            newNum += digit * powers
            number //= 10
            # strip down the number by 10
            powers *= 10
            return checkForEvens(number, newNum, powers)
        else:
            number //= 10
            return checkForEvens(number, newNum, powers)
