from collections import Counter
from itertools import permutations

def is_same(user, ban):
    
    if len(ban) != len(user):
        return False
    
    for i in range(len(user)):
        if ban[i] == '*':
            continue
        else:
            if ban[i] != user[i]:
                return False
            
        
    
    return True


def solution(user_id, banned_id):
    
    lst = set()
    len_ban = len(banned_id)
    res = []
    for permu in permutations(user_id, len_ban):
        is_match = True
        for i in range(len_ban):
            if is_same(permu[i], banned_id[i]) == False:
                is_match = False
        
        if is_match == True:
            if sorted(permu) not in res:
                res.append(sorted(permu))
  
    return len(res)

# 문자들을 비교하는건 어렵지 않았으나 순열을 이용하는 방법이 어려웠다.
# for permu in permutations(user_id, len_ban): 이렇게 하면 permu에 user_id 리스트에 있는 단어들로 len_ban만큼 단어들이 만들어지고 그거를 다 비교해서 맞는것들을 res에 넣어주면 된다.
