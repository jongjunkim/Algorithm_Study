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

