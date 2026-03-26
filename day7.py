'''Vowle_con = input("Enter a letter: ")
if Vowel_con in "AEIOUaeiou":
    print("Vow")
else:
     print("Con")

Time_aday = input("Enter 24 hours time: ")
Parts_ = Time_aday.split(":")
hours_ = int (Parts_[0])
Min_ = int(Parts_[1])
if hours_>=13 and Min_ < 60:
   print(f"{Time_aday} convert into {hours_ - 12}:{Min_}Pm")
else:
    print(f"You have entered nrml or Min are incorrect")

List--->Different types inside the [] , which are separted by,
Eg---> [1,"Name",[1,2,""Deepak]]

list_1 = [1,2,3,"Python",[1,2,["Python", "Java"],"Language"]]
print(list_1[4])
print(list_1[4][2])
print(list_1[4][2][0])
print(list_1[4][2][0][2])
append()-tis method is used to ad new items into list,it will go only for the last index of the list.

systax---> variable_name.append(item)

extend()--->this method is used to add items to list in the last index, where each item or substring is each index in the list.
remove()--->this method will remove or delete the item or valu directly pop.
pop()--->this method will delete the item or value based on index position.

mutable---> i can directly modify on that particular variable
immmutable---> i can not modify directly on the variable

list_2=[1,2,3,4,5]
print(list_2)
list_2.append(67)
print(list_2)
list_2.append(679)
print(list_2)

list_3 = [23,56,89,6]
list_3.append("Deepak")
list_3.extend("Deepak")
print(list_3)

list_4 = [23,"python",56,89,6]
list_4.remove("python")
print(list_4)'''
list_4 = [23,"python",56,89,6]
list_4.pop(1)
print(list_4)











