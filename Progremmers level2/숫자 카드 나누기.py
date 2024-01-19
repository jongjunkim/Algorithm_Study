import math 
#최대 공약수
def findGCD(array):
    GCD = 0
    for i in range(len(array)):
        GCD = math.gcd(GCD, array[i])
    return GCD

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
    
     
    
        
