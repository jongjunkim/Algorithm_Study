def solution(number, k):
    
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
        
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

#리스트에서 큰수를 찾으려며 stack을 사용해서 찾아보기
# 역시나 combinatio을 이용해서풀면 시간초과
