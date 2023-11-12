```Python
​class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        res = []
        candidates.sort()
        def dfs(idx, path, cur):
            if cur > target: return
            if cur == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                dfs(i, path+[candidates[i]], cur+candidates[i])
        dfs(0, [], 0)
        return res
```
```Python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      
        res = []
        candidates = sorted(candidates)
        subset = []

        def backtracking(i, cursum):
            if cursum > target :
                return
            if cursum == target:
                res.append(subset.copy())
                return
            for a in range(i, len(candidates)):
                if a > i and candidates[a] == candidates[a-1]:
                    continue
                subset.append(candidates[a])
                backtracking(a+1, cursum + candidates[a])
                subset.pop()
        backtracking(0, 0)
        return res
```
* combinationSum manages state by creating a new list and sum in each recursive call,
* whereas combinationSum2 tracks the current combination's state by sharing and continuously modifying a single lis
