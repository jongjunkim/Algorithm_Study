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

