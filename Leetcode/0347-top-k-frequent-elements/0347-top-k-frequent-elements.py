class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        hashmap = { i:[] for i in range(len(nums)+1) }

        for n in nums:
            count[n] = 1 + count.get(n,0)


        "[1:3, 2:2, 3:1]"
        for key, value in count.items():
            if value not in hashmap:
                hashmap[value] = [key]
            else:
                hashmap[value].append(key)
        
        res = []
        for i in range(len(hashmap)-1, -1, -1):
            for j in hashmap[i]:
                if k > 0:
                    res.append(j)
                    k -= 1
        
        return res