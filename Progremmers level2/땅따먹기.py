def solution(land):
    for j in range(1, len(land)):
        land[j][0] += max(land[j-1][1], land[j-1][2], land[j-1][3])
        land[j][1] += max(land[j-1][2], land[j-1][3], land[j-1][0])
        land[j][2] += max(land[j-1][3], land[j-1][0], land[j-1][1])
        land[j][3] += max(land[j-1][0], land[j-1][1], land[j-1][2])

    return max(land[-1])

# 이렇게 하드코드 하는것도 하나중 방법이라고 생각해보자


def solution(land):
    
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

# max(land[i -1][: j] + land[i - 1][j + 1:]) 이부분이 리스트에있는 값을 더하는게 아닌 서로 split된 리스트를 합친것 중에서 max값을 구하는거 그리고 자기 자신과 더하기
