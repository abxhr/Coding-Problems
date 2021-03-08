# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        lst = []
        for i in rectangles:
            lst.append(min(i))
        return lst.count(max(lst))