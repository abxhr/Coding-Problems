class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = []
        for i in nums:
            c = 0
            for j in nums:
                if j < i:
                    c += 1
            lst.append(c)
        return(lst)