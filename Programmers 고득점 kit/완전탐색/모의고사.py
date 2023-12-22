def solution(answers):
    
    num1 = "12345"
    num2 = "21232425"
    num3 = "3311224455"
  
    
    count1, count2, count3 = 0, 0, 0
    i,j,k = 0,0,0
    for answer in answers:
        if num1[i] == str(answer): 
            count1 +=1
        if num2[j] == str(answer):
            count2 +=1
        if num3[k] == str(answer):
            count3 +=1
        i+=1
        j+=1
        k+=1
        if i >= len(num1):
            i = 0
        if j >= len(num2):
            j = 0
        if k >= len(num3):
            k = 0
        
    res = max(count1, count2, count3)
    
    list = []
    
    if res == count1:
        list.append(1)
    if res == count2:
        list.append(2)
    if res == count3:
        list.append(3)
        
    return list
    

#굳이 초기화를 안해줘도 % 연산을 통해서 자릿값을 구하면된다

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

