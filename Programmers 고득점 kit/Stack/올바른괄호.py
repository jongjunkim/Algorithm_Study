def solution(s):
    stack = []
    
    if s[0] == ')':
        return False
    
   
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        elif stack and stack[-1] == '(':
            stack.pop()
    
    return not stack

https://school.programmers.co.kr/learn/courses/30/lessons/12909
