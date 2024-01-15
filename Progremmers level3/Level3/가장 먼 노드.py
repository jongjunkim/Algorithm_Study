from collections import deque

def solution(n, edge):
    
    vertex = {i:[] for i in range(1,n+1)}
    
    for node in edge:
        x, y = node
        vertex[x].append(y)
        vertex[y].append(x)
    
    INF = float("inf")
    distance = [INF] * (n+1)
    distance[0] = 1
    distance[1] = 0
    q = deque([1])
    
    while q:
        
        node = q.popleft()
        
        for i in vertex[node]:
            if distance[i] == INF:
                distance[i] = distance[node] + 1
                q.append(i)
    
    ans = max(distance)
    res = 0
    for d in distance:
        if ans == d:
            res += 1
        
    return res
# 다익스트라 알고리즘인데 여기서 맨처음 모든 노드들을 인피니티로 set한다음 그다음 distance들을 찾아준다
