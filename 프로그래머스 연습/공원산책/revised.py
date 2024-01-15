

def solution(park, routes):
    
    row, column = len(routes), len(routes[0]) 
    
    #find start point
    curx, cury = 0, 0
    for i in range(row):
        for j in range(column):
            if park[i][j] =="S":
                curx, cury = j, i
                continue
    
    def check(x, y):
        if (0 > x or x >= len(park[0])) or (0 > y or y >= len(park)) or park[y][x] == 'X':
            return False
        return True
        
    
    for route in routes:
        dir, move = route[0], int(route[2])
        
        if dir == "E":
            nx = curx + move
            for i in range(curx, nx+1):
                if check(i, cury) == False: 
                    break
            else:
                 curx =nx 
                    
        elif dir == "W":
            nx = curx - move
            for i in range(nx, curx+1):
                if check(i, cury) == False: 
                    break
            else:
                curx = nx
            
        elif dir == "N":
            ny = cury - move
            for i in range(ny, cury+1):
                if check(curx, i) == False: 
                    break
            else:
                cury = ny 
        elif dir == "S":
            ny = cury + move
            for i in range(cury, ny+1):
                if check(curx, i) == False: 
                    break
            else:
                cury = ny 
                
    return [cury, curx]