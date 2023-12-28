def solution(n):
    
    a = list(str(bin(n)[2:]))
    length = a.count("1")
    num = n
    while True:
        num += 1
        
        b = str(bin(num)[2:])
        if length == b.count("1"):
            return num
    
