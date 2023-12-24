
#이렇게 하는게 애초에 맞지가 않음 한 dfs를 하나의 가는 길로 생각해서 처리를 했어야했고 그리고 res = min(res,temp) 이거 또한 전혀 맞지가 않는다. 계속 min값이 아니라 결국에는 map에 있는 모든 1값들을 count한거를 보냄
 def solution(maps):
    
    row, col = len(maps), len(maps[0])
    res = float("inf")
    visitied = set()
    
    if maps[row-2][col-1] == 0 and maps[row-1][col-2] == 0:
        return -1
 
    def dfs(i,j,temp):
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
    
    return result if result != float("inf") else -1

