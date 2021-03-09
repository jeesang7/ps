class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = {}
        for n in nums:
            if n in table.keys():
                table[n] = True
            else:
                table[n] = False
        
        for key, val in table.items():
            if val == False:
                print(key)
                return key

    
    def aprch1_list_operation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
    
    
    def aprch2_hashtable(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i
            
    
    def aprch3_math(self, nums):
        """
        2∗(a+b+c)−(a+a+b+b+c)=c
        
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
    
    
    def aprch4_bit_manipulation(self, nums):
        """
        Concept
        - If we take XOR of zero and some bit, it will return that bit
        a⊕0=a
        
        - If we take XOR of two same bits, it will return 0
        a⊕a=0

        - a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        So we can XOR all bits together to find the unique number.
        
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a