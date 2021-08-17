# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        lst = list(set([i[1] for i in paths]))
        for i in paths:
            if i[0] in lst:
                lst.remove(i[0])
        return lst[0]
