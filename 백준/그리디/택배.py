from sys import stdin

N, C =  map(int, stdin.readline().split())
M = int(stdin.readline())
infos = []
for _ in range(M):
    s, r, box = map(int, stdin.readline().split())
    infos.append((s, r, box))
infos.sort(key=lambda x :  x[1])

print(infos)

capa = [C]*N
total = 0
for s, r, box in infos:
    _min = C
    for i in range(s, r):
        if _min > min(capa[i], box) :
            _min = min(capa[i], box)
    for i in range(s, r):
        capa[i] -= _min
    total += _min
print(total)

# 큐를 이용해서 빼주려 했지만 구현 실패및 로직상 맞지가 않는다
# 처음부터 각 마을에 배정된 capacity를 지정뒤 배달수 있는만큼 뺴주면 된다
