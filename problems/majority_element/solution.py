class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = {}
        
        for n in set(nums):
            table[str(n)] = 0
        
        for n in nums:
            table[str(n)] += 1
            
        max = 0
        for key, val in table.items():
            if max < val:
                max = val
                majority_element = key
        
        return majority_element
        