-- Load department lookup table
INSERT INTO department (department_id, department_nm) 
SELECT ROW_NUMBER() OVER (ORDER BY department_nm), department_nm FROM (SELECT DISTINCT department_nm FROM proj_stg) d;

-- Load location lookup table
INSERT INTO location (location_id, location_name, address, city, state) 
SELECT ROW_NUMBER() OVER (ORDER BY location, address, city, state), location, address, city, state FROM (SELECT DISTINCT location, address, city, state FROM proj_stg) l;

-- Load education level lookup table
INSERT INTO education_level (education_level_id, education_level) 
SELECT ROW_NUMBER() OVER (ORDER BY education_lvl), education_lvl FROM (SELECT DISTINCT education_lvl FROM proj_stg) e;

-- Load job lookup table
INSERT INTO job (job_id, job_title) 
SELECT ROW_NUMBER() OVER (ORDER BY job_title), job_title FROM (SELECT DISTINCT job_title FROM proj_stg) j;

-- Load employee table
INSERT INTO employee (emp_id, emp_nm, email_address, hire_dt, department_id, location_id, education_level_id, manager_id) 
SELECT DISTINCT ON (s.emp_id) s.emp_id, s.emp_nm, s.email, s.hire_dt, d.department_id, l.location_id, e.education_level_id, m.emp_id AS manager_id 
FROM proj_stg s JOIN department d ON s.department_nm = d.department_nm JOIN location l ON s.location = l.location_name AND s.address = l.address AND s.city = l.city 
AND s.state = l.state JOIN education_level e ON s.education_lvl = e.education_level LEFT JOIN (SELECT DISTINCT emp_id, emp_nm FROM proj_stg) m ON s.manager = m.emp_nm 
ORDER BY s.emp_id, s.start_dt DESC;

-- Load employee salary table
INSERT INTO employee_salary (salary_id, emp_id, salary_amount, start_date, end_date) 
SELECT ROW_NUMBER() OVER (ORDER BY emp_id, start_dt), emp_id, salary, start_dt, end_dt FROM proj_stg;

-- Load employee job history table
INSERT INTO employee_job_history (job_history_id, emp_id, job_id, start_date, end_date) 
SELECT ROW_NUMBER() OVER (ORDER BY s.emp_id, s.start_dt), s.emp_id, j.job_id, s.start_dt, s.end_dt FROM proj_stg s JOIN job j ON s.job_title = j.job_title;

-- Validation checks
SELECT * FROM department;
SELECT * FROM location;
SELECT * FROM education_level;
SELECT * FROM job;
SELECT * FROM employee LIMIT 10;
SELECT * FROM employee_salary LIMIT 10;
SELECT * FROM employee_job_history LIMIT 10;