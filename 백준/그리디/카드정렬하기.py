import heapq

N = int(input())

lst = []
for _ in range(N):
    heapq.heappush(lst, int(input()))

sum = 0
while len(lst) > 1:

    num1 = heapq.heappop(lst)
    num2 = heapq.heappop(lst)
    sum += num1 + num2
    heapq.heappush(lst, num1+num2)

print(sum)

# lst를 받고 sort할 필요없이 heappush를 이용해서 넣어주면 됨
