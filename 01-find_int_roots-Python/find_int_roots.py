# Write the function bonusFindIntRoots(a,b,c) that takes 
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that 
# the roots are all integers. Your function should return these 2 int roots 
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

import math
def fun_find_int_roots(a, b, c):
	disc=int((b*b)-(4*a*c))
	if disc>0:
		rootOne=int(-b+math.sqrt(disc))/(2*a)
		rootTwo=int(-b-math.sqrt(disc))/(2*a)
		if (rootOne>rootTwo):
			return (rootTwo, rootOne)
		return (rootOne, rootTwo)
	elif (disc==0):
		rootOne=(-b/(2*a))
		rootTwo=(-b/(2*a))
		return (rootOne, rootTwo)
	else:
		return (0,0)

