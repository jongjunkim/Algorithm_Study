def solution(targets):
    answer = 0
    bound = 0
    
    
    for s, e in sorted(targets):
        if bound > s:
            bound = min(bound, e)
        elif bound <= s:
            bound = e
            answer += 1

    return answer

#need to solve one more