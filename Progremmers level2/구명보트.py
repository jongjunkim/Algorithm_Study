def solution(people, limit):
    
    people.sort()
    
    l, r = 0, len(people) - 1
    answer = 0
    
    while l<= r:
        
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        elif people[l] + people[r] > limit:
            r -= 1
        answer += 1
        
    return answer
# 아 문제를 보니까 최대 2명씩 봤게 못태운다는거를 잊고 풀었다
# 일단 sliding window appraoch로 이용해서 구현하려 했으나 구현이 잘못된건지 접근방법이 잘못된거인지 작동되지가 않음
# Two pointer를 사용한다는 접근법은 비슷했지만 결국에는 제일 무게가 적은 사람과 많이 나온 사람이 같이 타게되면서 만약 limit에 넘어가게 되면 무거운 사람만 태우고
# 그렇지 않을 경우 다 태우더라도 +1 은 해야함
    
