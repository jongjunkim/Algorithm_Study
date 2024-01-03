def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for ind, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(ind)
     
    return answer
  # 처음에 brute force 방법을 이용해서 접근해보려했으나 역시나 시간초과
  # stack을 이용해서 가장 가까이에 있는 숫자를 구했음 이건좀 신박함
