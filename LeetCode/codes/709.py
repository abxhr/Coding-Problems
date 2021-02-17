# Author: Abshar Mohammed Aslam, github.com/abxhr
 
class Solution:
    def toLowerCase(self, str: str) -> str:
        nstr = ''
        for i in str:
            val = ord(i)
            if 65 <= val <= 90:
                nstr += chr(val+32)
            else:
                nstr += chr(val)
        return nstr