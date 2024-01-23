import heapq

def solution(operations):
    
    minq = []
    maxq = []
    for oper in operations:
        ins, num = oper.split(" ")
        if minq and maxq and ins == "D" and int(num) < 0: #최소값
            removed = heapq.heappop(minq)
            maxq.remove(-removed)
        elif minq and maxq and ins == "D" and int(num) > 0: #최대값           
            removed = - heapq.heappop(maxq)
            minq.remove(removed)
        elif ins == "I":
            heapq.heappush(minq, int(num)) 
            heapq.heappush(maxq, - int(num))
   
    if not minq and not maxq:
        return [0,0]
    
    return [-maxq[0], minq[0]]
