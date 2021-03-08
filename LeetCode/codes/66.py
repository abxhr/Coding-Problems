# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join([str(i) for i in digits])) + 1
        return [int(i) for i in list(str(number))]