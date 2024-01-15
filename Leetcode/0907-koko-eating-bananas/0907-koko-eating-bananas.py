class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles) # left should be 1 becuase 0 menas KoKo doesn't eat banana
        res = r

        while l <= r:

            mid = (l+r)//2
            hour = 0
            for pile in piles:
                hour += math.ceil(float(pile)/mid)

            if hour <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
            # 1 1 2 2 = 6 