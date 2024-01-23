from collections import deque

def solution(board):
    
    direction = [[0,1], [0,-1], [1,0], [-1,0]]
    row, col = len(board), len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] == "G":
                goal = (i,j)
            if board[i][j] == "R":
                start = (i,j)
    
    count = 0
    for xd, yd in direction:
        curx, cury = xd + goal[0], yd + goal[1]
        if board[curx][cury] == ".":
            count += 1
    if count == 4:
        return -1
    
    q = deque([(start[0],start[1],0)])
   
    while q:
        
        curx,cury, distance = q.popleft()
        
        if (curx,cury) == goal:
            return distance
        
        #하단 이동
        tempx, tempy = curx, cury
        while tempx + 1 < row and board[tempx + 1][tempy] != "D":
            tempx += 1
        
        if curx != tempx:
            q.append((tempx, tempy, distance + 1))
            
        # Move Up
        tempx, tempy = curx, cury
        while tempx - 1 >= 0 and board[tempx - 1][tempy] != "D":
            tempx -= 1

        if curx != tempx:
            q.append((tempx, tempy, distance + 1))
        
        #우측
        tempx, tempy = curx, cury
        while tempy + 1 < col and board[tempx][tempy+1] != "D":
            tempy += 1
        
        if cury != tempy:
            q.append((tempx, tempy, distance + 1))
            
        # 좌측
        tempx, tempy = curx, cury
        while tempy - 1 >= 0 and board[tempx][tempy-1] != "D":
            tempy -= 1

        if cury != tempy:
            q.append((tempx, tempy, distance + 1))
            
# 어떻게하면 미끄러지는거를 구현할수있을까 고민한 끝에 이게 나왔지만 시간초과


def solution(board):
    que = []
    for x, row in enumerate(board):
        for y, each in enumerate(row):
            if board[x][y] == 'R':
                que.append((x, y, 0))
    visited = set()
    while que:
        x, y, length = que.pop(0)
        if (x, y) in visited:
            continue
        if board[x][y] == 'G':
            return length
        visited.add((x, y))
        for diff_x, diff_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            now_x, now_y = x, y
            while True:
                next_x, next_y = now_x + diff_x, now_y + diff_y
                if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]) and board[next_x][next_y] != 'D':
                    now_x, now_y = next_x, next_y
                    continue
                que.append((now_x, now_y, length + 1))
                break
    return -1

# While True문을 이용해서 만약 D나 board의 끝이 나왔을경우  append를 하고 break해서 미끄러지는 거 구현
