def solution(n, t, m, p):
    answer = "0"
    notation = "0123456789ABCDEF"

    for num in range(1, m * t):
        result = ""
        while num > 0:
            num, remainder = divmod(num, n)
            result += notation[remainder]

        answer += result[::-1]

    return answer[p-1::m][:t]

# 새로배운문법 answer[p-1::m] answer의 p-1 시작부터 끝가지 m간격으로 나눈 리스트
