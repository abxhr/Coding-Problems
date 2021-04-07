# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length = len(students)
        cycle = 0
        while length != cycle:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                length = len(students)
                cycle = 0
            else:
                back = students[0]
                students.pop(0)
                students.append(back)
                cycle += 1
        return cycle
