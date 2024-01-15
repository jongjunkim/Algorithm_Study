def solution(wallpaper):
    row, column = len(wallpaper), len(wallpaper[0])
    minx, miny, maxx, maxy = row, column, 0, 0
    
    for i in range(row):
        for j in range(column):
            if wallpaper[i][j] == "#":
                minx = min(minx, i)
                miny = min(miny, j)
                maxx = max(maxx, i + 1)
                maxy = max(maxy, j + 1)
        
    return [minx, miny, maxx, maxy]



#got 100 out of 100

".#..."
"..#.." 
"...#."