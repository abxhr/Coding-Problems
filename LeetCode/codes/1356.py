# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        binary_counts = []
        arr.sort()
        for val in arr:
            binary_counts.append(str(bin(val)).count('1'))
        return [y for x, y in sorted(zip(binary_counts, arr))]
