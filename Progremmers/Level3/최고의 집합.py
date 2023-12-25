def solution(n, s):
    answer = []
    if s // n <= 0: return [-1]
    answer = [s // n for _ in range(n)]
    
 
    if s % n == 0:
        return sorted(answer)
    
    for i in range(s % n):
        print(i)
        answer[i] += 1
        
    return sorted(answer)

#맨처음 heap을 이용해서 heappush와 heappop을 하면서 가장 큰값을 2로 나눈뒤 나눈값들을 heap에 계속 넣는 방식이였지만 틀림
