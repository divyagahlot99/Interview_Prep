#This is the code for Matrix chain Multiplication
#MCM Problem is optimisation problem and helps us to find most efficient way of Multiplying 2 matrices
#Input format:Array of integers 

#defining the loockup table
def mcm(arr,i,j,t):

    
    #Base condition:One matrix
    if(i>=j):
        return 0

    min1 = float('inf')    
    
    #if subproblem not in lookup table and seen for first time
    if(t[i][j]!=-1):
        return t[i][j]
    else:    
        for k in range(i,j-1):
            tempans=mcm(arr,i,k,t)+mcm(arr,k+1,j,t)+arr[i-1]*arr[k]*arr[j]
            print(tempans)

            if(tempans<min1):
                min1=tempans

        t[i][j]=min1
    
    return t[i][j]

arr=[2,3,3,4,4,2]
t = [[-1 for i in range(len(arr))] for i in range(len(arr))]

i=1
j=len(arr)-1
print(mcm(arr,i,j,t))


