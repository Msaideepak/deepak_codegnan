'''
constructor(__init__)
---------------------
-->a computer is a special method used to initiallize object data__init__()

class student:
    def __init__ (self, name, id):
        self.name = name
        self.id = name

    def display(self):
        print(self.name, self.id)
stu_1 = student("deepak", 123)
stu_1.display()

Access Specifiers
-----------------
1.public --> systax -- name,, we can use it anywhere in the program

2.protected --> systax -- _name,, this is only for internal use

3.private --> systax -- __name,, this one is restricted

'''
class some:
    def __init__(self):
        self.public = "public"
        self.protected = "_protected"
        self.private = "__private"
any = some()
print(any.public)
print(any.protected)
print(any.private)
