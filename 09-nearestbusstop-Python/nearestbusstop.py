# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	#streets=abs(street)
	if(street%2==0):
		if(street%8==0):
			street1=street
			return street1
		street1=street-4
		return street1

	else:
		street1=street+3
		return street1
