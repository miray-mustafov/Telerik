-- SELECT * FROM employees;
-- Select the managers only?
SELECT *
FROM employees
WHERE EmployeeID IN (SELECT DISTINCT ManagerID FROM employees WHERE ManagerID IS NOT NULL);

SELECT * FROM departments;
SELECT Name FROM departments;
SELECT EmployeeID, FirstName, LastName, Salary FROM employees;
SELECT CONCAT(FirstName, ' ', LastName) AS Full_Name FROM employees;
SELECT CONCAT(FirstName, '.', LastName, '@telerikacademy.com') AS Full_Email_Addresses FROM employees;
SELECT DISTINCT Salary FROM employees;
SELECT * FROM employees WHERE JobTitle = 'Sales Representative';
SELECT e.* FROM employees e
JOIN employees m ON e.ManagerID = m.EmployeeID
WHERE e.Salary > m.Salary;
SELECT * FROM employees WHERE FirstName LIKE 'SA%';
SELECT * FROM employees WHERE LastName LIKE '%ei%';
SELECT * FROM employees WHERE Salary BETWEEN 20000 AND 30000;
SELECT * FROM employees WHERE Salary IN (25000, 14000, 12500, 23600);
SELECT * FROM employees WHERE ManagerID IS NULL;
SELECT e.* FROM employees e
JOIN employees m ON e.ManagerID = m.EmployeeID
WHERE e.HireDate < m.HireDate;
SELECT * FROM employees
WHERE Salary > 50000 ORDER BY Salary DESC;
SELECT * FROM employees ORDER BY Salary DESC LIMIT 5;
SELECT e.*, a.AddressText FROM employees e
JOIN addresses a ON e.AddressID = a.AddressID;
SELECT e.*
FROM employees e
JOIN addresses a ON e.AddressID = a.AddressID
JOIN towns t ON a.TownID = t.TownID
WHERE e.MiddleName = LEFT(t.Name, 1);
SELECT e.*, m.FirstName AS Manager_FirstName, m.LastName AS Manager_LastName
FROM employees e
JOIN employees m ON e.ManagerID = m.EmployeeID;
SELECT e.*, m.FirstName AS Manager_FirstName, m.LastName AS Manager_LastName, a.AddressText
FROM employees e
JOIN employees m ON e.ManagerID = m.EmployeeID
JOIN addresses a ON m.AddressID = a.AddressID;
SELECT Name AS Department_Town
FROM departments
UNION
SELECT Name
FROM towns;
SELECT e.*, m.FirstName AS Manager_FirstName, m.LastName AS Manager_LastName
FROM employees e
LEFT JOIN employees m ON e.ManagerID = m.EmployeeID;
SELECT e.*
FROM employees e
JOIN departments d ON e.DepartmentID = d.DepartmentID
WHERE d.Name IN ('Sales', 'Finance')
AND YEAR(e.HireDate) BETWEEN 1995 AND 2005;
