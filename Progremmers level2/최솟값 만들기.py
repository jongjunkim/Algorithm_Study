def solution(A,B):
    
    A.sort()
    B = sorted(B, reverse = True)

    ans = 0
    for x,y in zip(A,B):
        ans += x*y
      
    return ans
#그냥 sort 해주면됨
