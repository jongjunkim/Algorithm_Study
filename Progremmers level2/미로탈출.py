from collections import deque

def bfs(maps, start, goal):
    rows, cols = len(maps), len(maps[0])
    visited = set()
    queue = deque([(start, 0)])  # (position, distance)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left

    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == goal:
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and maps[nx][ny] != 'X':
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))

    return -1  # Goal is unreachable

def solution(maps):
    start = lever = exit = None
    for i, row in enumerate(maps):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'L':
                lever = (i, j)
            elif cell == 'E':
                exit = (i, j)

    # Find shortest path from start to lever and from lever to exit
    start_to_lever = bfs(maps, start, lever)
    lever_to_exit = bfs(maps, lever, exit)

    if start_to_lever == -1 or lever_to_exit == -1:
        return -1
    else:
        return start_to_lever + lever_to_exit


# while queue:
#         (x, y), dist = queue.popleft()
#          visited.add((x, y)) 이렇게 visited했을경우 더 느리다
#         if (x, y) == goal:
#             return dist
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and maps[nx][ny] != 'X':           
#                 queue.append(((nx, ny), dist + 1))

