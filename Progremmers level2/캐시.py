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
        elif city not in cache and len(cache) < cacheSize:
            db += 5
        else:
            db += 5
            cache.popleft()
        cache.append(city)        
    
    return db

    
