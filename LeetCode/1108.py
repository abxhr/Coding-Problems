# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
