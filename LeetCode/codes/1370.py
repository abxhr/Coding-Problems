# Author: Abshar Mohammed Asam, github.com/abxhr

class Solution:
    def sortString(self, s: str) -> str:
        count = {}
        result = ''
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        chars = sorted(list(set(s))) 
        while(count):
            for char in chars:
                if char in count:
                    result += char
                    count[char] -= 1
                    if count[char] == 0:
                        del count[char]
            for char in chars[::-1]:
                if char in count:
                    result += char
                    count[char] -= 1
                    if count[char] == 0:
                        del count[char]
        return result