# This is similar to 0/1 Knapsack
#  For eg. set1=[1,2,3,4] sum1=5  output:True     

def subsetSum(set1,sum1,n):
    
    #Initialise the dp matrix 
    t=[[False for i in range(sum1+1)] for j in range(n+1)]
    for i in range(n+1):
        t[i][0]=True

    for i in range(1,n+1):
        for j in range(1,sum1+1):
            # If the array element is less than reqd sum then we have a choice to either take it or not
            if(set1[i-1]<=j):
                t[i][j]=t[i-1][j-set1[i-1]] or t[i-1][j]    
            #Here we dont take the value asvalue isgreater than sum
            else:

                t[i][j]=t[i-1][j]
    return t[-1][-1]  
              
print(subsetSum([2,3,5,6,8,10],10,6))   