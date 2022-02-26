# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def romanToInt(self, s: str) -> int:
        equiv = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        actual = 0
        
        for place in range(len(s)):
            if (place <= len(s) - 2) and (equiv[s[place]] < equiv[s[place + 1]]):
                actual -= equiv[s[place]]
            else:
                actual += equiv[s[place]]
        return actual