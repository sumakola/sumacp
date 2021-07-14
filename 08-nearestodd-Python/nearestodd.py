# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.


import math
def fun_nearestodd(n):

	nOdd=math.ceil(n)
#if it is an odd number, minus it by one for getting odd no
	if(nOdd%2==0):
		return nOdd-1
	return nOdd
	


