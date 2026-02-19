print("Jai Shree Ram \nbolo Jai Shree Ram")
print("Sia var Ram chandra ki jai")

#variables
name = "Avinav"
_age = 35
PI = 3.14

#printing methods
print("my name is : ", name ," ", _age ," ", PI)
print("\n")
print(type(_age))

'''  tripple quotes are used for 
multiline comments '''

style_preffered  = "Snake Case "


#Arithmetic ops
a = 4
b = 3

sum = a+b
sub = a-b
mul = a*b
div = a / b

pow = a ** b

print(sum , sub , pow , sum == sub)

is_true = False
print(not is_true) # "not" operator

#explicit type casting 
print ( int(5+ 10.2)) 

val = bool(12) # False = 0
print(val)

#TAKING INPUT

input1 = int( input("Enter a value : ")) # or else it will do concatenation
input2 = int (input("Enter a value : "))
print( (input1 + input2 ) / 2)

decimal_num = float( input( "Enter a decimal number : "))
print( int ( decimal_num))
print(decimal_num  - int(decimal_num))