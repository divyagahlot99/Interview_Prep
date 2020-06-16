def calc(n, arr):
    dp=[0]*n
    res=0
    for i in range(n):
        dp[i]=1
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i], dp[j]+1)
    return dp[n-1]

n = int(input())
arr = list(map(int, input().split()))
print(calc(n, arr))
