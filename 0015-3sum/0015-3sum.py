class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        nums.sort()
        res = set()
        for i, n in enumerate(nums):

            l, r = i+1, len(nums)-1

            while l < r:

                add = n + nums[l] + nums[r]

                if add < 0:
                    l += 1
                elif add > 0:
                    r -= 1
                else:
                    res.add( (n, nums[l], nums[r]) )
                    r -= 1
                    l += 1
        
        return res

    