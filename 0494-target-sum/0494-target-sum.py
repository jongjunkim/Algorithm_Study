class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def backtracking(index, cursum):

            if index == len(nums):
                return 1 if cursum == target else 0
            
            if (index, cursum) in dp:
                return dp[(index, cursum)]

            dp[(index, cursum)] = backtracking(index+1, cursum + nums[index]) + backtracking(index+1, cursum - nums[index])
            return dp[(index, cursum)]
        
        return backtracking(0,0)
        