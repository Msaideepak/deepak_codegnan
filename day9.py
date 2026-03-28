'''
we can store data as key : value
keys are union and we can only give immutable data types in type
keys
values--- we all data types (immutable and matable)
{}

methods
-------keys()this mesthod is used to get all keys from the dict
values()--- this method is used to get all values from the dict
clear()--- this method is used to delete the dict 

deepak = {"name":"deepak",
             45:89,(4,7):0}
print(deepak)

deepak = {"name":"deepak",
          "role":"mentor",
          "sal":5678}
print(deepak.keys())
print(deepak.values())
print(deepak.clear())
print(deepak)

set{}---> set data type is a unordered collection and is never allow duplication
methods
------
union--- this is used add or get 2 different sets without duplication
intersection---this method is used to find out common items from the 2 set
difference---this method is used to find

any = {1,2,3,4}
so = {4,5,6}
print(any.union(so))
print(any.intersection(so))
print(any.difference(any))
print(any.pop())
print("the removed inbox value:",any.pop())
#check weather user entered pin is write or wrong
correct_pin = ("1234")
user_ pin = input("enter pin:")
if user_pin in correct_pin:
print("correct pin")
else:
    print("wrong pin")
'''
some = "python is a programming language"
count_ = 0

for j in some:
    if j == " ":
        count_ += 1

print(count_)

