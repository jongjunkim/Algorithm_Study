import math
def solution(progresses, speeds):
    
    stack = []
    pro = [-1]
    count = 0
    for progress, speed in zip(progresses, speeds):
        temp =  math.ceil((100 - progress) / speed) # // floor division 5//3 = 1. / regular division 5/3 = 1.666
        if pro and pro[-1] < temp:
            stack.append(count)
            count = 0
        pro.append(max(pro[-1], temp))
        count += 1
    stack.append(count)

    return stack[1:]
