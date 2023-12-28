def solution(n):
    answer = 1
    
    
    # 어차피 숫자의 반이상인 경우는 연속된 수를 만족하기 어려움
    for i in range(1, n):
        
        total = 0
        
        while total <= n:
            
            total += i
            
            if total == n:
                answer += 1
                break 
            i+=1
    
    return answer
