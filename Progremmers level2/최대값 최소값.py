def solution(s):
    
    num = list(map(int, s.split()))
    
    mini = min(num)
    maxi = max(num)
    
    return f"{mini} {maxi}"
