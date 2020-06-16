def lcs(s1, s2):
    dp=[[0 for i in range(len(s2) + 5)] for j in range(len(s1) + 5)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if i==0 or j==0:
                dp[i][j] = 0
            if s1[i]==s2[j]:
                dp[i][j]=dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len(s1)-1][len(s2)-1]

print(lcs("apple", "coappjleu"))
