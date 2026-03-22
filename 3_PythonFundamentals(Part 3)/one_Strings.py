word = "python"
print("THe lenght of the word is : ", len(word))
print(word[2])

word2 = "water"
#concatenation
print(word + word2)

#slicing
print(word[0  : 3])
print(word[-4:-2]) #in reverse start indexing from -1 from the end of the string

#String formating 

#normal formating
a =4
b = 3
sum  = a+b
print("language is {}".format("python"))
print("sum of {} and {} is {} ".format(a , b , sum))

#index based formatiing
print("sum of {} and {} is {} ".format(a , b , sum))
print("sum of {1} and {0} is {2} ".format(a , b , sum))

#value based formatting
print("values of vars {c} and {d} ".format(c=5 , d = 4))

#f-string
print(f"Sum of {a} and {b} is {a+b}")
