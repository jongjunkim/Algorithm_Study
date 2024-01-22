from collections import defaultdict


def solution(weights):
    answer = 0
    info = defaultdict(int)
    
    
    for w in weights:
        
        if w % 2 == 0:
            answer += info[w//2]
        if w % 3 == 0:
            answer += info[w//3 * 2] + info[w//3 * 4]
        if w % 4 == 0:
            answer += info[w//4 * 2] + info[w//4 * 3]
        info[w] += 1
    print(info)
        
    return answer

#defaultdict(int)를 했을때 info[w//2] + info[w//3 * 2] + info[w//3 * 4] 했을경우 그 값에 대해서 알아서 dictionary가 생긴다
# 예를들어 180이 있을때 info[w//2] + info [w//2 * 3] 했을경우 dictionary에 90: 0 270:0 이런식으로 key값들이 생기고 추후에
# 270이라는 숫자가 들어왔을경우 info[w] +=1 에 들어가므로 answer + 1이 값이 된다
