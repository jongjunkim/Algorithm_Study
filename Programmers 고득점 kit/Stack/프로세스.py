def solution(priorities, location):
    
    curmax = max(priorities)
    current = 0
    process = 1
    while True:
        
        if priorities[current] == curmax:
            if current == location:
                return process
            priorities[current] = 0
            print(priorities)
            process += 1
            curmax = max(priorities)
            
        current += 1
        if current >= len(priorities):
            current = 0
    
    
        
