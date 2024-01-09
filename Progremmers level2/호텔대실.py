def solution(book_time):
    answer = 0
    book_time_int=[]

    for start,end in book_time:
        book_time_int.append([int(start[:2])*60+int(start[3:]),1])
        book_time_int.append([int(end[:2])*60+int(end[3:])+10,-1])
    

    book_time_int.sort()
  
    now=0
    for time in book_time_int:
        now += time[1]
        answer=max(answer,now)

    return answer

# book_time_int = sorted(book_time_int, key = lambda x:x[0]) 이렇게 했을떄 답이 다르게 나온다
