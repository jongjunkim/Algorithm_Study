class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

        
        len1, len2, len3 = len(s1), len(s2), len(s3)
        
        if len1 + len2 != len3:
            return False
        
        res = {}

        def backtracking(i, j , k):

            if k == len3:
                return True
            
            if (i, j) in res:
                return res[(i,j)]

            ans = False
            if i < len1 and s1[i] == s3[k]:
                ans = ans or backtracking(i+1, j , k+1)

            if j < len2 and s2[j] == s3[k]:
                 ans = ans or backtracking(i, j+1 , k+1)

            res[(i,j)] = ans

            return ans

        return backtracking(0, 0, 0)



