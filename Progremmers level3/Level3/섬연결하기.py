import heapq

def solution(n, costs):
    
    limit = n
    graph = {i:[] for i in range(n)}
    distance = {i:float("inf") for i in range(n)}
    for x,y,w in costs:
        graph[x].append((w,y))
        graph[y].append((w,x))
        
    visited = set()
    print(graph)
    q = [(0,0)]
    
    ans = 0
    while q:
        weight, node = heapq.heappop(q)
        
        if node in visited:
            continue
    
        visited.add(node)
        ans += weight
        
        if len(visited) == limit:
            return ans
        
        for w,n in graph[node]:
            if n not in visited:
                heapq.heappush(q, (w,n))
        
# visited.add() 하고 ans+= weight를 해야 if len(visited) == limit return ans
