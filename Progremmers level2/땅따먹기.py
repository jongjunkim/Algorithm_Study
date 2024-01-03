def solution(land):
    for j in range(1, len(land)):
        land[j][0] += max(land[j-1][1], land[j-1][2], land[j-1][3])
        land[j][1] += max(land[j-1][2], land[j-1][3], land[j-1][0])
        land[j][2] += max(land[j-1][3], land[j-1][0], land[j-1][1])
        land[j][3] += max(land[j-1][0], land[j-1][1], land[j-1][2])

    return max(land[-1])

# 이렇게 하드코드 하는것도 하나중 방법이라고 생각해보자
