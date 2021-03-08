# Author: Abshar Mohammed Aslam, github.com/abxhr

SELECT Name AS Customers FROM Customers WHERE Id NOT IN (SELECT DISTINCT CustomerID FROM orders);