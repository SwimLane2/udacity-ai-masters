
-- Create Department table
CREATE TABLE department (
    department_id INT PRIMARY KEY,
    department_nm VARCHAR(100)
);

-- Create Location table
CREATE TABLE location (
    location_id INT PRIMARY KEY,
    location_name VARCHAR(100),
    address VARCHAR(150),
    city VARCHAR(100),
    state VARCHAR(100)
);

-- Create Education Level table
CREATE TABLE education_level (
    education_level_id INT PRIMARY KEY,
    education_level VARCHAR(100)
);


-- Create Job table
CREATE TABLE job (
    job_id INT PRIMARY KEY,
    job_title VARCHAR(100)
);

-- Create Employee table
CREATE TABLE employee (
    emp_id VARCHAR(10) PRIMARY KEY,
    emp_nm VARCHAR(100),
    email_address VARCHAR(150),
    hire_dt DATE,
    department_id INT,
    location_id INT,
    education_level_id INT,
    manager_id VARCHAR(10)
);

-- Create Employee Salary table
CREATE TABLE employee_salary (
    salary_id INT PRIMARY KEY,
    emp_id VARCHAR(10),
    salary_amount DECIMAL(10,2),
    start_date DATE,
    end_date DATE
);

-- Create Employee Job History table
CREATE TABLE employee_job_history (
    job_history_id INT PRIMARY KEY,
    emp_id VARCHAR(10),
    job_id INT,
    start_date DATE,
    end_date DATE
);


-- Add foreign key between employee and department
ALTER TABLE employee
ADD CONSTRAINT fk_employee_department
FOREIGN KEY (department_id)
REFERENCES department(department_id);

-- Add foreign key between employee and location
ALTER TABLE employee
ADD CONSTRAINT fk_employee_location
FOREIGN KEY (location_id)
REFERENCES location(location_id);

-- Add foreign key between employee and education level
ALTER TABLE employee
ADD CONSTRAINT fk_employee_education
FOREIGN KEY (education_level_id)
REFERENCES education_level(education_level_id);

-- Add self-referencing foreign key for employee manager
ALTER TABLE employee
ADD CONSTRAINT fk_employee_manager
FOREIGN KEY (manager_id)
REFERENCES employee(emp_id);

-- Add foreign key between employee salary and employee
ALTER TABLE employee_salary
ADD CONSTRAINT fk_salary_employee
FOREIGN KEY (emp_id)
REFERENCES employee(emp_id);

-- Add foreign key between employee job history and employee
ALTER TABLE employee_job_history
ADD CONSTRAINT fk_job_history_employee
FOREIGN KEY (emp_id)
REFERENCES employee(emp_id);


-- Add foreign key between employee job history and job
ALTER TABLE employee_job_history
ADD CONSTRAINT fk_job_history_job
FOREIGN KEY (job_id)
REFERENCES job(job_id);