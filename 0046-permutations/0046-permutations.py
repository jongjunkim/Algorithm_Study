class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(index):
            
            if index== len(nums):
                res.append(subset.copy())
                return

            if index > len(nums):
                return
            
            for num in nums:
                if num not in subset:
                    subset.append(num)
                    dfs(index + 1)
                    subset.pop()

        dfs(0)

        return res