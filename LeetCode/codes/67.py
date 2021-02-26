# Author: Abshar Mohammed aSlam ,github.com/abxhr

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return (bin(int(a,2) + int(b,2)).replace("0b",""))