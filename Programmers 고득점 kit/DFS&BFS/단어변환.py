from collections import Counter, deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    
    result = []
    while q:
        
        word, count = q.popleft()
        
        if word == target:
            return count
        
        for w in words:
            if len(Counter(word) - Counter(w)) == 1:
                q.append((w,count+1))
    
#맨처음 BFS사용하지 않고 while True 문으로 word와 target이 맞을 때가지 돌렸으나 시간초과 그래서 BFS가 가장 최소한의 방법을 찾을수있는데 효과적이라는것을 꺠닯음 
#hit->hot->dot->dog->log->cog
#hit->hot->lot->log->cog
