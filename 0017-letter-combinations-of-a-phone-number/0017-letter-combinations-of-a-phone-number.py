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
            #여기 for loop에서 일단은 index에 해당하는 digits이 돌아가고 그것이 첫번쨰 loop가 된다. 그리고 나서 다음 recurisve하면 다음 index에 있는 
            #letter들이 뒤에 붙어진다

        if digits:
            dfs(0, "")

        return res
