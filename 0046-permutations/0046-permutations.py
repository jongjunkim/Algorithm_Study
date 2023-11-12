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


* [1,2,3] 이 있을때 subset에 nums가 3이 맨처음 들어오고 나서 다음 재귀호출할때는 다시 for num in nums:는 1 부터 돌아간다 이미 subset에는 3이 있으므로 1이 들어가고 [3,1]이라는 subset이 만들어진다.
* 이게 가능한 이유는 index가 len(nums)보다 클때 끝나는게 아니라 index는 여기서 subset의 개수 즉 subset이 len(nums)와 같을때 재귀호출이 끝나기 때문에 
