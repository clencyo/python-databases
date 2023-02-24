from main import Student

mystudent = Student.select()
for user in mystudent:
    print(Student.student_name,Student.student_id,Student.student_class)