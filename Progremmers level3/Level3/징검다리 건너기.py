def solution(stones, k):
    l = 1
    r = max(stones)
    res = 1
    while l <= r:
        mid = (l + r) // 2  # 건너는 친구 수 
        # mid명 건넌다고 가정했을 때 연속 점프수 -> k 초과 시 건너기 불가능하다고 판단하고 break
        cnt = 0  
        for stone in stones:
            if stone - mid < 0:
                cnt += 1
                if cnt >= k:
                    r = mid - 1  # 건널 수 없음 -> 건널 사람 줄이기
                    break
            else:
                cnt = 0        
        else:  # break없이 loop 무사 탈출 -> mid명 건널 수 있음 -> 건널 사람 늘리기
            res = mid
            l = mid + 1
      
    return res
#위에 답은 처음부터 건나갈 사람을 정하고 stone에서 그만큼 빼준다음 0 이 연속으로 k번 나오게 되면 끝나는 구조.

#답은 다 맞으나 효율성에서 많이 떨어짐
def solution(stones, k):
  
    count = 0
    while True:
        zero = 0
        temp = 0
        for i in range(len(stones)):
            if stones[i] > 0:
                stones[i] -= 1
                zero = 0
            else:
                zero += 1
                temp = max(temp, zero)
            
        if temp >= k:
            break
        count += 1
    
            
    return count
