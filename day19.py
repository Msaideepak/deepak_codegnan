'''
Encapusalation
--------------
--> the principle of bunding data (Attributes) andmethods that
operate on that data into a single unit, which is a class

class bankac:
     def __init__(self, balance):
         self.__balance = balance
         
     def deposite(self, amount):
          self.__balance += amount
          
     def get_balance(self):
         return self.__balance
         
acc = bankac(15000)
acc.deposite(7000)
print(acc.get_balance())


   
acc = bankac(15000)
acc.deposite(7000)
print(acc.get_balance())

# Masking the Adhaar number for security

class BankAccount:
    def __init__(self, balance, adhaar_card):
        self.__balance = balance
        self.__adhaar_card = adhaar_card  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def get_balance(self):
        return f"Current Balance: {self.__balance}"

    def get_adhaar(self):
        
        return f"Adhaar Card: {'XXXX-XXXX-' + str(self.__adhaar_card)[-4:]}"


acc = BankAccount(15000, 123456789012)
acc.deposit(7000)

print(acc.get_balance())
print(acc.get_adhaar())

inheritance
-----------
--> this allows a child class (sub class) to acquire the attributes and methods
    of a parent class (base class) this is called inheritance
    
1.single inheritance --> using single method of the class from base class is know as single

2.multiple .inheritance --> a child class inherits from more than one parent class..

super()
------
--> this is used to call methods of the parents class from the child class


class parent:
    def display(self):
        print("this is parent method")
class child(parent):
    def display(self):
        super().display()
        print("this is child method")
obj = child()
obj.display()

'''
class father:
    def skill_1(self):
        print("father: hard working")

class mother:
    def skill_2(self):
        print("mother: cooking")

class child(father, mother):
    def all_skills(self):
        print("child: coding")

any = child()
any.skill_1()
any.skill_2()
any.all_skills()
    







