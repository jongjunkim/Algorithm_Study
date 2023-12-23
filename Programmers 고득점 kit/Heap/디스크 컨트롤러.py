import heapq

def solution(jobs):
    
    jobs.sort()
    total = len(jobs)
    candidate = []
    currentTime = 0
    answer = 0
    
    while jobs or candidate:
        while jobs and jobs[0][0] <= currentTime:
            time, delay = jobs.pop()
            heapq.heappush(candidate, (delay, time))
        
        if candidate:
            delay, time = heapq.heappop(candidate) 
            currentTime += delay
            answer += currentTime - time
        else:
            currentTime = jobs[0][0]
            
    return answer // total

# 내가 놓쳤던거  heapq.heappush(candidate, (delay, time)) 이부분을  heapq.heappush(candidate, (time, delay)) 이렇게 했었는데 
# 이렇게 해버리면 heappush를 할때 time을 기준으로 해서 push가 되니 절대로 delay시간이 작은 순서대로 push가 안됨 
# 따라서 delay를 앞에 넣고 time을 넣는거
