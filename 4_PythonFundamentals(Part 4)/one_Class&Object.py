class Student :    #🌟🌟🌟🌟 IN PYTHON CANNOT CREATE MULTIPLE CONSTRUCTOR WITHIN SAME CLASS
    sub = "Hindi"
    college = "ABC"
    year = "4th year"

    # @staticmethod # if dont define it static then have to type "self" within in the parameter of the fxn
    # def __init__(self): #default constructor
    #     print("Default constructor")

    def __init__(self,name):#Parameterised constructor
        print("Parameterised constructor")
        self.name = name
    
   
    

stu1  = Student("Avinav") #object creation
print(stu1.sub , stu1.year)
print(stu1.name)

stu2 = Student("TIGER")