
#이렇게 했을경우 시간초과 만약 array가 [10,9,2,5,3,7,101,18] 1 부터 N이 차레대로 있는게 아니라면 이 방법을 써도되는데 만약 그게 아니라면 밑에 방법
#이방법은 배열에서 가장 긴 수열을 찾는 문제
N = int(input())

lst = list(map(int, input().split()))

LIS = [1] * (N+1)

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if lst[i] < lst[j]:
            LIS[i] = max(LIS[i], 1 + LIS[j])

print(N-max(LIS))


# 가장 긴 수열을 포함하지 않는 나머지를 움직여야 하기 때문에 N - max(LIS)
N = int(input())

lst = list(map(int, input().split()))

LIS = [0] * (N+1)

for i in range(N):
    idx = lst[i]
    LIS[idx] = max(LIS[idx], LIS[idx-1]+1)

print(N - max(LIS))
