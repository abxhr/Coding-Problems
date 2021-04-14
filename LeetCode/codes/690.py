# Author: Abshar Moahmmed Aslam, github.com/abxhr

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        imp_list = {x.id: x for x in employees}
        tot_imp = imp_list[id].importance
        subords = imp_list[id].subordinates
        while subords:
            pop_curr = subords.pop()
            subords.extend(imp_list[pop_curr].subordinates)
            tot_imp += imp_list[pop_curr].importance
        return tot_imp
