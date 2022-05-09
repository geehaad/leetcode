# Write your MySQL query statement below
UPDATE Salary
SET Sex = 
    CASE WHEN sex = 'f' then 'm'
         ELSE "f"
    END 