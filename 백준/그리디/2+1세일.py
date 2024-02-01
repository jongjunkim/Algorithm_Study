#아래 방법도 맞았지만 너무 느림
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
length = len(lst)

if length < 3:
    print(sum(lst))
    exit(0)
    
total = 0
idx = 0

while idx <= length:

    if idx + 3 <= length:
        total += sum(lst[idx:idx+2])
    else:
        total += sum(lst[idx:])

    idx += 3

print(total)

# 3으로 나누고 나머지 값이 2만 아닌값만 넣어주면됨!
from sys import stdin

arr = []
n = int(stdin.readline())
for i in range(n):
    arr.append(int(stdin.readline()))

arr.sort(reverse=True)
ans = 0

for i in range(n):
    if i % 3 != 2:
        ans += arr[i]
print(ans)
