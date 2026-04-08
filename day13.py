'''
functions()
---> this a block of code which is reuseable.
-->two types 1Bulit-in or In-bulid
             2.User define
Bulit-in or In-bulid
-->they comes with program and those are already defined...
eg..
---- print(), sum(), map().....

User define
-->  this is created by person who is developing or using for development
Note:
---> it's starts with keyword follwed by func name
---> and it has calling func...
systax:
        def fun-name(): parameters
           ......
           ........
           ........
           ........
        func_name() ..... arguments

'Even Number Using Functions'

a=int(input("enter the number:"))
def even(a):
   if a%2 == 0:
      print(f"{a} is even number")
   else:
      print(f"{a} is odd number")
even(a=2)


'Prime Numbers Using functions'

prime_num = 7
count = 0
def prime_check(num,k):
    for j in range (1,num+1):
        if num % j == 0:
            k += 1
    if k == 2:
        print("prime")
    else:
        print("not")
prime_check(prime_num,count)
'''

a = [3,4]
b = [3,4]
c = b
print(id(c), id(b))
print(c is b)
