def solution(n, m, section):
    
    count = 0
    section = set(section)
    
    i = n
    
    while i >= 1:
        if i in section:
            count += 1
            i = i - m
        else:
            i -= 1
        
        
    return count

#got 100 out of 100