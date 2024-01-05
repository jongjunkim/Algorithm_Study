def solution(order):
    
    stack = [] #보조벨트
    cur = 0 # 현재 순서
    for i in range(1, len(order)+1):
        
        stack.append(i)
        
        while stack and stack[-1] == order[cur]:
            stack.pop()
            cur += 1
            

    return cur
    
#보조 벨트 stack
