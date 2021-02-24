# Author: Abshar Mohammed Aslam, github.com/abxhr

DELETE from Person WHERE ID not in (Select * from (select min(p.Id) from Person p group by p.email) temp);