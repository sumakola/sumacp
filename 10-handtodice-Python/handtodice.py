# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	# your code goes here
	#n=int(input())
	# x is for extraction of first digit
	#y is for extracting second digit
	#z is for extracting thrid digit
	x=(hand//100)
	temp=hand//10
	y=(temp%10)
	z=(hand%10)
	return x, y, z