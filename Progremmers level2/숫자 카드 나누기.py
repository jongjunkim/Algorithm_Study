import math 
#최대 공약수
def findGCD(array):
    GCD = 0
    for i in range(len(array)):
        GCD = math.gcd(GCD, array[i])
    return GCD

#맨처음 GCD가 0이고 array[i]가 10이라고 가정할때 GCD = math.gcd(GCD, array[i]) 값은 10이 들어온다 즉 math.gcd(0,10)은 10이 들어옴
#따라서 그뒤에 만약 5가 array[i]값으로 들어오면 math.gcd(5,10)은 5가 되는거다

def divisible(array, divide):
    
    for num in array:
        if num % divide == 0:
            return False
    return True
        

def solution(arrayA, arrayB):
    
    num1 = findGCD(arrayA)
    num2 = findGCD(arrayB)
    
    resA = divisible(arrayB, num1)
    resB = divisible(arrayA, num2)
    
    if not (resA or resB):
        return 0
            
    return max(num1, num2)

#gcd math 사용해보기
    
     
    
        
