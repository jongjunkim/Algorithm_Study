N,K = input().split()

lst = list((map(int, input().split())))

res = []

for i in range(len(lst)-1):
    res.append(lst[i+1]- lst[i])

res.sort()
total = int(N) - int(K)
print(sum(res[:total]))
