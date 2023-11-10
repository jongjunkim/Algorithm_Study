def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
        # str(i) = 9 이면 min() 값중 가장 낮은값이 2라고 치면 99라는 숫자가 answer에 들어가게 된다
        

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer