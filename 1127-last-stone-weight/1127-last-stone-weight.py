class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        stones = [-s for s in stones] #negate all weight values in-place
        heapq.heapify(stones)

        while(len(stones)) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first-second)
        stones.append(0)   # just in case when the array is [2,2] -> [0]   
        return abs(stones[0])