1、内置：COLUMN_NAME、TABLE_NAME、information_schema
SELECT COLUMN_NAME FROM information_schema.`COLUMNS` WHERE TABLE_NAME = 't_user'

日志（二）
select distinct fileid from execution order by fileid desc limit 4,1
主要学习limit 4,1，是指返回5
如果limit 4,2，返回5,6

日志（一）
Select Person.FirstName, Person.LastName, Address.City, Address.State From Person left join Address where Person.PersonId = Address.AddressId;

SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person p LEFT OUTER JOIN Address a USING (PersonId);

2、SELECT dept_name, IFNULL(student_number,0) AS student_number FROM department
LEFT JOIN (SELECT dept_id,count(*) AS sttudent_number FROM student GROUP BY dept_id) t USING (dept_id) ORDER BY student_number DESC,dept_name

# 先按照人数从大到小排序，其次按照院系名称排序
ORDER BY student_number DESC,dept_name

3、顺序：
SELECT、dim、FROM、relation、whereClause、 groupBy、havingClause、 orderBy
SQL语句通过web工程的SQL拼接工具的书写有了深度地认识。

4、
Select Score , (Select distinct Score from Scores order by Score desc)
as Rank from Scores
order by Score desc

# COUNT(Ranking.Score) 都搞了这么久的count。哎
Select Scores.Score,COUNT(Ranking.Score) AS Rank
# 可以同时查两，不用 关联。这个触动我了
FRROM Sccores,(Select DISTINCT Score FROM Scores) Ranking

Where Scores.Score <= Ranking.Score
#  一定要有 GROUP BY？
GROUP BY Scores.Id,Scores.Score ORDER BY Scores.Score DESC;


