def solution(s):
    
    word = s.split(' ')
    
    res = []
    for w in word:
        if w == '':
            res.append('')
        else:
            temp = w[0].upper() + w[1:len(w)].lower()
            res.append(temp)
    
    return " ".join(res)
#문자열에 앞에 공백이 여러번 있을수 있는 경우가 있어서 그거를 해결하느라 시간이 걸림
