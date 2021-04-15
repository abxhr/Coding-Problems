# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0]
        for i in range(1, num+1):
            bits.append(bits[i//2] + i % 2)
        return bits
