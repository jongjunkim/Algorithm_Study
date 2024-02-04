N = int(input())

lst = []

total = 0
for _ in range(N):
    village, num = map(int, input().split())
    total += num
    lst.append((village, num))

lst.sort(key=lambda x:x[0])

v = 0
for pos, peo in lst:
    v += peo
    if v >= total/2:
        print(pos)
        break

# if v >= total//2:
# 이렇게 했을경우 답이 맞지가 않음
