N = int(input())

lst = [int(input()) for _ in range(N)]
maxi = max(lst)

dp = [0] * (maxi+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for num in lst:
    for i in range(4,num+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    print(dp[num])

