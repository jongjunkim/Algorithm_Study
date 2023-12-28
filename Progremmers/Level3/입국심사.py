#deque, heapq?

def solution(n, times):
    
    fastest = min(times)
    
    maximum = fastest * n #확실히 최단 기간에 끝낼수 있게 보장되는 시간
    minimum = fastest
    answer = 0
    count = 0
    while minimum <= maximum:
        done = 0
        time = (maximum + minimum) // 2
        
        for t in times:
            done += (time // t) 
            
        if done < n:
            minimum = time
        elif done >= n:
            maximum = time
        
        if minimum == maximum-1:
            answer = maximum
            break
        
      
    return answer

#이분탐색을 하는데 처음 보는 유형
    
