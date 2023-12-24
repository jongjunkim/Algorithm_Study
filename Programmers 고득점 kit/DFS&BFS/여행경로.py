answers = []

def dfs(tickets, route, visited):
    global answers
    if len(route) == len(tickets) + 1:
        answers.append(route)
    else:
        for i, ticket in enumerate(tickets):
            if i not in visited and ticket[0] == route[-1]:
                new_visited = visited.copy()
                new_visited.add(i)
                dfs(tickets, route + [ticket[1]], new_visited)

def solution(tickets):
    global answers
    dfs(tickets, ["ICN"], set())
    answers.sort()
    return answers[0]

#이게 visited를 dfs밖에서 선언하고 그거를 계속쓰면 결국에는 모든 경로 방법들이 똑같은 visited=set()을 쓰게 되므로
#고유의 경로들의 가진 방법들을 여러개 만들수가 없으므로 dfs안에 vistied를 copy해서 새로운 visited()이용해서 만든다
