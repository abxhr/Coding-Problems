# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [i for i in nums if i % 2 == 0]
        odd = [i for i in nums if i % 2 == 1]
        return [even.pop() if i % 2 == 0 else odd.pop() for i in range(len(nums))]