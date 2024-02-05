N = int(input())

lst = list(map(int, input().split()))

dp = [0] * (N)
dp[0] = lst[0]

for i in range(1,len(lst)):
    for j in range(i):
        maxi = lst[i]
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + lst[i])
        else:
            dp[i] = max(dp[i], lst[i])
print(max(dp))
