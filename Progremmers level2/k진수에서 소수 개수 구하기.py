import math
def solution(n, k):
    
    converted = change(n,k)
    s = converted.split('0')
    count = 0
    for num in s:
        if num == '' or num == "1":
            continue
        if is_prime(int(num)):
            count += 1
    
    return count

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1): 
        if num % i == 0:
            return False
    
    return True
    
def change(n, q):
    rev_base = ''

    while n > 0:
        n, mod = n//q, n % q
        rev_base += str(mod)

    return rev_base[::-1] 

# 소수점 구하는것과 진법을 바꾸는거 배움
