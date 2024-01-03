import math

def solution(fees, records):
    
    hashmap = {} 
    for record in records:
        time, carNum, status = record.split(" ")
        hour, minute = time.split(":")
        if status == "IN":
            if carNum not in hashmap:
                hashmap[carNum] = -(int(hour) * 60 + int(minute)) - 1
            else:
                hashmap[carNum] -= int(hour) * 60 + int(minute) - 1
        else:
            stack = int(hour) * 60 + int(minute) + hashmap[carNum]
            hashmap[carNum] = stack 
    hashmap = sorted(hashmap.items(), key = lambda x: x[0])
    res = []
    for car, time in hashmap:
        if time < 0:
            res.append(1439 + time + 1)
        else:
            res.append(time + 1)    
    pay = []
    for t in res:
        if t > fees[0]:
            pay.append(fees[1] + math.ceil((t - fees[0])/fees[2]) * fees[3])
        else:
            pay.append(fees[1])   
    return pay

#내가 구현한건데 83점맞음 뭐떄문에 틀렷는지 감이 안잡힌다.. 로직은 맞지만 마이너스한 부분이 틀린것같음
