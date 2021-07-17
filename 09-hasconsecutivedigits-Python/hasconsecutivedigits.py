# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	x= abs(n)
	if x==0:
		return False
	else:
		while(x>0):
			
			y=x%10
			z=y
			x=int(x//10)
			y=x%10
			if( z== y):
				return True
		return False        
