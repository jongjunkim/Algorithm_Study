def solution(sequence, k):
    
    answer = []
    mini = float("inf")

    for i in range(len(sequence)):
        r = i + 1
        cursum = sequence[i]
        if cursum == k:
            return [i,i]
        while r < len(sequence) and cursum != k:
            cursum += sequence[r]   
            if mini < r - i:
                break      
            if cursum == k:
                mini = min(mini, r-i)
                answer = [i,r]
            r += 1
      
    return answer

#got 44.1 out of 100