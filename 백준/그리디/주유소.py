
N = int(input())

distance = list(map(int,input().split()))
stations = list(map(int,input().split()))

idx = 0
res = 0
curstation = float("inf")
while idx != len(stations)-1:

    if curstation > stations[idx]:
        curstation = stations[idx]

    res += curstation * distance[idx]
    idx += 1


print(res)
