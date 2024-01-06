import math

def solution(arr):
    
    
    maxi = max(arr)
    total = math.prod(arr)
    
    for i in range(max(arr), multi+1):
        for num in arr:
            if i % num != 0:
                break;
        else:
            return i
# 최소공배수 최대공약수는 이미 직관적인 코드가 있을거라고 생각해서 그냥 보고했음
# 최대공약수
for i in range(min(A,B), 0, -1):
	if A % i == 0 and B % i == 0:
    	print(i)
        break
                
         
    
            
    
    
