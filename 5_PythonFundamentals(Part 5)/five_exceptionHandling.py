try:
    x = int(input("enter x: "))
    ans = 10/x
except ZeroDivisionError :
    print("Division by zero is not allowed")
except ValueError:
    print(f"Invalid input")

else:
    print(f"ans ={ans}")
finally:
    print("This is the end of the program")