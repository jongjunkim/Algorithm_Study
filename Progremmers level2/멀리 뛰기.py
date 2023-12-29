def solution(n):
    
    dp = [1] * (n+1)
    
    for i in range(n-2, -1 ,-1):
        dp[i] = dp[i+1] + dp[i+2]

        
    return dp[0] % 1234567

# 제일 기초적인 dp문제
