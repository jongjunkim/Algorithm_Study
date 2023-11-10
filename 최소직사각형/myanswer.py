def solution(sizes):
    
    w, h = 0, 0
    for size in sizes:
        
        if size[0] < size[1]:
            h = max(h, size[1])
            w = max(w, size[0])
        else:
            h = max(h, size[0])
            w = max(w, size[1])
    
    return h*w
       
    
# got 100 out of 100

#    80
# -------
# |
# |       70
# |