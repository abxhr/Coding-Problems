class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = 0
        for i in range(len(nums)):
            for j in nums[i+1:]:
                if nums[i] == j:
                    n += 1
        return n