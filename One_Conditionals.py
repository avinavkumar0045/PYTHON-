age = 1
if(age >= 18):
    print("You can drive")
    print("You can vote")
else :
    print("You can't vote")

#match case in python
#color = input("Enter Color : ")
color = "Red"
match color :
     case "Green":
        print("Go")
     case "Red":
        print("Stop")
     case _:
        print("default Case")

word = "water"
for var in word : 
    print(var)

if 'a' in word :
    print("a is present")

#range

for i in range(1,5,2) :
    print(i)

#Functions

def sum( a, b =1): # definition of the function with default parameter
   s = a+b
   return s
ans  = sum( 2  ) #calling function , write the non default paramter first 
print(ans)

#Lambda function example
water = lambda a,b,c : a+b+c
print(water(7,3,2))

#ternary 
age =13
status="adult" if age > 18 else "not adult"
print(status)