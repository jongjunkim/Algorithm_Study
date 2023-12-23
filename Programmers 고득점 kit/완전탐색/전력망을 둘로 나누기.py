def dfs(v, graph, visited):
    visited[v] = True
    component_size = 1  # Count the current vertex

    for u in graph[v]:
        if not visited[u]:
            component_size += dfs(u, graph, visited) 

    return component_size


def solution(n, wires):
    graph = [[] for _ in range(n+1)]

    for v, u in wires:
        graph[v].append(u)
        graph[u].append(v)
    
    answer = 100
    for i in range(n-1):
        visited = [False for _ in range(n+1)]
        v1, v2 = wires[i]
        visited[v2] = True #temporily disconnect v1 and v2
        tmp = abs(dfs(v1, graph, visited) - dfs(v2, graph, visited))
        print(tmp)
        answer = min(tmp, answer)

    return answer

#graph = {i:[] for i in range(1, n+1)}
#    print(graph)
#{1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
#그래서 graph = {i:[] for i in range(n)}
#이렇게 하면 0부터 시작하므로 key error가 나온거임
