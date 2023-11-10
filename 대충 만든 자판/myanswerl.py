def solution(keymap, targets):
    
    kmap = {}
    
    for key in keymap:
        for i,k in enumerate(key):
            if k not in kmap:
                kmap[k] = i + 1
            else:
                kmap[k] = min(kmap[k], i + 1)
    res = []            
    for target in targets:
        count = 0
        for key in target:
            if key in kmap:
                count += kmap[key]
            else:
                count = 0
                count -= 1
                break
                
        res.append(count)
        
       
    return res

#got 100 out of 100