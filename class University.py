class University:
    def __init__(self):
        self.studentName = 'Asasira'
        self.courseUnit = 'English'
        self.lecturerName = 'Mr. Kamugisha'
    def students(self): #function definition for students
        return f"Student Name:{''.join(self.studentName)}"
    def courses(self): #function definition for courses
        return f"Course Unit:{''.join(self.courseUnit)}"
    def lecturers(self): #function definition for lecturers
        return f"Lecturer' Name:{''.join(self.lecturerName)}"
new = University()
print(new.students())
print(new.courses())
print(new.lecturers())
