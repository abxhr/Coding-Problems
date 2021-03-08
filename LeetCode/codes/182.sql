# Author: Abshar Mohammed Aslam, github.com/abxhr

SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email)>1;