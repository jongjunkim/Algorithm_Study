
num = int(input())

count = 0
while num >= 0:

    if num % 5 == 0:
        count += int(num/5)
        num = 0
        break
    
    num -= 2
    count += 1

if num < 0:
    print(-1)
else:
    print(count)
