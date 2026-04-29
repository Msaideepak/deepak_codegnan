'''
import re
def validate_name(name):
    pattern = r'^[A-Za-z]{3,}$'
    return re.fullmatch(pattern, name)

def validate_email:
    pattern = r'^[\W\.-]+@[\w\.-]+\.\w+$'
    return re.fullmatch(pattern, email)

def validate_phone(phone):
    pattern = r'^[0-9]{10}'
    return re.fullmatch(pattern, phone number)

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern, password)

def main():

    name = input("enter name:")
    email = input("enter email:")
    phone = input("enter phone number:")
    password = input("enter password:")

def main():

    elif not validate_name(name):
        print("Invalid name")
    elif not validate_email(email):
        print("Invalid email")
    elif not validate_phone(phone):
        print("Invalid phone number")
    elif not validate_password(password):
        print("Invalid password")
    else:
        print("all inputs are valid from submitted sucessfully")


why this need?
--------------
--> this is crictical because it  converts raw data into actionable insights, enabling information to
    decision-making easy and improve operational efficiency...

1.Decision-Making
2.Improve Operational Efficiency
3.Customer Understanding
4.Market Insight
5.Risk Management
6.Data-Driven Strategies

Line plot
---------
import matplot.pyplot as pit
X = [1,2,3,4]
Y = [10,20,15,25]
pit.plot(X,Y)
pit.show()


Bar graph
----------
import matplotlib.pyplot as pit
pit.bar(["A","B","C"],[4,10,7])
pit.show()

pie graph
---------
import matplotlib.pyplot as pit
pit.pie([35,15,50,], labels = ["sandeep","deepak","saikumar"])
pit.show()

Histogram
---------
import matplotlib.pyplot as pit
pit.hist([23,15,78,12])
pit.show()

Numpy
-----
--> Numpy (numerical python) these the foundational open-source libary for scientfic computing in python,
providing high-performace, N-diensional array ojects (ndarray)
--> this enables efficent numerical computation linear algebra, and data manipulation, serving as the basis
   for tools like tensorflow and scipy

import numpy as np
arr = np.array([1,2,3])
print(arr+1)

import numpy as np
arr = np.array([1,2,3])
print(arr-1)

Pandas
------
--> this pandas is used for handling structure data in a table format
'''
import pandas as pd
data = {"name" : ["deepak","sandeep"], "marks" : [40,79]}
any = pd.DataFrame(data)
print(any)






        









