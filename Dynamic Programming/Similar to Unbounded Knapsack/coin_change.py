# Similar to unbounded knapsack which is itself similar to 0/1 Knapsack

def coinChange(coin,n,sum1):


    #Initialisation
    t=[[False for i in range(sum1+1)]for j in range(n+1)]

    # Base condition
    for i in range(n+1):
        t[i][0]=True
    
    for i in range(1,n+1):
        for j in range(1,sum1+1):

            #If coin is less than sum then we have a choice to take it and not take it
            #Notice that in 0/1 knapsack when we take its t[i-1][j-coin[i-1]] but here it isnt as we have unlimited coins
            if(coin[i-1]<=j):
                t[i][j]=t[i-1][j]+t[i][j-coin[i-1]]
            
            #Case when we do not take the coin as coin value>sum
            else:
                t[i][j]=t[i-1][j]

    return t[n][sum1]

print(coinChange([1,2,3],3,5))
