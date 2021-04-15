class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        # print(set_nums, len(set_nums))
        
        if len(set_nums) != len(nums):
            return True
        else:
            return False