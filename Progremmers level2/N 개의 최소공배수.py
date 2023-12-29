import math

def solution(arr):
    
    
    maxi = max(arr)
    total = math.prod(arr)
    
    for i in range(maxi, total+1):
        count = 0
        for j in arr:
            if i % j == 0:
                count += 1
        if count == len(arr):
            return i
# 최소공배수 최대공약수는 이미 직관적인 코드가 있을거라고 생각해서 그냥 보고했음
# 최대공약수
for i in range(min(A,B), 0, -1):
	if A % i == 0 and B % i == 0:
    	print(i)
        break
                
         
    
            
    
    
