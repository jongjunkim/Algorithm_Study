def solution(participant, completion):
    complete = {}

    for person in participant:
        complete[person] = 1 + complete.get(person, 0)

    for person in completion:
        complete[person] -= 1

    for person, count in complete.items():
        if count > 0:
            return person


#Note
from collections import Counter

def solution(participant, completion):
    
    x1 = Counter(participant)
    x2 = Counter(completion)
    
    result = x1 - x2
    return list(result.keys())[0]
