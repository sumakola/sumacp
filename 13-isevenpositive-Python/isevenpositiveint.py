# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

def isevenpositiveint(x):
	# your code goes here
	#cheching for lists and tuples
	if type(x)!= int:
		return False
	#checking for given conditions
	elif(x%2 == 0 and x>0 and type(x)==int):
		return True
	else:
		return False
