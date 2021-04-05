# Author: Absahr Mohammed Aslam, github.com/abxhr

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = defaultdict(int)
        for i in s:
            letters[i] += 1
        for j in t:
            if not j in letters:
                return j
            else:
                letters[j] -= 1
                if letters[j] == 0:
                    letters.pop(j)
        return ""
