# Author: Abshar Mohammed Aslam, github.com/abxhr

SELECT FirstName, LastName, City, State from Person LEFT JOIN Address USING (PersonId);