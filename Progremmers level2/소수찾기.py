from itertools import permutations

def solution(numbers):
    
    visited = set()
    res = 0
    for i in range(1,len(numbers)+1):
        for permu in permutations(numbers, i):
            
            num = '.'.join(permu).replace(".", "")
            if num[0] == "0" or num in visited:
                continue
            visited.add(num)
            
            if is_prime(int(num)):
                res += 1
            
    return res
            
def is_prime(num):
    
    if num == 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# for i in range(2, int(num**0.5) + 1): 이부분 기억하기
