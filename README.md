# Algorithm Study.
This repository is a place where I upload my studies on algorithms. I have studied using Leetcode and a Korean platform called Programmers.

# Heap
https://school.programmers.co.kr/learn/courses/30/lessons/42628

``` Python
import heapq
def solution(operations):
    q = []
    minq = []
    maxq = []
    
    for operation in operations:
        oper, num = operation.split()
        num = int(num)
        
        if oper == 'I':
            heapq.heappush(q, num) #push 
            heapq.heappush(minq, num)
            heapq.heappush(maxq, -num)
        elif oper == 'D' and num == 1:
            if maxq:
                val = -heapq.heappop(maxq) #pop
                minq.remove(val)
        elif oper == 'D' and num == -1:
            if minq:
                val = heapq.heappop(minq)
                maxq.remove(-val)
    
    max_val = -maxq[0] if maxq else 0
    min_val = minq[0] if minq else 0
    
    return [max_val, min_val]
```

``` Python
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 리스트를 힙으로 변환 (in-place)
heapq.heapify(my_list)

#print the smallest number 
print(my_list)
```
