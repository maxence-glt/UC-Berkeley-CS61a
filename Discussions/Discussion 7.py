# Discussion 7 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/disc07.pdf

# 1.1
class Student:
    students = 0 # this is a class attribute
    def __init__(self, name, ta):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        ta.add_student(self)
    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}
    def add_student(self, student):
        self.students[student.name] = student
    def assist(self, student):
        student.understanding += 1

snape = Professor("Snape")
harry = Student("Harry", snape)

harry.visit_office_hours(snape)

harry.visit_office_hours(Professor("Hagrid"))

print(harry.understanding)

print([name for name in snape.students])

x = Student("Hermione", Professor("McGonagall")).name

print(x)

print([name for name in snape.students])
