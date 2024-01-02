def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break
    return answer

# 일단 내 코드는 깔끔하지 못한 부분이 있고 더군다나 마지막 문자열이 들어올때 잘못된 알고리즘에 의해 다른 값들이 계속 들어왔다. 
# 이것처럼 하는게 제일 깔끔
