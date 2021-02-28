# Author: Abshar Mohammed Aslam, github.com/abxhr

SELECT MAX(Salary) AS SecondHighestSalary FROM Employee WHERE Salary < (SELECT MAX(Salary) FROM Employee)