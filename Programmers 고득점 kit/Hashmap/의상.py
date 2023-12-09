def solution(clothes):
    
    combination = {}

    for cloth, kind in clothes:
        combination[kind] = 1 + combination.get(kind, 0)
    res = 1
    for i in sorted(combination.values()):
        res *= (i+1)
     
    return res-1

#(빨강옷, 파랑옷) (빨강바지, 파랑바지)이 주어진다면 2*2= 4이다.
#그리고 여기서 옷을 압입는 수를 투명옷으로 입는다고 가정해보면
#(빨강옷, 파랑옷, 투명옷) (빨강바지, 파랑바지,투명바지) 3*3 = 9 이고 여기서 투명바지 투명옷을 입는 경우를 -1 하면된다

https://school.programmers.co.kr/learn/courses/30/lessons/42578
