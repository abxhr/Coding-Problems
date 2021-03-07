# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = list()
        distance = len(s) - 1
        for letter in s:
            if letter != c:
                distance += 1 
            else:
                distance = 0
            ans.append(distance)
        for i in range(len(s) - 2, -1, -1):
            ans[i] = min(ans[i], ans[i + 1] + 1)
        return ans