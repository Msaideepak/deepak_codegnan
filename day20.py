'''
Multilevel-inhertance
---------------------
--> this occurs when a class inherits from a child class, creating a
    grandparent--> parent --> child in this structure.

class grandparent:
    def show_grandparent(self):
        print("i'm grandparent")
        
class parent(grandparent):
    def show_parent(self):
        print("i'm parent")

class child(parent):
    def show_child(self):
        print("i'm child")
any = child()
any.show_grandparent()
any.show_parent()
any.show_child()


class Employee:
    def employee(self):
        print("Employee Name: UMP")
class Manager(Employee):
    def manager(self):
        print("He manages the work")
class TeamLead(Manager):
    def teamlead(self):
        print("The Team lead will guide the work and assign the work")

var = TeamLead()
var.employee()
var.manager()
var.teamlead()

Hierchical-inhertance
---------------------
--> this occurs when mutiple child classes inherit from a single parent class
    this process is called Hierchical

class parent:
    def parent_(self):
        print("I am parent")
class child_1(parent):
    def child_2(self):
        print("I am 1st child")
class child_2(parent):
    def _child(self):
        print("I am 2nd child")
class child_3(child_1, child_2):
    def child(self):
        print("I am the child")

thing = child_3()
thing.parent_()
thing._child()
thing._child()
thing.child()
'''
class parent:
    def parent_(self):
        print("I am parent")
class child_1(parent):
    def child_2(self):
        print("I am 1st child")
class child_2(parent):
    def _child(self):
        print("I am 2nd child")
class child_3(child_1, child_2):
    def child(self):
        print("I am the child")

class parent:
    def parent_(self):
        print("I am parent")
class child_1(parent):
    def child_2(self):
        print("I am 1st child")
class child_2(parent):
    def _child(self):
        print("I am 2nd child")
class child_3(child_1, child_2, parent):
    def child(self):
        print("I am inherited from parent class and child_1, child_2")

thing = child_3()
thing.parent_()
thing.child_2()
thing._child()
thing.child()


