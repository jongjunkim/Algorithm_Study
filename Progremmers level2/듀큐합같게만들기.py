from collections import deque

def solution(queue1, queue2):
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    visited = []
    q1_sum, q2_sum = sum(q1), sum(q2)
    
    if (q1_sum + q2_sum) % 2 != 0:
        return -1
    
    goal = (q1_sum + q2_sum) // 2
    limit = len(q1) + len(q2)

    count = 0
    while q1_sum != q2_sum:
        
        if count > limit:
            return -1
        
        while q2 and q1_sum < q2_sum:
            num = q2.popleft()
            q2_sum -= num
            q1.append(num)
            q1_sum += num
            count += 1
        while q1 and q1_sum > q2_sum:
            num = q1.popleft()
            q1_sum -= num
            q2.append(num)
            q2_sum += num
            count += 1
 
    return count

# 맨처음 while q2 and q1_sum < q2_sum -> if  q1_sum < q2_sum 이라고 하니 시간이 더 오래 걸리고 시간초과가 뜬다
# if count > limit: return -1 경우도 if not q1 or not q2라고 하니까 시간초과가 뜬다.


from collections import deque

def solution(queue1, queue2):
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    if (sum(q1) + sum(q2)) % 2 != 0:
        return -1
    
    target = (sum(q1) + sum(q2)) // 2
    ans = 0
    q1_sum = sum(q1)
    while q1 and q2 and q1_sum != target:
        
        if q1_sum < target:
            num = q2.popleft()
            q1.append(num)
            q1_sum += num
        elif q1_sum > target:
            num = q1.popleft()
            q1_sum -= num
        
        ans+=1
    
    return ans if q1 and q2 else -1
        
