# Write the function isFactor(f, n) that takes 
# two int values f and n, and returns True 
# if f is a factor of n, and False otherwise. 
# Note that every integer is a factor of 0.



def fun_isfactor(f, n):
	n1=abs(n)
	f1=abs(f)
	if(n1==0 and f1==0):
		return True
	elif(f1==0):
		return True
	elif(n1==0):
		return True
	elif(n1%f1==0):
		return True
	else:
		return False 
