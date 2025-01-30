-- SQL Exercises (With Answers)

-- 1. Retrieve all students who enrolled in 2023.
SELECT * 
FROM students
WHERE EnrollmentDate LIKE '2023%';

-- 2. Find students whose email contains 'gmail.com'.
SELECT * 
FROM students
WHERE Email LIKE '%gmail.com';

-- 3. Count how many students are enrolled in the database.
SELECT COUNT(StudentID)
FROM students

-- 4. Find students born between 2000 and 2005.
SELECT *
FROM students
WHERE DateOfBirth >= '2000-1-1' AND  DateOfBirth <= '2005-12-31';

-- 5. List students sorted by last name in descending order.
SELECT *
FROM students
ORDER BY LastName DESC;

-- 6. Find the names of students and the courses they are enrolled in.
SELECT s.FirstName, s.LastName, c.CourseName 
FROM Students s, Courses c, Enrollments e
WHERE e.StudentID = s.StudentID AND e.CourseID = c.CourseID;


-- 7. List all students and their courses, ensuring students without courses are included (LEFT JOIN).
SELECT s.FirstName, s.LastName, c.CourseName 
FROM Students s
LEFT JOIN Enrollments e ON s.StudentID = e.StudentID 
LEFT JOIN Courses c ON e.CourseID = c.CourseID;

-- 8. Find all courses with no students enrolled (LEFT JOIN).
SELECT c.CourseName
FROM Courses c
LEFT JOIN Enrollments e ON c.CourseID = e.CourseID
WHERE e.StudentID IS NULL;





-- 10. List courses and show the number of students enrolled in each course.
SELECT c.CourseName, COUNT(e.StudentID) AS NumberOfStudents
FROM Courses c
LEFT JOIN Enrollments e ON c.CourseID = e.CourseID
GROUP BY c.CourseName;


