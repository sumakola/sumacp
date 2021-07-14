# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
    flag = False
    if(n < 0):
        n = -n
        flag = True
    inc = 0
    newNo = 0
    while(inc<=k or n > 0):
        r = n % 10
        if inc == k:
           newNo=newNo + (d * (10 ** inc))
        else:
           newNo =newNo + (r * (10 ** inc))
        inc += 1
        n = n // 10
    
    if flag:
       newNo =-newNo
    return (newNo)
   


