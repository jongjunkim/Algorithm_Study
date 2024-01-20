from collections import deque

def solution(places):
    
    res = []
    for place in places:
        if bfs(place):
            res.append(1)
        else:
            res.append(0)
    return res
            


def bfs(place):
    
    direction = [[0,1], [0,-1], [1,0], [-1,0]]
    
    q = deque()
    visited = set()
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P" and (i,j) not in visited:
                q.append((i,j,0))
                
                while q:
                    curx, cury, distance = q.popleft()
                    visited.add((curx,cury))
                    print(curx,cury)
                    for x,y in direction:
                        dx, dy = curx + x, cury + y

                        if dx >= 0 and dy >= 0 and dx < 5 and dy < 5 and (dx,dy) not in visited:            
                            if place[dx][dy] == "O":
                                q.append((dx,dy, distance + 1))
                            if place[dx][dy] == "P" and distance <= 1:
                                return False
    return True          
                        
                    
                    
                
                
                
            
#abs(r1-r2) + abs(c1-c2) <= 2
# 파티션이 존재하면 괜찬
# 만약 같은 거리에 빈 테이블이 잇으면 안됨
