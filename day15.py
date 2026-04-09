'''
lambda function()
--> this is also called anonymous functions
--> a lambda function can take n number of arguments but have only one expression

systax
-------
        lambda (keyword) arguments : expression


any = lambda so ,some : so + some
print(any(6,10))

some = lambda an, how, do :(how - an)* do
print(some(4,9,2))

some = lambda an, how, do :(how + an)* do
print(some(3,5,7))

some = lambda an, how, do :(how *an)* do
print(some(6,9,11))

some = lambda an, how, do :(how /an)* do
print(some(12,15,19))

list comprehension:
-------------------
--> this is offers the shorter systax when you want tp create a new list from the existing list

systax
------
         variable_name = [expression loop and condition]
'''
old_list = [1,2,3,4,5]
even_list = [j for j in old_list if j%2==0]
odd_list = [j for j in old_list if j%2!=0]
print(even_list,odd_list)
