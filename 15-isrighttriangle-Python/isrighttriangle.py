# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

import math
#distance formula function
def distance(x1,x2,y1,y2):
	return(float(math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))))

#for comparing floats
def almostEqual(d1, d2):
    epsilon = 10**-10
    return (abs(d2 - d1) < epsilon)

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a=distance(x1, x2, y1, y2)
	b=distance(x3, x2, y3, y2)
	c=distance(x3, x1, y3, y1)
	aSq=a**2
	bSq=b**2
	cSq=c**2
	d=a**2+b**2
	e=a**2+c**2
	f=b**2+c**2

	if ((almostEqual(d,cSq) or almostEqual(e,bSq) or almostEqual(f,aSq)) and (d>0 and e>0 and f>0)):
		return True
	else:
		return False




