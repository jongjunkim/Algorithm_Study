def solution(s):
  
    s = s.replace('{','').replace(',',' ').split('}')
    
    for i,v in enumerate(s):
        s[i] = v.split()
        
    s.sort(key=lambda x:len(x))
    
    res = []
    for tuple in s:
        for i in tuple:
            if int(i) not in res:
                res.append(int(i))

    return res

#문자열을 리스트로 만드는게 이문제의 키포인트이다. 그래서 위에 같이 비슷하게 replace이용해서 했지만 그이후가 문제였음 
# 그래서 결국에는 저 문제를 해결하기 해설을 봤음
