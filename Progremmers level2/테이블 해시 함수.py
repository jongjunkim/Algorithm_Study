def solution(data, col, row_begin, row_end):
    
    data = sorted(data, key = lambda x: (x[col - 1], -x[0]))
    ans = 0
    for i in range(row_begin-1, row_end):
        total = 0
        for j in data[i]:
            total += j%(i+1)
        ans ^= total
  
    return ans
# xor 연산 ans ^= total
# col 값 첫번째 기준으로 내림차순 하기 위해서는 -x[0] 방법을 쓴다
