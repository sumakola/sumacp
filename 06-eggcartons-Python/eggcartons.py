# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	# your code goes here
	#if the number of eggs is a multiple of 12, then we can written the quotient of the num//12
	if eggs%12==0:
		return eggs//12
	#else we need to add the num by dividng with 12 and give it an extra count
	else:
		return(int(eggs/12)+1)
	
