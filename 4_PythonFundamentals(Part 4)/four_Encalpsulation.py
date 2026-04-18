class BankAccount :
    def __init__(self , name , balance,age):
        self.name = name #public
        self._balance = balance  #PROTECTTED with the help of "_"
        self.__age = age #private with the help of "__"

    def get_age(self):#getter
        print(f"The age is : {self.__age}")
    
    def set_age(self,value):#setter
        self.__age = value
        print("Value is changed")

acc1 = BankAccount("Ram",10_000,32)

print(acc1.name , acc1._balance , acc1._BankAccount__age) #this shows that protected in python is just convention not enforced
acc1.get_age()
acc1.set_age(24)
acc1.get_age()
