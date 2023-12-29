def solution(s):
    
    hashmap = {")":"(", "}":"{", "]":"["}
    
    count = 0
    for i in range(len(s)):
        s = s[1:len(s)] + s[0] 
        stack = []
        for word in s:
            if stack and word in hashmap and stack[-1] == hashmap[word]:
                stack.pop()
            else:
                stack.append(word)
        if not stack:
            count+=1
        
    return count
