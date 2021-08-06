# This is the most complicated part. Write the function playstep2(hand, dice) that plays step 2 as
# explained above. This function takes a hand, which is a 3-digit integer, and it also takes dice,
# which is an integer containing all the future rolls of the dice. For example, if dice is 5341,
# then the next roll will be a 1, then the roll after that will be a 4, then a 3, and finally a 5.
# Note that in a more realistic version of this game, instead of hard-coding the dice in this way,
# we'd probably use a random-number generator.

# With that, the function plays step2 of the given hand, using the given dice to get the next rolls
# as needed. At the end, the function returns the new hand, but it has to be ordered, and the
# function also returns the resulting dice (which no longer contain the rolls that were just used).

# For example:
# assert(playstep2(413, 2312) == (421, 23))
# Here, the hand is 413, and the future dice rolls are 2312. What happens? Well, there are no
# matching dice (pair) in 413, so we keep the highest die, which is a 4, and we replace the 1 and the 3
# with new rolls. Since new rolls come from the right (the one's digit), those are 2 and 1. So the
# new hand is 421. It has to be sorted, but it already is. Finally, the dice was 2312, but we used 2
# digits, so now it's just 23. We return the hand and the dice, so we return (421, 23).

# For Example:
# assert(playstep2(544, 456) == (644, 45))
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# So the output is (644, 45)

# Here are some more examples. Be sure you carefully understand them:
# assert(playstep2(413, 2312) == (421, 23))
# assert(playstep2(413, 2345) == (544, 23))
# assert(playstep2(544, 23) == (443, 2))
# assert(playstep2(544, 456) == (644, 45))
# Hint: You may wish to use handToDice(hand) at the start to convert the hand into the 3 individual
# dice.
# Hint: Then, you may wish to use diceToOrderedHand(a, b, c) at the end to convert the 3 dice back
# into a sorted hand.
# Hint: Also, remember to use % to get the one's digit, and use //= to get rid of the one's digit.

# REFERENCE FROM https://github.com/Chiver/15-112-Fundamentals-of-Programming/blob/master/hw1_Version2.py

def handToDice(hand):
    # your code goes here
    # n=int(input())
    # x is for extraction of first digit
    # y is for extracting second digit
    # z is for extracting thrid digit
    x = (hand//100)
    temp = hand//10
    y = (temp % 10)
    z = (hand % 10)
    return x, y, z


def diceToOrderedHand(a, b, c):
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


def matchNum(hand):
    # this is for checking whether numbers are equal or not
    digitOne, digitTwo, digitThree = handToDice(hand)
    if digitOne == digitTwo == digitThree:
        return 3
    elif digitOne != digitTwo != digitThree:
        return 1
    else:
        return 2


def playstep2(hand, dice):
    getMatch = matchNum(hand)

    a, b, c = handToDice(hand)
    orderedHand = diceToOrderedHand(a, b, c)
    # Case one- when all the numbers are equal
    if getMatch == 3:
        return hand, dice
     # Case two -when all any 2 numbers are equal
    elif getMatch == 2:
        numOne, numTwo, numThree = handToDice(orderedHand)
        # Select the last digit of the dice
        numFour = dice % 10
        if numOne == numTwo:
            handChanged = diceToOrderedHand(numOne, numTwo, numFour)
            return handChanged, dice // 10

        elif numOne == numThree:
            handChanged = diceToOrderedHand(numOne, numThree, numFour)
            return handChanged, dice // 10

        else:
            handChanged = diceToOrderedHand(numThree, numTwo, numFour)
            return handChanged, dice // 10
    # Case three -when all the numbers are unequal
    else:
        numOne, numTwo, numThree = handToDice(orderedHand)
        secondHalf = dice % 100
        t1, t2, t3 = handToDice(numOne * 100 + secondHalf)
        changedHand = diceToOrderedHand(t1, t2, t3)

        return changedHand, dice // 100
