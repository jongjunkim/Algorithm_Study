import math

def solution(n,a,b):
    
    count = 0
    
    while abs(a-b) != 0:
         
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        count+=1
        
    return count


# 맨처음 abs(a-b) 가 아니라  a + 1 != b 라는 조건을 하였는데 a가 항상 b보다 작을리는 없는 경우도 있기 때문에 계속 시간초과 오류가 뜸
# 그리고 abs(a-b) != 1 이라는 조건을 했을때 어떤 경우는 abs(a-b)가 1 이 아닌 경우가 잇기 때문에 그냥 계속 둘이 비슷해질때까지 나누기 2를 해주면됨
