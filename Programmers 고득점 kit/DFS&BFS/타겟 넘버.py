def solution(numbers, target):    
    res = 0
    def dfs(i, current_sum):
        nonlocal res
        
        if  i == len(numbers):   
            if current_sum == target:
                res += 1
            return 
        
        dfs(i + 1, current_sum + numbers[i])
        dfs(i + 1, current_sum - numbers[i])
        
    dfs(0, 0)
    
    return res
    
# 맨처음    if  i == len(numbers):  이 부분을    if  i >= len(numbers):   이렇게 해서 틀린 답이 나왔다
