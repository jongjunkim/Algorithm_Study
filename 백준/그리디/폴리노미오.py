
def solution(word):
    res = ""
    count = 0
    lst = []
    for w in word:
        if w == ".":
            if count % 2 != 0:
                return -1
            if count != 0:
                lst.append(count)
            lst.append(".")
            count = 0
        else:
            count += 1
    
    if count % 2 != 0:
        return -1

    if count != 0:
        lst.append(count)

    for w in lst:
        if w == ".":
            res += "."
        else:
            count = w
            temp = ""
            while count != 0:
                if count > 2:
                    temp += "AAAA"
                    count -= 4
                else:
                    temp += "BB"
                    count -= 2
            res += temp

    return res 
    

word = input()
print(solution(word))
