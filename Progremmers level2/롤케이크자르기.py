from collections import Counter

def solution(topping):
    answer = 0
    dic = Counter(topping)
    set_dic = set()
    answer = 0

    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1
    
    return answer

# 둘다 set을 이용하거나 counter를 이용하면 시간초과가 난다.
# 한개를 set을 넣고 한개를 Counter를 이용해서 Counter dictionary에서 하나씩 set에 넣어주고 둘이 길이가 같은경우 +1
