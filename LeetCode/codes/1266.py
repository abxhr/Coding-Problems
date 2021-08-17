# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        prev = points[0]
        for i in range(1, len(points)):
            time += max(abs(points[i][0]-prev[0]), abs(points[i][1]-prev[1]))
            prev = points[i]
        return time
