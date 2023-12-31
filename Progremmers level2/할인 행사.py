from collections import Counter

def solution(want, number, discount):
    
    total = len(discount)
    
    hashmap = {}
    for i in range(len(want)):
        hashmap[want[i]] = number[i]
        
    
    count = 0
    for i in range(total-10+1):
        if hashmap == Counter(discount[i:i+10]):
            count += 1

    return count

# 10일 회원자격
# 매일 한가지 제품할인 한개만 구매가능
