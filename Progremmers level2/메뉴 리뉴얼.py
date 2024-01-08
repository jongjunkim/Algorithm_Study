from itertools import combinations

def solution(orders, course):
    
    hashmap = {}
    
    
    for order in orders:
        for c in course:
            for comb in combinations(order, c):
                comb = ''.join(sorted(comb))
                hashmap[comb] = 1 + hashmap.get(comb, 0)
                
    
    hashmap = sorted(hashmap.items(), key = lambda x:(len(x[0]),x[1]), reverse = True)
    
    res = []
    
    curmax = 0
    previous = course[-1]
    for key, value in hashmap:
        if previous != len(key):
            previous = len(key)
            curmax = 0
        if len(key) in course and value > 1 and curmax <= value:
            curmax = value
            res.append(key)
    
    res = sorted(res, key = lambda x:x.lower())
    return res

#알파멧 순으로 정렬 x.lower()
