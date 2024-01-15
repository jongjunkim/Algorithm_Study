class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        subset = []

        
        def dfs(index):

            if index >= len(s):
                res.append(subset.copy())
                return

            for i in range(index, len(s)):
                if self.ispalindrome(index, i, s):
                    subset.append(s[index: i+1])
                    dfs(i+1)
                    subset.pop()

        dfs(0)

        return res

    def ispalindrome(self, l, r, s):

        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
        



        