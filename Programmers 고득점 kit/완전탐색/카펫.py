def solution(brown, yellow):   
    lst = set() 
    for i in range(1, yellow):
        if yellow % i == 0:
            width = max(i, yellow//i)
            length = min(i, yellow//i)
            lst.add((width,length))
    
    res = float('inf')
    num1, num2 = 0, 0
    for pair in lst:
        width, length = pair
        if res > width - length:
            res = width - length
            num1, num2 = width, length

    return [num1,num2]

#이경우 입력값이 18,6 일경우 답은 [8,3]이지만 [6,4]로 나옴
#따라서 yellow 값을 맞춰야 하는데 그경우를 찾지 못했는데 생각보다 쉬웠음.

def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(1, total):
        if total % i == 0:
            j = total // i
            if (i - 2) * (j - 2) == yellow:
                return [max(i, j), min(i, j)]

# 보면 (i-2) * (j-2) == yellow를 했을때 yellow값도 맞으면서 길이와 넓이도 구할수 있다
