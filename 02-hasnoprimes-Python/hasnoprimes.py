# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

def isPrimenombre(n):
	if(n<2):
		return False
	if(n==2):
		return True
	if(n%2==0):
		return False
	f=round(n**0.5)
	for i in range(3,f+1,2):
		if(n%i==0):
			return False
	return True

def fun_hasnoprimes(l):
	a=l
	for rowlst in range(len(a)):
		for collst in range(len(a[rowlst])):
			if(isPrimenombre(a[rowlst][collst])):
				return False
	return True




