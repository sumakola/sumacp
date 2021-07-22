
def isPrime(n):

    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):  
        if n%i==0:
            return False    
    return True
# Function to get sum of digits
def getSum(n):

	sum = 0
	while (n != 0):
		sum = sum + n % 10
		n = n / 10
	return sum


def isAdditivePrime(n):


	if (not isPrime(n)):
		return False
	return isPrime(getSum(n))
N=98
if (isAdditivePrime(N)):
	print(True)
else:
	print (False)





