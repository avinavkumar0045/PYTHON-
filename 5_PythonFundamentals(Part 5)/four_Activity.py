# find the word in the given file and print the line in which it is
data = True
line = 1
with open("sample.txt","r") as f:

    while data :
        data = f.readline()
        if("most" in data):
            print(f"Word Found at line{line}")
            break

        line = line+1 


