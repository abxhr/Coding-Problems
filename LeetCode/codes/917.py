# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = []
        ans = ''
        j = 0
        for i in S:
            if i.isalpha():
                letters.append(i)
        letters = letters[::-1]
        for i in S:
            if i.isalpha():
                ans += letters[j]
                j += 1
            else:
                ans += i
        return ans
