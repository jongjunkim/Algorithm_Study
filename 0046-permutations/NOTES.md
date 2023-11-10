#My Wrong code
```Python
​class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(index):
            
            if index >= len(nums):
                return

            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            if nums[index] not in subset:
                subset.append(nums[index])
                
            dfs(index + 1)
            subset.pop()
            dfs(index + 1)

        for i in range(len(nums)):
            dfs(i)

        return res
```
index를 이용해서 subset을 res값에 넣는게 아니라 index는 subset의 개수를 카운트 하기 위해 사용
실제적으로는 for loop를 dfs function에 넣어서 해줘야함 그리고 num이 있는지 없는지 확인 있다면 확인해야함
