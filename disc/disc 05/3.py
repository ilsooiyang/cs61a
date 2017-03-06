class Instructor:
    degree = "PhD"
    def __init__(self, name):
        self.name = name

    def lecture(self, topic):
        print("Today we're learning about " + topic)

denero = Instructor("Professor DeNero")

class Student:
    instructor = denero
    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        ta.add_student(self)

    def attend_lecture(self, topic):
        Student.instructor.lecture(topic)
        print(Student.instructor.name + " is awesome!")
        self.understanding += 1

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class TeachingAssistant:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

alvin = TeachingAssistant("Alvin")
michelle = Student("Michelle", alvin)
michelle.attend_lecture("OOP")

kristin = Student("Kristin", alvin)
kristin.attend_lecture("trees")

kristin.visit_office_hours(TeachingAssistant("Luise"))

print(michelle.understanding)
print(alvin.students["Kristin"].understanding)

Student.instructor = Instructor("Professor Hilfinger")
Student.attend_lecture(michelle, "lists")

