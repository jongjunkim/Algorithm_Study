from collections import defaultdict

def solution(s):
    
    answer = len(s)
    
    slice = 1
    
    while slice != len(s)//2+1:
        previous = s[0:slice]
        temp = ""
        count = 1
        for i in range(slice, len(s), slice):
            word = s[i:i+slice]
            if previous == word:
                count += 1      
            else:
                temp += str(count) + previous if count > 1 else previous 
                previous = word
                count = 1
        
        temp += str(count) + previous if count > 1 else previous
        answer = min(answer, len(temp))
        slice += 1
    return answer

#거의 비슷했지만 count = 0 이 초기값일 경우 맞지가 않다.
