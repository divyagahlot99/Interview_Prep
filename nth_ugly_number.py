def nthUglyNumber(n):
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    nextMultipleOf2 = ugly[i2] * 2
    nextMultipleOf3 = ugly[i3] * 3
    nextMultipleOf5 = ugly[i5] * 5
    
    for i in range(1, n):
        ugly_no = min(nextMultipleOf2, nextMultipleOf3, nextMultipleOf5)
        ugly[i] = ugly_no
        if (nextMultipleOf2 == ugly[i]):
            i2 += 1
            nextMultipleOf2 = ugly[i2] * 2
        if (nextMultipleOf3 == ugly[i]):
            i3 += 1
            nextMultipleOf3 = ugly[i3] * 3
        if (nextMultipleOf5 == ugly[i]):
            i5 += 1
            nextMultipleOf5 = ugly[i5] * 5    
    return ugly[n - 1]
    
   
  
n = int(input("Enter n: "))
print(nthUglyNumber(n)) 
