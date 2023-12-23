def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    for i in reserve:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
            
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
        
    return n - len(lost)

#이코드가 맞다. 둘이 똑같이 duplicate인 부분을 제거하고 하는거지만 set으로 했을때까 더 정교하다.
def solution(n, lost, reserve):
    # Set data structure to efficiently check if a student has an extra or lost a uniform
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for student in reserve_set:
        # Check if the student can lend the uniform to the previous student
        if student - 1 in lost_set:
            lost_set.remove(student - 1)
        # Check if the student can lend the uniform to the next student
        elif student + 1 in lost_set:
            lost_set.remove(student + 1)

    return n - len(lost_set)


#배운거 
#reserve_set = set(reserve) - set(lost)
#lost_set = set(lost) - set(reserve)
