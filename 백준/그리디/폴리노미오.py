# 풀이
board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
    
else:
    print(board)

#파이썬에서 replace는 문자 왼쪽열 부터 해당하는 문자열을 찾아서 치환해주는 함수
# XXXX가 오면 AAAA로 해주고 XX면 BB로 치환


#내 정답
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
