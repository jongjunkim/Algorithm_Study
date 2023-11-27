def solution(n, computers):
    def dfs(com_number):
        nonlocal res

        if com_number in visited:
            return
        
        visited.add(com_number)
        for i, c in enumerate(computers[com_number]):
            if com_number == i:
                continue
            if c == 1:
                dfs(i)

    res = 0
    visited = set()
    for i,computer in enumerate(computers):
        if i not in visited:
            res += 1
            dfs(i)
    return res

# Note:
nonlocal res 그냥 def 밖에 있는 변수를 사용하고 싶으면 nonlocal을 써야함
