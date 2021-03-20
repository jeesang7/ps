from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # print(Counter(s), Counter(t))
        if Counter(s) == Counter(t):
            return True
        else:
            return False
        