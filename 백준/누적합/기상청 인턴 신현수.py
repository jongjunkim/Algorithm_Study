
def solution(n,k, measures):


    ans = float('-inf')
    for i in range(0, n-k+1):
        ans = max(ans, sum(measures[i:i+k]))
    
    return ans


res = solution(10, 2, [3, -2, -4, -9, 0, 3, 7, 13, 8, -3])
print("res:",res)

#맞음
