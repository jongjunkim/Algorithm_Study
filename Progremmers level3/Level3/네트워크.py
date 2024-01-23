def solution(n, computers):
    
    
    map = {i:[] for i in range(1,n+1)}
    
    for i, computer in enumerate(computers):
        for idx, com in enumerate(computer):
            if com == 1:
                map[i+1].append(idx+1)
            
    visited = set()
    answer = 0
    def dfs(node):
        
        if node in visited:
            return
        
        visited.add(node)
        
        for i in map[node]:
            if i == node and i not in visited:
                continue
            dfs(i)
   
    for i in map:
        if i not in visited:
            answer+=1
            dfs(i)
    return answer
