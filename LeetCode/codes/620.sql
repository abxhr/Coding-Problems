# Author: Abshar Mohammed Aslam, github.com/abxhr

SELECT * FROM cinema WHERE (id%2!=0) AND (description NOT LIKE '%boring%') ORDER BY rating DESC;  