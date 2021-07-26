# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)
#lognbase10
def findDigitSquaresum(n, sum = 0):
	if(n>0):
		sum+=(n%10)**2
		n=n//10
		return findDigitSquaresum(n, sum)
	return sum

# print (findDigitSquaresum(125))
# assert(findDigitSquaresum(125) == 30)
# assert(findDigitSquaresum(1) == 1)
# assert(findDigitSquaresum(0) == 0)
# assert(findDigitSquaresum(12) == 5)
# print ("All test cases passed. :-)")

def ishappynumber(n):
	sum = findDigitSquaresum(n)
	if sum == 1:
			return True
	elif sum<10:
		return False
	else:
		return ishappynumber(sum)
def nth_happy_number(n):
	x = 1
	y = 0
	while(x<=abs(n)):
		y+=1
		if(ishappynumber(y)):
			x+=1
	return y

