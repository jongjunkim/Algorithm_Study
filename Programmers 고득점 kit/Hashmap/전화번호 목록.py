def solution(phone_book):
    
    if len(phone_book) == 1:
        return True
    phone = sorted(phone_book, key=lambda x:len(x))
    prefix = phone[0]
    listp = [prefix]
        index = 1
    for p in phone[1:]:
        if len(p) == len(prefix):
            listp.append(p)
            index += 1    
    if index == len(phone_book):
       return True 
    for pref in listp:
        for p in phone[index:]:
            if int(pref) == int(p[:len(prefix)]):
                return False      
    return True

#Answer
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        print(phone_book[i], phone_book[i+1][:len(phone_book[i])])
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

#여기서 내가 간과한게 phone_book.sort() 이렇게 하면 ["119", "97674223", "1195524421"] -> ["119", "97674223", "1195524421"] 이렇게 안됨
# 그냥 작은수부터 큰수로 정렬되는것이 아니라 "119","1195524421", "97674223"] 이렇게 앞자리가 작은수 부터 정리가됨 
