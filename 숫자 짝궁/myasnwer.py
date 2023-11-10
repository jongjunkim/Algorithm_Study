from collections import Counter

def solution(X, Y):
    
    counterx = Counter(X)
    countery = Counter(Y)
    
    hashmap = {}
    
    for x in counterx.keys():
        for y in countery.keys():
            if x == y:
                hashmap[x] = min(counterx[x], countery[y])
    
    another = sorted(hashmap.keys(), reverse = True) #key point reverse = True
    sorted_keys = {}
    
    for key in another:
        sorted_keys[key] = hashmap[key]
        
    res = ""
    for key,value in sorted_keys.items():
        for i in range(value):
            res += key
    
    if res and res[0] == "0":
        res = "0"

    
    return res if res else "-1"