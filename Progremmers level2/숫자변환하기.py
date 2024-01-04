from collections import deque

def solution(x, y, n):
    
    
    q = deque([(x,0)])
    visited = set()
    
    
    while q:
        
        num, count = q.popleft()
        if num == y:
            return count
        if num * 2 <= y and num * 2 not in visited:
            q.append((num * 2, count+1))
            visited.add(num*2)
        if num * 3 <= y and num * 3 not in visited:
            q.append((num * 3, count+1))
            visited.add(num*3)
        if num + n <= y and num + n not in visited:
            q.append((num + n, count+1))
            visited.add(num+n)
            
    return -1

#그냥 BFS로 했을경우 시간초과가 뜨지만 set()이용해서 이미 계산한 경우를 BFS queue에 포함시키지 않아야함
