def solution(skill, skill_trees):
    
       
    order = []
    for skills in skill_trees:
        temp = ""
        for s in skills:
            if s in skill:
                temp += s
        order.append(temp)
    
    count = 0
    for skills in order:
        if skill[:len(skills)] == skills:
            count += 1
        else:
            continue
    
    return count

#hashmap을 이용해서 문자열이 해당 문자열에 포함이 되는지 확인하려하는데 hashmap은 굳이 필요없다. 
#그리고 order를 확인하려했지만 그냥 skill의 len(skills)만큼 비교하면 되는거임
