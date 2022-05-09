# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

delete from Person
where id in 
(select id from (select a.id from Person a, Person b where a.email = b.email and a.id > b.id) as p);


