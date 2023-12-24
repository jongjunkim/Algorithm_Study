
#이렇게 하는게 애초에 맞지가 않음 한 dfs를 하나의 가는 길로 생각해서 처리를 했어야했고 그리고 res = min(res,temp) 이거 또한 전혀 맞지가 않는다. 계속 min값이 아니라 결국에는 map에 있는 모든 1값들을 count한거를 보냄
 def solution(maps):
    
    row, col = len(maps), len(maps[0])
    res = float("inf")
    visitied = set()
    
    if maps[row-2][col-1] == 0 and maps[row-1][col-2] == 0:
        return -1
 
    def dfs(i,j,temp)
        nonlocal res    
        if i == row-1 and j == col-1:
            res = min(res, temp)    
            return 
        if i < 0 or j < 0 or i >= row or j>= col or (i,j) in visitied or maps[i][j] != 1:
            return 
        
        visitied.add((i,j))        
        res +=1
        dfs(i+1, j, temp+1) 
        dfs(i, j+1, temp+1) 
        dfs(i-1, j, temp+1) 
        dfs(i, j-1, temp+1)
     
    dfs(0,0,0)
    return res
  
# DFS
#이렇게 했을 경우 답은 맞지만 효율성은 떨어짐
def solution(maps):
    
    row, col = len(maps), len(maps[0])
    res = float("inf")
    visitied = set()
     
    def dfs(i,j,temp):
        nonlocal visitied
        
        if i == row-1 and j == col-1:
            return temp
        
        if i < 0 or j < 0 or i >= row or j>= col or (i,j) in visitied or maps[i][j] != 1:
            return float("inf")
        
        visitied.add((i,j))
        
        one = dfs(i+1, j, temp+1) 
        two = dfs(i, j+1, temp+1) 
        three = dfs(i-1, j, temp+1) 
        four = dfs(i, j-1, temp+1)
        
        visitied.remove((i,j))
        
        return min(one, two, three, four)
    
    result = dfs(0,0,1)


 # BFS

#막혀있는 구간이 있기때문에 여기서 visited을 이용해서 (i,j)값들을 저장하지 않으면
#무한으로 q가 돌아간다.

#그리고 안에 count를 넣어서 지나왔던 칸의 개수들을 저장한다. (이건 꽤유용)
#deque에서 값들을 저장할때 맨처음 q= deque([ ])인데 set값을 넣으니까 q = deque([(0,0,1)]) 이렇게 되는거고
#q.append할때는 q.append((i,j,count+1)) 이렇게 ( ) 만을 이용해서 해준다
    
from collections import deque

def solution(maps):
    
    q = deque([(0,0,1)])
    row, col = len(maps), len(maps[0])
    visited = set()
    directions = [ [0,1], [1,0], [-1,0], [0,-1]]
    
    while q: 
        x,y,count = q.popleft()
        if x == row-1 and y == col-1:
            return count
        for dx,dy in directions:
            i = x + dx
            j = y + dy
            if i in range(row) and j in range(col) and maps[i][j] == 1 and (i,j) not in visited:
                q.append((i,j,count+1))
                visited.add((i,j))
        
    return -1

   
  

