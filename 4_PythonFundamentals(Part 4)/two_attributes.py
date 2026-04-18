class Student :
    college_name = "ABC college" #class attributes(same for all objects ) 
    height = 5.7

    def __init__(self , name,height):#instance attribute(might be different for all attributes )
        self.name = name
        self.height = height

std1 = Student("tiger",5.75)
print(std1.college_name)
print(Student.college_name)

print(std1.name)

print(std1.height)
print(Student.height)
