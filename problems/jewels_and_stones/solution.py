class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:        
        output = 0
        
        jewels_set = set(jewels)
        
        for stone in stones:
            if stone in jewels_set:
                output += 1
        
        return output
