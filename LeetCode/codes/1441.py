# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        for i in range(1, target[-1]+1):
            if i in target:
                res.append("Push")
            else:
                res.append("Push")
                res.append("Pop")
        return res