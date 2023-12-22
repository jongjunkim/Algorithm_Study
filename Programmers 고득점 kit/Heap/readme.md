import heapq as hp

hp.heapify(x)			# 리스트 x를 힙으로 반환한다.
hp.heappush(heap, item)		# item 값을 heap으로 push한다.
hp.heappop(heap)		# heap에서 가장 작은 값을 pop한다(=빼낸다).
hp.heappushpop(heap, item)	# heap에 item을 push한 후, heap에서 가장 작은 값을 pop한다. (개별 호출하는 것보다 더 효율적)
hp.heapreplace(heap, item)	# heap에서 가장 작은 값을 pop한 후, 새로운 item을 push한다. (개별 호출하는 것보다 더 효율적)

출처: https://mini-min-dev.tistory.com/202

heapq를 Max heap으로 사용하고 싶은 경우
```Python
import heapq

def solution(scoville, K):
    # Negate the values to create a max heap
    neg_scoville = [-x for x in scoville]
    heapq.heapify(neg_scoville)
    
    count = 0
    
    while len(neg_scoville) >= 2:
        first = -heapq.heappop(neg_scoville)  # Negate again to get the original value
        second = -heapq.heappop(neg_scoville)
        res = first + (second * 2)
        heapq.heappush(neg_scoville, -res)  # Negate before pushing onto the max heap
        count += 1
        if res > K:
            break
    
    return count if res > K else -1
```
