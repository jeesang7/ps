class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:        
        output = 0
        
        for stone in stones:
            for jewel in jewels:
                if stone == jewel:
                    output += 1                
        
        return output
