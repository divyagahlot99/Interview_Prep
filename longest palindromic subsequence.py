# Longest palindromic subsequence is similar to Longest common subsequence but instead the difference is the second substring is the reverse of first substring
# Example : agbcba and reverse of it abcbga have the lps abcba of length 5 which is lcs of string and its reverse 


#Function for longest common subsequence
#m and n are length of first and second string resp.
def lcs(a,b,m,n):
    #Initialise the DP Matrix 
    t=[[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            #This is base condition
            if(i==0 or j==0):
                t[i][j]=0

            #If the particular char is equal increase count by 1 and move to next element    
            elif(a[i-1]==b[j-1]):
                t[i][j]=t[i-1][j-1]+1
            
            # If the char isnt equal then shift 1 char in either A string or B depending upon which will give max count
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t[m][n] 

#Longest palindromic subsequence  Function where second string is basically reverse of first string
def  lps():
    print(lcs("agbcba","abcbga",6,6))

lps()
