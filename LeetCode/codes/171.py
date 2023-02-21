# Author: Abshar Mohammed Aslam

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        col_number = 0
        for curr in columnTitle:
            col_number *= 26
            col_number += alpha.index(curr)
        return col_number
