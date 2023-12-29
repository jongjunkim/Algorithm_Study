def solution(k, tangerine):
    
    tangerine.sort()
    hashmap = {}
    
    for t in tangerine:
        hashmap[t] = hashmap.get(t,0) + 1

    hashmap = sorted(hashmap.items(), key = lambda x: x[1], reverse = True)
    
    count = 0
    for i, (x, y) in enumerate(hashmap):
        count += y
        if count >= k:
            return i + 1
    
