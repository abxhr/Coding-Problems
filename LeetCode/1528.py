class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)
        str = ''
        for i in range(len(s)):
            str += s[indices.index(i)]
        return(str)