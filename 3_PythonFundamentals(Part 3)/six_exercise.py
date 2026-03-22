info = [
    ("alice","Math"),
    ("sa","Sci"),
    ("alice","Phy"),
    ("na","Eng"),
    ("sa","Math"),
    ("na","Sci"),
]

unique_sub = set()
english= []
for tup in info:
    unique_sub.add(tup[1])#for unique subjects
    if(tup[1] == "Eng"): #for the english students
        english.append(tup[0])
print(unique_sub)
print(english)

#part 3 create a dict of students with the courses they are eunrooled in

dict = {}

for name, course in info:
    if(dict.get(name) == None):
        dict.update({name: set()}) #{} for dict 
        dict[name].add(course)
    else :
        dict[name].add(course)  

print(dict)
