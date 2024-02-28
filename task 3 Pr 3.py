class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Хелоу, Мене звати {self.name}"

class Student(Person):
    def in_student(self):
         return True

student = Student("Serioja")
print(student.greet())          
print(f"Seryyoja є студентом:{student.in_student()}") 




