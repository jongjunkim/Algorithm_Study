class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        res = 0
        cache = {}
        def dfs(index, curamount):

            if curamount > amount:
                return 0
            if index == len(coins):
                return 0
            if curamount == amount:
                return 1
            if (index, curamount) in cache:
                return cache[(index, curamount)]
            
            cache[(index, curamount)] = dfs(index, curamount + coins[index]) + dfs(index+1, curamount)
            
            return cache[(index, curamount)]

        return dfs(0,0)