class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        res = []
        subset = []
        hashmap = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs",
                "8": "tuv", "9":"wxyz"}

        def dfs(index, curletter):

            if len(curletter) == len(digits):
                res.append(curletter)
                return

            for c in hashmap[digits[index]]:
                dfs(index+1, curletter + c)

        if digits:
            dfs(0, "")

        return res