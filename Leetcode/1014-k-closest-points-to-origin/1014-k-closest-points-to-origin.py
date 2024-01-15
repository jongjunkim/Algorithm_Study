class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        for x1, x2 in points:
            distance = (x1 ** 2) + (x2 ** 2)
            minHeap.append((distance, x1, x2))
        
        heapq.heapify(minHeap)

        res = []
        while k > 0:
            dis, x, y = heapq.heappop(minHeap)
            res.append((x,y))
            k -= 1
        return res
