def solution(arr):
    
    stack = [arr[0]]
    
    for element in arr:
        if element != stack[-1]:
            stack.append(element)
        
    return stack

https://school.programmers.co.kr/learn/courses/30/lessons/12906
