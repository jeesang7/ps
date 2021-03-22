class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Time complexity: O(n)
        Spece complexity: O(1)
        '''
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                # print(hare)
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            print(hare)
        
        return hare
    
        '''
        Bad case: Time Limit Exceeded
        idx = 0
        
        while True:
            if idx == len(nums):
                # print('none', idx)
                break
            else:
                target = nums[idx]
                # print(target)
                i = 0
                
            for n in nums:
                if idx == i:
                    # print(idx, i, target)
                    i += 1
                    continue
                if target == nums[i]:
                    # print(target)
                    return target
                i += 1
            
            idx += 1
        '''