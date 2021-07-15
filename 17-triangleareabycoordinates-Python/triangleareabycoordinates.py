# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
import math

def distance(x1, y1, x2, y2):
	#by the distance formula ((x2-x1)^2 +(y2-y1)^2)^0.5
	return(float(math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))))

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	s1=distance(x1, y1, x2, y2)
	s2=distance( x2, y2, x3, y3)
	s3=distance(x3, y3,x1, y1)
	semiPer=float((s1+s2+s3)/2.0)
	areaOfTriangle=float((semiPer*(semiPer-s1)*(semiPer-s2)*(semiPer-s3))**0.5)
	return areaOfTriangle

