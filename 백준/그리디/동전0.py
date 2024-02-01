# 이렇게 했을경우 답은 맞지만 시간초과가 난다.
N, K = map(int, input().split())

lst = []

for _ in range(N):
    lst.append(int(input()))

ans = 0
while K > 0:

    coin = 0
    for i in range(len(lst)-1, -1, -1):
        if lst[i] <= K:
            coin = lst[i]
            break
    
    K -= coin
    ans += 1

print(ans)

#아래같은 방법이 optimized된 버전
N, K = map(int, input().split())

lst = []

for _ in range(N):
    lst.append(int(input()))

ans = 0

for i in range(len(lst)-1, -1, -1):
    if lst[i] <= K:
        ans += K // lst[i]
        K = K % lst[i]
    if K == 0:
        break
    
print(ans)

