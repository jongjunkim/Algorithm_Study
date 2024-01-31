
n = int(input())
total = n
ropes = [int(input()) for _ in range(n)]
 
ropes.sort()

res = 0
for i,rope in enumerate(ropes):
    res = max(res, rope * (total - i))

print(res)
