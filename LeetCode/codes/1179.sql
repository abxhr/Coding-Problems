# Author: Abshar Mohammed Aslam, github.com/abxhr

SELECT id,
SUM(CASE WHEN month='Jan' THEN revenue ELSE null END) Jan_Revenue,
SUM(CASE WHEN month='Feb' THEN revenue ELSE null END) Feb_Revenue,
SUM(CASE WHEN month='Mar' THEN revenue ELSE null END) Mar_Revenue,
SUM(CASE WHEN month='Apr' THEN revenue ELSE null END) Apr_Revenue,
SUM(CASE WHEN month='May' THEN revenue ELSE null END) May_Revenue,
SUM(CASE WHEN month='Jun' THEN revenue ELSE null END) Jun_Revenue,
SUM(CASE WHEN month='Jul' THEN revenue ELSE null END) Jul_Revenue,
SUM(CASE WHEN month='Aug' THEN revenue ELSE null END) Aug_Revenue,
SUM(CASE WHEN month='Sep' THEN revenue ELSE null END) Sep_Revenue,
SUM(CASE WHEN month='Oct' THEN revenue ELSE null END) Oct_Revenue,
SUM(CASE WHEN month='Nov' THEN revenue ELSE null END) Nov_Revenue,
SUM(CASE WHEN month='Dec' THEN revenue ELSE null END) Dec_Revenue
FROM Department
GROUP BY id
ORDER BY id;