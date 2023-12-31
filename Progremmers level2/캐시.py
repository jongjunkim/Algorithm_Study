from collections import deque

def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    cache = deque()
    db = 0
    
    for i,city in enumerate(cities):
        
        city = city.lower()
        
        if cache and city in cache:
            db += 1
            cache.remove(city)
            cache.append(city)
            continue
        elif city not in cache and len(cache) < cacheSize:
            db += 5
            cache.append(city)
        elif city not in cache and len(cache) >= cacheSize:
            db += 5
            cache.popleft()
            cache.append(city)
    
    return db
#LRU 정의를 보면 cache hit를 하면 그대로 캐시를 두는게 아니라 최근에 사용됬으므로 cache맨 뒤에 넣어주는게 맞다. 그래서 city가 cache에 있으면 그 해당 city를 삭제한후 맨 뒤에 넣어줌
