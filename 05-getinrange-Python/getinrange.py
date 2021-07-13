# Write the function getInRange(x, bound1, bound2) which takes 3 int values
# x, bound1, and bound2, where bound1 is not necessarily less than bound2. 
# If x is between the two bounds, just return it unmodified. Otherwise, 
# if x is less than the lower bound, return the lower bound, 
# or if x is greater than the upper bound, return the upper bound.

def fun_getinrange(x, bound1, bound2):
	# your code goes here
	#taking low value of bound1 
	lowBound=min(bound1, bound2)
	#taking higher bound
	highBound=max(bound1, bound2)
	#according to questions
	if x<lowBound:
		return lowBound
	#according to questions
	elif x>highBound:
		return highBound
	#according to questions
	else:
		return x


