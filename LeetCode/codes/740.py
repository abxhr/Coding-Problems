# Author: Abshar Mohammed Aslam, github:@abxhr

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        prev = curr = 0
        check = 0
        for num in sorted(counts):
            earn = counts[num] * num
            if num - 1 == check:
                prev, curr = curr, max(prev+earn, curr)
            else:
                prev, curr = curr, curr+earn
            check = num
        return curr