f = open("one.txt", "r+") #file Object modes :  r,w,
f.write("123")

data = f.read() # readline() to read the content line by line 
print(data)

# f.write("Bharat mata ki jai\n Vasudev")
f.close()