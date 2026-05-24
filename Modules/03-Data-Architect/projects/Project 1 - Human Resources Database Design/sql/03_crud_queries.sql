-- Question 1
SELECT e.emp_id, e.emp_nm, j.job_title, d.department_nm FROM employee e JOIN employee_job_history ejh ON e.emp_id = ejh.emp_id JOIN job j ON ejh.job_id = j.job_id JOIN department d ON e.department_id = d.department_id ORDER BY e.emp_nm;

-- Question 2
INSERT INTO job (job_id, job_title) VALUES (999, 'Web Programmer');
SELECT * FROM job WHERE job_id = 999;

-- Question 3
UPDATE job SET job_title = 'Web Developer' WHERE job_id = 999;
SELECT * FROM job WHERE job_id = 999;

-- Question 4
DELETE FROM job WHERE job_id = 999;
SELECT * FROM job WHERE job_id = 999;

-- Question 5
SELECT d.department_nm, COUNT(e.emp_id) AS total_employees FROM department d JOIN employee e ON d.department_id = e.department_id GROUP BY d.department_nm ORDER BY total_employees DESC;

-- Question 6
SELECT e.emp_nm AS employee_name, j.job_title, d.department_nm, m.emp_nm AS manager_name, ejh.start_date, ejh.end_date FROM employee e JOIN employee_job_history ejh ON e.emp_id = ejh.emp_id JOIN job j ON ejh.job_id = j.job_id JOIN department d ON e.department_id = d.department_id LEFT JOIN employee m ON e.manager_id = m.emp_id WHERE e.emp_nm = 'Toni Lembeck';