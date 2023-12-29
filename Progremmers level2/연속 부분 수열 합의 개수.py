

def solution(elements):
    
    res = set()
    k = len(elements)
    elements *= 2
    
    for i in range(1, k):
        for j in range(0,k):
            res.add(sum(elements[j:j+i]))
    return len(res) + 1

#맨처음 list를 2배로 늘려서 하는게 쉽다고 생각했지만 그렇게 되면 element가 2배로 늘어나니까 그만큼 시간이 걸리다는 착각을 했다.
#그래서 만약 list가 끝에 도달했을때 앞에 숫자가 필요하다면 포인터를 다시 앞으로 보내려했지만 그렇게 되니 알고리즘이 꼬이고 가독성도 이상함
#그냥 처음부터 element를 2배 늘리기전에 element길이를 알고 하는게 편함
