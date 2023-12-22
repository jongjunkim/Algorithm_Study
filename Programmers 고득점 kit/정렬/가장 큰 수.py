def solution(numbers):
   
    numbers = map(str, numbers)
    sorted_numbers = sorted(numbers, key=lambda x: x * 3, reverse=True)
  
    answer = str(int(''.join(sorted_numbers)))
    return answer

