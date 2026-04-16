'''
oop's
-----
--> object-oriented language (oop) is a style of programming where we model
    real-world things as objects that contain both data and functions()
--> reusable of code
-->and also scalable

class
-----
--> class is a bule-print or template that define what kind of data behavior
    a certain type of object will have

object
------
--> instance of class or an object is a real instance created from a class.
    is is the actual thing taht exists in memory while the program run


class car:
     pass
car1 = car()
            >---->objects
car2 = car()

attributes
----------
--> these are variables that store data related to a class or object

class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
car_1 = car("toyata", "white")
car_2 = car("thar", "red")
print(car_1.brand)

class Dog:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
dog_1 = Dog("Labrador", "Golden")
dog_2 = Dog("Pug", "Black")
print(dog_1.breed)


class Cat:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

cat_1 = Cat("Siamese", "Cream")
cat_2 = Cat("Persian", "White")

print(cat_1.breed)


class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

fruit_1 = Fruit("Apple", "Red")
fruit_2 = Fruit("Banana", "Yellow")
fruit_3 = Fruit("Grape", "Purple")
fruit_4 = Fruit("Orange", "Orange")
fruit_5 = Fruit("Kiwi", "Green")
print(fruit_1.name)
'''
class Food:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

food_1 = Food("Pizza", "Italian")
food_2 = Food("Sushi", "Japanese")

print(food_1.name)







