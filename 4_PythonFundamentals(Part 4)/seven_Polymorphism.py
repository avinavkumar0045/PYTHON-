class Employee:
    def get_designation(self):
        print("designation : Employee")

class Teacher(Employee):
    def get_designation(self): #fxn overridding
        print("designation : Teacher")

t1= Teacher()
t1.get_designation()

#Duck type (similar work in both and also unrellated so duck typing)
class Accountant:
    def get_designation(self):
        print("designation : Accountant")

class Clerk():
    def get_designation(self): #fxn overridding
        print("designation : Clerk")

a1 = Accountant()
a1.get_designation()

c1 = Clerk()
c1.get_designation()