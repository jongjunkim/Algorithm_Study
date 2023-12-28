def solution(mushrooms):


    current, total = 0, 0
    for mushroom in mushrooms:
        current += mushroom
        
        if abs(current - 100) <= abs(total - 100):
            total = current 
    
    return total

mushrooms = [1,2, 3, 5, 8, 13, 21, 34, 55, 89]
result = solution(mushrooms)
print("Result:", result) 

#맨처음 이렇게 했으나 보이는 test case에서 반례의 케이스들이 있어서 틀림
def solution(mushrooms):
    current, prev = 0, 0
    for mushroom in mushrooms:
        current += mushroom
        if current >= 100:
            prev = current - mushroom
            break
    

    return current if (current - 100) <= (100 - prev) else prev


