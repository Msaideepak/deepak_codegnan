'''
Polymorphism
------------
--> this allow a object of different classes to be created as instance of the same base class
    with method behaving diffeerently based on the actual object type.
Eg...
print(len("python"))
print(len("[1,2,3]))


Method Overloding
-----------------
--> this define multiple methods with the same name but different parameters
    (number, type, or order) in the same class

class calculator:
    def add(self, a, b=0, c=0):
        return a+b+c
cal= calculator()
print(cal.add(2))
print(cal.add(3,4))
print(cal.add(5,7,8))

class calculator:
    def add(self, a, b=0, c=0):
        return a-b-c
cal= calculator()
print(cal.add(2))
print(cal.add(3,4))
print(cal.add(5,7,8))

Method overriding
-----------------
--> this occurs in the child class, redefining a parent class method with the same signature for runtime.

class animal:
    def speak(self):
        return "sound"
class dog(animal):
    def speak(self):
        return "woof"
dog = dog()
print(dog.speak())

class animal:
    def speak(self):
        return "sound"
class cow(animal):
    def speak(self):
        return "moo"
cow = cow()
print(cow.speak())

Operator overloding
-------------------
--> this is customizes operator like +, - for user-defined classes by implementing special methods..
Eg... __add__, __sub__

class someone:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return someone (self.a +other.a, self.b + other.b)
    def __str__(self):
        return f"({self.a}, {self.b})"
any = someone(2,3)
so = someone(5,9)
print(any + so)


class someone:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __add__(self, other):
        return someone (self.a +other.a, self.b + other.b , self.c +other.c)
    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"
any = someone(2,3,4)
so = someone(5,9,11)
print(any + so)

Data Abstraction
--------------
--> this hides compelx implementation details, exposing only essential features via abstract class or interface.
'''
from abc import ABC, abstractmethod
class shape (ABC):
    @abstractmethod
    def area(self): 
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2
circle = circle(5)
print(circle.area())
    










