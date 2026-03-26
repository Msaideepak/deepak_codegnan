'''
print(9+8)
print("python"+ "language")
print([1,2} + [3,4])

concatenation
-------------
this is nothing but, a (+) behavi..
case_1
------
intergers--- this will act as addition for the int

case_2
can only concatenate str (not "list"0 to str
for others datatypes (we have use same type) this (+) act as concatenate
------



tuple()--->
-------
is a collacation of different datatype and this is represented by parathesis ()
#and seperated by comma ,
Thing = (1,"deepak",[12,4],(6,7))
print(Thing)
Thing=(12,89, "python", (23, "deepak", "python is a language",[(7,8)], [8, ("python", [34, 9])]))
print(Thing[3][2][1])
print(thing)
num = 9
num_2 = 90
print(f"before swapping num ={num} and num_2 = {num_2}")
num, num_2 = num_2, num
print(f"after swapping num = {num} and num_2 = {num_2}")'''

leap_year = int(input("enter year: "))
if (leap_year % 4 == 0 and leap_year % 100 != 0)or leap_year % 400 == 0:
    print(f"yes, {leap_year} is a leap year")
else:
    print(f"no, {leap_year} is not leap year")

     
