# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        final_str = ""
        while columnNumber >  0:
            columnNumber -= 1
            curr = columnNumber % 26
            columnNumber = int(columnNumber/26)
            final_str += chr(65+curr)
        return final_str[::-1]
