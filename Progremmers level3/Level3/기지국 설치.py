import math
def solution(n, stations, w):
    
    cover = w * 2 + 1
    
    now = 1
    ans = 0
    for s in stations:
        prior, next = s - w, s + w
        if prior < 1:
            prior = 1
        if next > n:
            next = n
        ans += math.ceil((prior-now) / cover)
        now = next + 1
    
    if now <= n:
        ans += math.ceil((n-now+1) / cover)
        
    return ans

