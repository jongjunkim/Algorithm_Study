import heapq

def solution(N, road, K):
    graph = {i: [] for i in range(1, N + 1)}

    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))

    distances = {i: float('inf') for i in range(1, N + 1)}
    distances[1] = 0

    heap = [(0, 1)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    count = 0
    for distance in distances.values():
        if distance <= K:
            count += 1

    return count

#맨처음 heapq가 아니라 deque로 하고 visited set을 이용해서만했음 하지만 heapq를 이용해야하구 마지막에 distance value를 이용
