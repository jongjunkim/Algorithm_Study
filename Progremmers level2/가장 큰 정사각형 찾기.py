def solution(board):
    
    res = board[0][0]
    row, col = len(board), len(board[0])
    
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] > 0:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    
    
    for i in range(row):
        res = max(res, max(board[i])) 
        
    return res ** 2


# 정사각형을 어떻게 찾는거에 대해 집중. 결국은 혼자 해결하지 못함
# Dynamic prgoramming 이용 근접한 board에서 가장 작은 값에서 1을 해주면 그게 현재 위치에서 정사각형을 만들수있는 최대 변
