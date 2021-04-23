# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = []
        for d in number:
            if d.isdigit():
                digits.append(d)
        ans = ""
        while digits:
            if len(digits) > 4:
                ans += "".join(digits[:3])
                digits = digits[3:]
            elif len(digits) >= 2 and len(digits) != 4:
                ans += "".join(digits[:len(digits)])
                digits = []
            else:
                ans += "".join(digits[:2]) + "-" + "".join(digits[2:])
                digits = []
            ans += "-"
        return ans.strip("-")
            