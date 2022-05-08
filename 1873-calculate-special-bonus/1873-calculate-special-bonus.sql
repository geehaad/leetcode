# Write your MySQL query statement below
SELECT employee_id,  
CASE WHEN (employee_id % 2 != 0) AND (name not like "M%" ) THEN salary
ELSE salary = 0
END AS "bonus"
FROM Employees


