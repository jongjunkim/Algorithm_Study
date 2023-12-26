def solution(gems):
    kind = len(set(gems))

    answer = [0, 0]
    length = float('inf')
    L = 0
    gem_count = {}

    for R in range(len(gems)):
        gem_count[gems[R]] = gem_count.get(gems[R], 0) + 1

        while gem_count[gems[L]] > 1:
            gem_count[gems[L]] -= 1
            L += 1

        if len(gem_count) == kind and length > (R - L):
            length = R - L
            answer[0] = L + 1
            answer[1] = R + 1

    return answer

#접근법은 비슷했지만 최소값을 구하기 위해서 해둔 장치는 안했다.
#밑에가 내 원래 코드
def solution(gems):
    
    ans = set(gems)
    res = set()
    temp = []
   
    l = 0
    for r in range(len(gems)):
        if gems[r] in res and gems[l] == gems[r]:
            res.remove(gems[l])
            temp.remove(gems[l])
            l += 1
        
        res.add(gems[r])
        temp.append(gems[r])
        if res == ans:
            break

    count = 0
    while len(temp) > 1 and temp[0] == temp[1]:
        a = temp.pop(0)
        count+=1
        
        
    return [l+1+count,r+1]
    
