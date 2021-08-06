# dicetoorderedhand(a, b, c) [5pts]
# Write the function dicetoorderedhand(a, b, c) that takes 3 dice and
# returns them in a hand, which is a 3-digit integer. However, even if the
# dice are unordered, the resulting hand must be ordered so that the largest
# die is on the left and smallest die is on the right. For example:
# assert(dicetoorderedhand(1,2,3) == 321)
# assert(dicetoorderedhand(6,5,4) == 654)
# assert(dicetoorderedhand(1,4,2) == 421)
# assert(dicetoorderedhand(6,5,6) == 665)
# assert(dicetoorderedhand(2,2,2) == 222)

# reference from https://github.com/Chiver/15-112-Fundamentals-of-Programming/blob/master/hw1_Version2.py

def dicetoorderedhand(a, b, c):
    # your code goes here
    # 123=100+20+3=(1*100)+(2*10)+(3*1)
    # this is for the hundreds digit
    x = max(a, b, c)
    digitHuns = 100*x
    # this is for the last digit
    z = min(a, b, c)
    digitOnes = z*1
    # this is  for the tens digit
    y = a+b+c-x-z
    digitTens = 10*y
    return digitHuns+digitTens+digitOnes
