def solution(n):
    
    
    res = ""
    while n != 0:
        
        if n % 3 == 0:
            n = n - 3
            n = n//3
            res = str(4) + res
        else:
            n, quo = n // 3, n % 3
            res = str(quo) + res
        
    
    return res

# res += str(4) 해서 나중에 다시 for loop로 자리수를 되돌리는게 아니라 처음부터 res = str(4) + res를 해서 자리수를 유지할수있음
