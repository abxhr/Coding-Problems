# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(list('aeiouAEIOU'))
        s = list(s)
        ptr1, ptr2 = 0, len(s)-1
        while ptr1 < ptr2:
            if s[ptr1] in vowels and s[ptr2] in vowels:
                s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                ptr1 += 1
                ptr2 -= 1
            if s[ptr1] not in vowels:
                ptr1 += 1
            if s[ptr2] not in vowels:
                ptr2 -= 1
        return ''.join(s)
