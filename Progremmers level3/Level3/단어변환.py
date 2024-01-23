from collections import Counter, deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    
    q = deque([(begin, 0)])
    while q:
        word, change = q.popleft()
        if word == target:
            return change

        for w in words:
            diff = Counter(word) - Counter(w)
            if len(diff) == 1:
                q.append((w, change+1))

        
    
