# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        blst = []
        greatest = candies[0]
        for i in candies:
            if i > greatest:
                greatest = i
        for i in candies:
            if i + extraCandies >= greatest:
                blst.append(True)
            else:
                blst.append(False)
        return blst
