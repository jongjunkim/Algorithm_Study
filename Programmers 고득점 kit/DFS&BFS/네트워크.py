def solution(n, computers):
    
    visited = set()
        
    def dfs(computer_num):
        
        if computer_num in visited:
            return
        
        visited.add(computer_num)
        for i, computer in enumerate(computers[computer_num]):
            if i == computer_num:
                continue
            if computer == 1:
                dfs(i)
    res = 0
    for i, computer in enumerate(computers):
        if i not in visited:
            res += 1
            dfs(i)
    
    return res

#기본적인 dfs
