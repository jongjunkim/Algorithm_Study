import heapq

def solution(jobs):
    answer = 0
    total_jobs = len(jobs)
    jobs.sort()  # 요청 시점을 기준으로 작업을 정렬

    heap = []  # 최소 힙
    current_time = 0  # 현재까지 처리한 작업 시간

    while jobs or heap:
        # 현재 시간까지 요청된 작업을 힙에 추가
        while jobs and jobs[0][0] <= current_time:
            job_time, request_time = jobs.pop(0)
            heapq.heappush(heap, (job_time, request_time))

        if heap:
            job_time, request_time = heapq.heappop(heap)
            current_time += request_time
            answer += current_time - job_time
        else:
            # 힙이 비어있을 때는 작업이 들어온 순서대로 처리
            current_time = jobs[0][0]

    return answer // total_jobs  # 소수점 이하 버림
