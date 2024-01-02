# 기본기

# split 함수
```python

# 문자열을 split을 이용해서 리스트를 만들어주는거
# 하지만 만약
# s = "abcdefg" 이렇게 붙어있는 거라면 split이 아니라 list 이용 r = list(s) 이렇게
s = "a b c d e f g"
r = s.split()
print(r)
#띄어쓰기로 문자를 나눈다
#['a', 'b', 'c', 'd', 'e', 'f', 'g']
```
```python
s = "a b c d e f g"
r = s.split('.')
print(r)

# '.' 을 이용해서 띄어쓰기를 하려하지만 '.' 없으므로 그냥 ['a b c d e f g'] 나온다
```
```python
s = "a b c d e f g"
r = s.split(' ',4)
print(r)
# 나누는 횟수를 제한. 4번까지만 split을 하고 그다음은 그대로 ['a', 'b', 'c', 'd', 'e f g']
```

# Join 함수
``` python
#리스트를 join으로 문자열로 합쳐주는거
a=['a','b','c','d','1','2','3']
r = ' '.join(a)
print(r)
#a b c d 1 2 3
```
``` python
#리스트를 join으로 문자열로 합쳐주는거
a=['a','b','c','d','1','2','3']
r = ''.join(a)
print(r)
#abcd123
```
```python
a=['a','b','c','d','1','2','3']
r = '-'.join(a)
print(r)
#a-b-c-d-1-2-3
```
# 좌우 공백 제거
``` python
S=input()
#' asdf asdf '

print(S.strip())
#asdf asdf
```

# Bit Manipulation
>>> for i in range(20):
print(i, bin(i), oct(i), hex(i)) # 십진수, 이진수, 8진수, 16진수를 출력

0 0b0 0o0 0x0
1 0b1 0o1 0x1
2 0b10 0o2 0x2
3 0b11 0o3 0x3
4 0b100 0o4 0x4
...........
앞에 0b 와 0o 0x는 몇진수인지 나타내는거 그래서 순수히 숫자만 가져오고싶으면 bin(i)[2:] 하면됨

Bit를 숫자로 바꾸는거는 int('1001', 2) 하면 1001을 2진법을 이용해서 숫자로 바꿔준다

# 소수 판별


```python
def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):  #for i in range(2, num) 했을경우 시간초과 그래서 이걸 사용
        if num % i == 0:
            return False
    
    return True
```

# Dynamic Programming 

```python
def solution(n):
    
    if n <= 1:
        return n
    
    dp = [0] * (n+1)
    dp[1] = 1
    
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
     
    return dp[n] % 1234567
```



