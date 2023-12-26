# Permutation
```python
for permu in permutations(user_id, len_ban):
        is_match = True
        for i in range(len_ban):
            if is_same(permu[i], banned_id[i]) == False:
                is_match = False
        
        if is_match == True:
            if sorted(permu) not in res:
                res.append(sorted(permu))  
    return len(res)
```
