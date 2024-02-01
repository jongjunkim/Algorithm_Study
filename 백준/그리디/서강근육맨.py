
N = int(input())

loss = list(map(int, input().split()))

tmp = []

loss.sort()

if(N%2==1):
    tmp.append(loss[-1])
    loss = loss[:-1]

for i in range(len(loss)//2):
    tmp.append(loss[i] + loss[len(loss)-1-i])

print(max(tmp))    
