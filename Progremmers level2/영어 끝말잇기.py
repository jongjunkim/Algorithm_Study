import math

def solution(n, words):
  
    done = []
    for i, word in enumerate(words):
        if done and done[-1][-1] != word[0] or word in done:
            person = (i+1) % n
            if person == 0:
                person = n 
            return [person, math.ceil((i+1)/n)]
        elif word not in done:
            done.append(word)

    return [0,0]

#좀더 간결하게

import math

def solution(n, words):
  
    done = []
    for i, word in enumerate(words):
        if done and done[-1][-1] != word[0] or word in done:
            return [i%n + 1, math.ceil((i+1)/n)]
        elif word not in done:
            done.append(word)

    return [0,0]
