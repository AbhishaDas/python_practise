"""Grades are computed using a weighted average. Suppose that the written test counts 70%,  lab exams 20% and assignments 10%.
If Arun has a score of
Written test = 81
Lab exams = 68
Assignments = 92
Arun’s overall grade = (81x70)/100 + (68x20)/100 + (92x10)/100 = 79.5
 Write a program to find the grade of a student during his academic year. 
Program should accept the scores for written test, lab exams and assignments
Output the grade of a student (using weighted average)
Eg:
Enter the marks scored by the students
Written test = 55
Lab exams = 73
Assignments = 87
Grade of the student is 61.8 """

def calculate_grade(written_test,lab_exam,assignment):
    grade= ((written_test*70)/100)+((lab_exam*20)/100)+((assignment*10)/100)
    return grade


print("Enter the marks scored by the students")
written_test=float(input("Written test: "))
lab_exam=float(input("Lab Exam: "))
assignment=float(input("Assignment: "))

grade=calculate_grade(written_test,lab_exam,assignment)
print("Grade of the student",grade)
