def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for x, y in puddles: #웅덩이가 [m,n] 형태로 주어졌기 때문에 y와 x 위치를 바꿔준다
        dp[y][x] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            
            dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % 1000000007

    return dp[n][m]
