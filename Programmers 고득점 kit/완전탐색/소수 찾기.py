from itertools import permutations

def solution(numbers):
    numbers = list(map(str, numbers))  # Convert to strings
    permutations_set = set()

    for i in range(1, len(numbers) + 1):
        permutations_set.update(permutations(numbers, i))

    answer = 0

    for perm in permutations_set:
        num_str = ''.join(perm)
        if num_str[0] == '0': #앞에 0이 있다는거는 다른 숫자가 이미 있다는거를 의미
            continue
        if is_prime(int(num_str)):
            answer += 1

    return answer

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
