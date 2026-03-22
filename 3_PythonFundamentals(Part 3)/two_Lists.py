marks = [99,99,34,32,"ada",2,7]
print(type(marks))
#slicing
ans = marks[0: 3]
print(ans)

marks.append(5)
print(marks)
ans.sort(reverse=True)
print(ans)

#Loops
idx =0
for val in marks:
    if(val == 32):
        print(idx)
        break
     
    idx = idx+1