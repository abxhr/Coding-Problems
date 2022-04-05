# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -float("inf")
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num == max1:
                continue
            elif num > max2:
                max2, max3 = num, max2
            elif num == max2:
                continue
            elif num > max3:
                max3 = num
        if max3 == -float("inf"):
            max3 = max1
        return max3
