''''
Operators
different type of operators
conditional statememt-->if,elif,nested if
'''
'''Operators-->An operator is a symbol that perform an
operator on one or more values (operands) and produces a result

operators are primarily used :
-->Caculate values
-->Compare values/ inputs
-->Make decisions
-->Control the progam flow

There are major seven categories of operators in python

-->Arithmetic Operators
-->Assigement Operators
-->Membership Operstors
-->Identity Operstors (in,out in)
-->Bitwise Operators
-->Logical operators (and,or,not)


#Aritmetic Operators -->Arithmetic operators perform mathematical operat:

# + -->Addition,- -->Subtraction , * -->Mulitiplication, / -->Division
# ** -->Exponent,% -->Modules ,//Integer Divison

a=5
b=3
print(a+
print(a-b)
print(a*b)
print(a/b) #returns the result in float values
print(a**b) #returns the exponential value

print(a%b) #Modules division -->returns remainder
print(a//b) #Floor / Intger Division -->returns Quotient discards float

#f-string notation
num1 =int(input("Enter the frist values:"))
num2 =float(input("Enter the second value:"))
result =(num1 + num2)*4
print("The result is",result) #standard notation

#f-string notation
print(f'The result is {result}')
print(f'The result of {num1} and {num2} is {result},{num1*num2}')


#Asssigement Operators 
#--> =Assign, +=Addtion Assigement ,
#-= -->Subtract Assigement,*=,/=,%=,//=,**=

#They are majorly used fir code repetitions in application usage

a= 4
b = 3
a +=2 #--> a = a+2
print(a)
b +=a
print(b)
#in similar way check for -=, *=, **=,/=, %=, //=

b -= 3 #b = b-3
print(b)
print(f'The updated values  of a and b are {a} and {b}')
b *= a # b =b*a
print(b)


#Relational or Compersions opetrators -->They always return the boolean
#values (True /False)

# == is equal to, !=not equal to
# < less than, > greater thsn, >= , <=

a = int(input("Enter a value:"))
b = int(input("Enter the value:"))
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

#Membership operators -->They check for the existance of an object in a
#collection --> in,not in

a = "codegnan"
print(type(a))
print('a' in a)
print('z' in 'deepak')
print('z' not in 'codegnan')

b = [12,6,3,4]
c =int(input("Enter the vaule"))
print(c)
print(c in b)
print(c not in b)


#Logical operators -->They are used to combine multiple conditions
#and,or,not

age = int(input("Enter the age:"))
vote_right =True
print(age>18 or vote_right)
print(age>18 or vote_right)
print(not vote_right)


#Identity Operators -->They check the/compare the memory location and validate we use
#(id) fuction it is different from == operator --> is , is not

a = [1,2,4]
b = [1,2,4]
print(a == b)
print(id(a))#returns the identity of an object
print (id (b))
print (a is not b)

c = b
print(c) #assigning b to c
print(id(c)) #then b and c have same memory locations
print(c is b) #return true because b,c have the same memory locaton
'''
 
#bitwise operators -->
print(5 & 3)
print(5 / 3)






