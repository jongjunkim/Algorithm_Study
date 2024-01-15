class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2 
        res = set()
        res.add(0)


        for i in range(len(nums)-1, -1, -1):
            nextdp = set()
            for num in res:
                if target == (nums[i] + num):
                    return True
                nextdp.add(nums[i] + num)
                nextdp.add(num)
            res = nextdp

        return False
        