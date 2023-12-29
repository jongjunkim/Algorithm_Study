def solution(n)  
    dp = [0] * (n//2 + 1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3,n//2+1):
        if i % 2 == 0:
            dp[i] = dp[i//2]
        else:
            dp[i] = dp[i-1] + 1
    
    return dp[n//2] if n % 2 == 0 else dp[n//2] + 1

#dynamic programming인줄 알았으나 오히려 효율성 테스트에서 떨어짐
#알고보면 더 쉬운거였음
def solution(n):

    count = 0
    
    while n >= 1:
        
        if n % 2 == 0:
            n = n/2
        else:
            n = n-1
            count+=1 
            
    return count
