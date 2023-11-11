​# myanswer

```Python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        res_index= []
        subset = [] #nums
        index = []

        def dfs(i):

            if i >= len(nums):
                if index not in res_index and subset not in res:
                    res.append(subset.copy())
                    res_index.append(index.copy())
                return 

            if i not in index:
                subset.append(nums[i])
                index.append(i)
            
            dfs(i+1)
            if subset:
                subset.pop()
                index.pop()
            dfs(i+1)

        dfs(0)

        return res
```
* input: [4,4,4,1,4]
* output: [[4,4,4,1,4],[4,4,4,1],[4,4,4,4],[4,4,4],[4,4,1,4],[4,4,1],[4,4],[4,1,4],[4,1],[4],[1,4],[1],[]]
* expected: [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

# duplicate results with different order

# key point
* sort the list first. If the previous value and currrent value are same -> continue
