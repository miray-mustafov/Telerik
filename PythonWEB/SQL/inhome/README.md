<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# SQL - Tasks

## Instructions

1. Start your favourite SQL Client and create new database "TelerikAcademy", using the [provided script](database_telerikacademy.sql)
1. Connect to the database "TelerikAcademy" and examine the major tables.
1. Use the "TelerikAcademy" database for all tasks.
1. Happy querying :)


## Tasks

1. Write a SQL query to find all information about all departments (use "TelerikAcademy" database).
1. Write a SQL query to find all department names.
1. Write a SQL query to find the salary of each employee.
1. Write a SQL to find the full name of each employee.
1. Write a SQL query to find the email addresses of each employee (by his first and last name). Consider that the mail domain is telerikacademy.com. Emails should look like “John.Doe@telerikacademy.com". The produced column should be named "Full Email Addresses".
1. Write a SQL query to find all different employee salaries.
1. Write a SQL query to find all information about the employees whose job title is “Sales Representative“.
1. Write an SQL query to find all employees whose salary is bigger than their manager's.
1. Write a SQL query to find the names of all employees whose first name starts with "SA".
1. Write a SQL query to find the names of all employees whose last name contains "ei".
1. Write a SQL query to find the salary of all employees whose salary is in the range [20000…30000].
1. Write a SQL query to find the names of all employees whose salary is 25000, 14000, 12500 or 23600.
1. Write a SQL query to find all employees that do not have manager.
1. Write a SQL query to find the names of all employees who are hired before their managers.
1. Write a SQL query to find all employees that have salary more than 50000. Order them in decreasing order by salary.
1. Write a SQL query to find the top 5 best paid employees.
1. Write a SQL query to find all employees and their address.
1. Write a SQL query to find all employees whose MiddleName is the same as the first letter of their town.
1. Write a SQL query to find all employees that have manager, along with their manager.
1. Write a SQL query to find all employees that have manager, along with their manager and their address.
1. Write a SQL query to find all departments and all town names as a single list.
1. Write a SQL query to find all the employees and the manager for each of them along with the employees that do not have manager.
1. Write a SQL query to find the names of all employees from the departments "Sales" and "Finance" whose hire year is between 1995 and 2005.

## Activity walk through

Some tasks require you to search additional information.

1. Task 4: "Write a SQL to find the full name of each employee."

   - [MySQL concat](http://www.mysqltutorial.org/sql-concat-in-mysql.aspx)
   - [Concat with null values](http://www.mysqltutorial.org/mysql-ifnull/). Consider what fields may and my not have null values.

1.  Task 16: "Write a SQL query to find the top 5 best paid employees."

    - [MySQL limit](http://www.mysqltutorial.org/mysql-limit.aspx)

1. Task 18: "Write a SQL query to find all employees whose MiddleName is the same as the first letter of their town."

   - [MySQL left() funtion](https://www.w3schools.com/sql/func_mysql_left.asp)
