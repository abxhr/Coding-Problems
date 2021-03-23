# Author: Abshar Mohammed Aslam, github.com/abxhr

SELECT a.Name as Employee FROM Employee a, Employee b WHERE a.ManagerId = b.ID and a.Salary > b.Salary;