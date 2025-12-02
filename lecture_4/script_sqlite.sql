-- Turn on foreign keys
PRAGMA foreign_keys = ON;


-- create table students
create table if not exists students (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	full_name TEXT NOT NULL,
	birth_year INTEGER NOT NULL
);


-- create table grades
CREATE TABLE IF NOT EXISTS grades (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	student_id INTEGER NOT NULL,
	subject TEXT NOT NULL,
	grade INTEGER NOT NULL CHECK (grade >= 1 AND grade <= 100), --check grades between 1 to 100
	FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);


-- insert data students
INSERT INTO students(full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);


-- insert data grades
INSERT INTO grades(student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'Math', 89),
(9, 'English', 96),
(9, 'Art', 92);


-- create indexes
CREATE INDEX IF NOT EXISTS idx_grades_student_id ON grades(student_id);
CREATE INDEX IF NOT EXISTS idx_grades_subject ON grades(subject);
CREATE INDEX IF NOT EXISTS idx_students_birth_year ON students(birth_year);


-- find all grades for a specific student (Alice Johnson).
SELECT students.full_name, grades.subject, grades.grade
FROM students 
JOIN grades ON grades.student_id = students.id
WHERE full_name = 'Alice Johnson';


-- calculate the average grade per sudents
SELECT students.full_name, Round(AVG(grade), 2) as avg_grades
FROM students 
JOIN grades on grades.student_id = students.id 
GROUP BY students.id, students.full_name;


-- list all students born after 2004
SELECT students.full_name 
FROM students 
WHERE students.birth_year > 2004;


-- create a query that lists all subjects and their average grades
SELECT subject, Round(AVG(grade), 2) as avg_grades 
FROM grades  
GROUP BY subject;


-- find the top 3 students with the highest average grades
SELECT students.full_name, Round(AVG(grade), 2) as avg_grades 
FROM students 
JOIN grades on grades.student_id = students.id
GROUP BY students.id, students.full_name 
ORDER BY avg_grades DESC 
LIMIT 3;


-- show all students who have scored below 80 in any subject
SELECT DISTINCT students.full_name
FROM students
JOIN grades ON grades.student_id = students.id
WHERE grade < 80;
