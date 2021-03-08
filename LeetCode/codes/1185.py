# Author: Abshar Mohammed Aslam, github.com/abxhr

import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day_date = datetime.date(year, month, day)
        return day_date.strftime("%A")