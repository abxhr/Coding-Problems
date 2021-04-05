# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lsto = []
        l = len(arr)
        for i in set(arr):
            c = 1
            for j in range(l):
                if i == arr[j] and arr[j] != 1001:
                    c += 1
                    arr[j] = 1001
            lsto.append(c)
        lsto.sort()
        chk = list(set(lsto))
        chk.sort()
        if lsto == chk:
            return True
        else:
            return False
