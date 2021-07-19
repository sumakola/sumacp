# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	diff = 10**5
	b = len(a)
	a.sort()
	if(b == 1):
		diff = a[0]
	if(b == 0):
		diff = -1
	for i in range(b-1):
		if abs(a[i]-a[i+1]) < diff: 
			diff = abs(a[i] - a[i+1])
	return diff
