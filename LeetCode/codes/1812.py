# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alpha = "abcdefgh"
        nums = "12345678"
        pos = alpha.index(coordinates[0]) + nums.index(coordinates[1]) + 2
        if pos % 2:
            return True
        return False
