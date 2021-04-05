# Author: Absahr Mohammed Aslam, github.com/abxhr

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        line = 0
        for i in s:
            line += widths[ord(i)-ord('a')]
            if line > 100:
                lines += 1
                line = widths[ord(i)-ord('a')]
        return [lines, line]
