n=3
c=[8,3,2,1]

dp=[[1]*(len(c)+1)]
for i in range(n):
    dp.append([0]*(len(c)+1))
for i in range(1,n+1):
    for j in range(1,len(c)+1):
        if c[j-1]<=i:
            dp[i][j]=dp[i-c[j-1]][j]+dp[i][j-1]
        else:
            dp[i][j]=dp[i][j-1]
print(dp[-1][-1])