def solution(record):
    
    username = {}
    log = []
    
    for r in record:
        if r.split(" ")[0] == "Leave":
            status, user_id = r.split(" ")
            log.append((status, user_id))
        elif r.split(" ")[0] == "Enter":
            status, user_id, name = r.split(" ")
            username[user_id] = name
            log.append((status, user_id))
        else:
            _, user_id, name = r.split(" ")
            username[user_id] = name
    
    res = []
      
    for l in log:
        if l[0] == "Enter":
            res.append((f"{username[l[1]]}님이 들어왔습니다."))
        else:
            res.append((f"{username[l[1]]}님이 나갔습니다."))
    
    return res

#단순구현임
