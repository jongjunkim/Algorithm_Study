import heapq
def solution(n, costs):
    
    costs.sort()
    
    vertex = {i:[] for i in range(n)}
    
    INF = float('inf')
    
    for x,y,c in costs:
        vertex[x].append((y,c))
        vertex[y].append((x,c))
    
    mst_node = [-1 for _ in range(n)]
    visited = [True for _ in range(n)]
    
    q = [(0,0,0)]
    while q:
        cost, start, end = heapq.heappop(q)
        if visited[start] is False:
            continue
        visited[start] = False    
        mst_node[start] = cost
        
        for dst, weight in vertex[start]:
            if visited[dst] == True:
                heapq.heappush(q, (weight, dst, start))
                print(weight, dst, start)
     

    return sum(mst_node)

#프림스 알고리즘 이용 weight를 heappush하면서 가장 낮은 weight를 일단은 pop하고 만약 그게 이미 visited에 있다면 continue 아니라면 visited에 넣고  most_node에 추가
