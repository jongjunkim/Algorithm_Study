from collections import Counter

def solution(lottos, win_nums):
    
    ranking = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
      
    count = 0
    zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            count += 1
        if lotto == 0:
            zero += 1
    
    
    return [ranking[count+zero], ranking[count]]


