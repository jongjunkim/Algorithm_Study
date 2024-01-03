def solution(dirs):
     
    map = set()
                # u   d   r   l
    direction = {"U":[0,1], "D":[0,-1], "R":[1,0], "L":[-1,0]}
    
    curx, cury = 0, 0
    count = 0
    
    for dir in dirs:
        x,y = direction[dir]
        if curx + x > 5 or curx + x < -5 or cury + y > 5 or cury + y < -5: 
            continue
        
        if (curx, cury, curx + x, cury + y) not in map and (curx + x, cury + y, curx, cury) not in map:
            map.add((curx, cury, curx + x, cury + y))
        
        curx = curx + x
        cury = cury + y
    
    return len(map)
#맨처음 set에 지나가는 좌표만 넣었는데 그렇게 되면 로직상 지나가는 길의 개수를 절대로 올바르게 구할수 없다.
#따라서 길이를 구하기위해 출발한 좌표와 도착한 좌표를 두개다 넣어야하고 set에 넣을때 양뱡향 즉 한지점에서 오른쪽으로 간것과  한지점에서 왼쪽으로 간 부분은 이미 지나간 부분이므로
# if 문에 두개의 경우가 없을때 set에 add
