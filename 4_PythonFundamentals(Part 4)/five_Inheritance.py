class Employee:
    start_time = "10am"
    end_time = "6pm"

class Teacher(Employee): #inheritance
    def __init__(self,subject):
        self.subject = subject

t1 = Teacher("Math")
print(t1.subject , t1.start_time ,t1.end_time)


#Multiple Inheritance
class master:
    def __init__(self,salary):
        self.salary = salary

class student:
    def __init__(self,gpa):
        self.gpa = gpa

class TA(master , student):
    def __init__(self, salary,gpa,name):
        super().__init__(salary) #no need to pass self as we are using super keyword
        student.__init__(self,gpa)
        self.name = name

ta1 = TA(15_000,9.3,"water")
print(ta1.name,ta1.gpa,ta1.salary)