def solution(today, terms, privacies):
    answer = []
    
    curyear, curmonth, curday = map(int,today.split("."))
    
    #key point here is map function map int to every elment in today
    
    dictionary = {}
    
    for term in terms:
       dictionary[term[0]] = int(term[2:]) * 28 #term[2] is just 1 when 12
    
    for i in range(len(privacies)):
        date, term = privacies[i].split(" ")
        year, month, day = map(int, date.split("."))
        
        dyear = (curyear - year) * 336
        dmonth = (curmonth - month) * 28
        dday = (curday - day) 
        
        total = dyear + dmonth + dday
        
        if dictionary[term] <= total:
            answer.append(i+1)
        

    return answer