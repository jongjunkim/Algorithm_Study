N = int(input())
K = int(input())
lst = set(map(int, input().split()))

lst = list(lst)
lst.sort()
res = []
for idx in range(len(lst)-1):
    res.append(lst[idx+1] - lst[idx])

res.sort()
print(res)
total = len(res) - K
print(sum(res[:total+1]))

#set을 for loop에 
# for idx in range(len(lst)):
#  print(lst[idx]) 
# 처럼 하게되면 set is not ~~ 에러가 나옴
# set을 for loop로 idx와 함께 돌리고 싶으면 그전에 list로 변경해줘야함
