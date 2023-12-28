def solution(s):
    
    zero,count = 0, 0
    while s != "1":
        temp = ""
        count+=1
        for char in s:
            if char == "1":
                temp += char
            else:
                zero += 1
        s = str(bin(len(temp))[2:])
      
    
    return [count,zero]


#4 2 1
#1 1 0 
