
N = int(input())

lst = [int(input()) for _ in range(N)]

lst.sort(reverse = True)

res = 0

for i,tip in enumerate(lst):
    temp = tip - (i+1-1)
    if temp > 0:
        res += temp

print(res)
