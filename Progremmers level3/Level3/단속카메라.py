def solution(routes):
    
    
    routes = sorted(routes, key = lambda x:x[0])
    
    interval = routes[0]
    res = []
    for i in range(1, len(routes)):
        start, end = interval
        
        if end >= routes[i][0]:
            interval = (min(start, routes[i][0]), min(end,routes[i][1]))
        else:
            res.append(interval)
            interval = routes[i]

        
    return len(res) + 1
