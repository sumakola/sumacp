# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.

import math
#distance formula function
def distance(x1,x2,y1,y2):
	return(float(math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))))

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	# your code goes here
	#for the circles to intersect, their distance between the centres 
	# must be equal to or less than the sum of their radii
	#c1c2=r1+r2
	centre=distance(x1,x2,y1,y2)
	if (centre<=(float(r1+r2))):
		return True
	else:
		return False

