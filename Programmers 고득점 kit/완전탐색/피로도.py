from itertools import permutations

def solution(k, dungeons):
    
    
    lst = list(permutations(dungeons, len(dungeons)))
    temp = k
    ans = 0 
    for i in range(len(lst)):
        temp = k
        count = 0
        for require, spend in lst[i]:
            if require <= temp:
                count += 1
                temp -= spend
        ans = max(ans,count)
    
    return ans
    
