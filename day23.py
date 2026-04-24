'''
Handling Errors
---------------
Try block --> the try block will test a block of code errors.
try:
    print(b)
    
Except block --> this block will take of any errors
except:
    print("this block can handle error")
    
Else block --> else keyword to define a block of code of code to be excuted if no errorwere raised.
try:
    a = 9
    b = 10
    print(a+b+c)
except:
    print("error here")
else:
    print("no error in the code")

Finally block --> this block will execute either try block have any error or no error
try:
    a = 9
    b = 10   
    print(a+b)
except:
    print("error here")
else:
    print("no error in the code")
finally:
        print("the try-except bolck is finished")
'''
try:
    num = int(input("enter a number: "))
    num_2 = int(input("enter a number: "))
    result = num / num_2
except valueerror:
    print("pls enter a valid number")
except zerodivisionerror:
    print("cannot divide by zero")
else:
    print(f"result = {result}")
finally:
    print("progam is completed")

