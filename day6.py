'''String --> String is a collaction of char, which represter
by " " or '' and we can access the using indexing (string can also allow negative indexing)and aslo
slicing. this also immutable, where i could not able to modified on the vari...
any = 'Python Programming'
print(any[20])
so = any.replace("Python","Java")
print(any)
print(so)


len()--- len() method is used to get char present in the string
or find the length of the string


a_day =("I'm Deepak from Kotavalasa, Have 3+ years of Exp as ") 
print(f"my name is {a_day[4:10]}
print(f"my name is {a_day[1:39]}

reverse
day = 'deepak'
print(day[::-1])

#integer convrt the strings, if the contain only integers valus ....
some = "123"
num = int(some)
print(type(num)
note [methods of string
#----------
split()--->remove space, and the is in the list[]it will give
the separated thing in each index

systax---->variable_split("substring")

lower()--->this is used to all convert into lower case

'''
some= "python is a programming language"
print(some.split(" "))

some= "python is a programming language"
print (some.split("progamming"))

some= "python is a programming language"
print(some.lower())

some= "python is a programming language"
print(some.upper())
'''
upper()--->

replace()--->this is used to replace old str with the new str
sytax---> variable_name.replace("old string","new string")

some = "python is a progamming language"
print(some.replace("programming","nrml"))'''


some = "python is a programming language"
if "ythn" in some:
    print("yes")
else:
    print("No")

