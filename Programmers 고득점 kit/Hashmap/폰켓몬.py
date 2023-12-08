from collections import Counter

def solution(nums):
    
    num = Counter(nums)
    
    return min(len(num), len(nums)//2)



#Note
def solution(nums):
    
    num = set(nums)
    
    return min(len(num), len(nums)//2)
