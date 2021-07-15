# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.


def mostfrequentdigit(n):
	#for frequency of the digits
    mostFreqdigit = 0
    freqOcc= 0
    for i in range(0 , 10):
        count = digitsCount(i , n)
        if(count > freqOcc):
            freqOcc = count
            mostFreqdigit = i            
    return mostFreqdigit


def digitsCount(i , n):
	#for count of digits of the given number
    dCount = 0
    while(n > 0):
        u= n % 10
        if(u== i):
            dCount = dCount + 1
        n = n //10
    return dCount
