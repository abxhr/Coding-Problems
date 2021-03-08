# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = {}
        sum = 0
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        for num, count in counts.items():
            if count == 1:
                sum += num
        return sum