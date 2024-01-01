def solution(str1, str2):
    
    hashmap1, hashmap2 = {}, {}
    dup = 0
    
    for i in range(len(str1)-1):
        word = str1[i:i+2].lower()
        if word.isalnum() and not word[0].isdigit() and not word[1].isdigit():
            hashmap1[word] = hashmap1.get(word, 0) + 1
           
     
    for i in range(len(str2)-1):
        word = str2[i:i+2].lower()
        if word.isalnum() and not word[0].isdigit() and not word[1].isdigit():
            hashmap2[word] = hashmap2.get(word, 0) + 1
            
    
    intersection = 0
    for key, value in hashmap1.items():
        if key in hashmap2:
            intersection+= min(value, hashmap2[key])
            
    union = sum(hashmap1.values()) + sum(hashmap2.values()) - intersection
    
    return 65536 if intersection == union else int(intersection/union * 65536) 

# 맨처음 hashmap 한개를 해서 두개의 word의 카운트를 계산한후 duplication을 word conut // 2하면 되는줄 알았지만 생각해보니 같은 hashmap을 썼을때
# 한단어에서 똑같은 단어가 2번 나오는 경우가 있어서 아이에 접근방식이 잘못되었음
# 그리고 나서 hashmap을 두개를 만든다음 보니 intersection과 union부분을 어떻게 만들어야 하나 고민을 했음 그리고 나온게 이거
