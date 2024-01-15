class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window = len(s1)
        s1_counter = Counter(s1)

        for i in range(len(s2)-window+1):
            s2_counter = Counter(s2[i:i + window])
            if s1_counter == s2_counter:
                return True

        return False