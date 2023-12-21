def solution(prices):
    
    list = [0] * len(prices)
    stack = [(0, prices[0])]
        
    for i in range(1,len(prices)):
        
        while stack and stack[-1][1] > prices[i]:
            index, price = stack.pop()
            list[index] = i - index 

        stack.append((i, prices[i]))
        
    while stack:
        index, _ = stack.pop()
        list[index] = len(prices) - index - 1
         
    return list
    

https://school.programmers.co.kr/learn/courses/30/lessons/42584
