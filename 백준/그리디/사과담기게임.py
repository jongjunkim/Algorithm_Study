n, m = map(int, input().split())           
j = int(input())                          

apples = [int(input()) for _ in range(j)]  

left = 1
right = left + m - 1
res = 0

for apple in apples:

    if left <= apple <= right:
        continue

    if apple < left:
        res += left - apple
        left = apple
        right = left + m - 1
    elif apple > right:
        res += apple - right
        right = apple
        left = right - m + 1

print(res)
