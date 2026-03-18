'''
Variables-->Variables is basically named storage location that is used to data in the memory,to make it simple it is the label which points out to a value -->storage placeholders
SyntaxError: invalid syntax
Rules for defining variables
SyntaxError: invalid syntax
-->A-Z,a-z,0-9
SyntaxError: invalid syntax
-->start with uppercases,lowercase letters,even with a uderscore _
SyntaxError: invalid syntax
-->But you cannot start with symbols (@,#,$...),even number aslo
                                      
SyntaxError: invalid syntax
Better preferable way is go with general purpose -->you want to store your details name,email,account_number..
                                      
SyntaxError: invalid syntax
'''
a=1
b=2
a=25
#python is dyamically typed you need not define the data type and also
#only the recent value to the variable with same name is pointed

print(a)
print(b)

#1a23 =25 #Syntax Error

#@werf =4.5 #Syntax Error

#$dsf =12 #Invaild error
#Store your personal details

name = "Codegnan"
location ="Viskhapatnam"
age = 7
emailid = "cmo@codegnan.com"
email_id ="cmo@Codegnan.com"
print(name,location,age,email_id)

#How to assign multiple values to a variables
akash,praneeth,ajay=21,20,22
print (akash)
print (praneeth)
print (ajay)
#assign same value to mutliple varaibles

x =y =z =21
print (x,y,z)

#keywords are reserved words which will have specific uaage/meaning
#There are 35 keywords in Python
#never usekeywords as Identifiers

#if =23
#lambda ='deepak'
#False = 0 #cannot assign

#python is case-senstive
false =25

#literals are names given to variables ,functions,classes,objectives...

#literals are fixed values to a identifers
name =25

#name is Identifiers,25 is literal

#Single line comments --> #
#Multi line comments --> #start end with triple quotes
#Bulit-in Datatypes -->numeric,boolean,collection
#Numeric datatypes -->int,float,complex
#int -->count,values,quantities
#float -->temperature,percentage,price
#complex -->specific conversation (real and imaginary)

count =40
print(count)
print(type(count))

price =175.25
print(price)
print(type(price))

j3 =25
value =2+j3
print(value)
print(type(value))
#Typecasting -->converting onr type to another

#int -->float,complex

age =25
print(type(age))

b =float(age)
print(b)
print(type(b))
c =complex(age)
print(c)
print(type(c))

#float,complex
price =275.25
print(type(price))
d =int(price)
print(d)




