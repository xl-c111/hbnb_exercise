# Classes: 3 conpartments
"""
1, a reactangle with 3 compartments: 
top compartment: class name, 
middle compartment: class's attributes(characteristics of objects); 
bottom compartment: class's operations (behaviors of class)

Class Name

+ Attribute 1 : Type
+ Attribute 2 : Type
- Attribute 3 : Type
- Attribute 4 : Type

+ Operation 1(arg list): return
+ Operation 2(arg list): return
- Operation 3(arg list): return
- Operation 4(arg list): return
(+: public; -: private; #: protected)

2, class without last two compartments called =simple class. 

Class Name

"""

# Interface: a special type that defines a set of operations(methods) that classes must implement

"""
top compartment: interface’s name with the label <<Interface>> at the top
second compartment: operations (methods) that classes must implement, but no attributes (interface only defines operations, not attributes)

<<Interface>>
interface's name 


+ doMethod(String) : void (a method named doMethod, takes a string as argument, returns void)
+ init(boolean, long) : boolean (a method named init, takes a boolean and a long as arguments, returns a boolean)

"""
# Difference between class and interface
"""
class: defines what and how, can have attributes (states) and methods (behaviors)
interface: defines what must be done, not how, and can only have operations (methods)

class for concrete implementation and installation;
interface for abstraction and flexibility
"""


# class diagram relationships

# Association: regular connection, no ownership (solid arrow)

from abc import ABC, abstractmethod
class Student:
    def __init__(self, name):
        self.name = name


class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []      # Association

    def add_student(self, student):
        self.students.append(student)


s1 = Student("Alice")
t1 = Teacher("Mr. Wang")
t1.add_student(s1)
print([student.name for student in t1.students])  # ['Alice']
"""
1, The Teacher has an association with Student, but the Student does not belong to the Teacher. 
There is only a reference.
2, Classes are linked but independent, lifetime is not tied. 
e.g., Teacher knows Students, but does not own them.
"""


# Inheritance: child class extends parent class (solid line, hollow triangle)
class Animal:
    def speak(self):
        print("Animal speaks")


class Cat(Animal):
    def speak(self):
        print("Meow")


cat1 = Cat()
cat1.speak()     # Meow
"""Cat is a subclass of Animal and inherits its behavior. It can also override the method."""


# Realization/Implementation: class implements an interface (dashed line, hollow triangle)
class AnimalBehavior(ABC):
    @abstractmethod
    def eat(self):
        pass


class Dog(AnimalBehavior):   # Implements interface
    def eat(self):
        print("Dog eats bone")


dog1 = Dog()
dog1.eat()      # Dog eats bone
"""Dog implements all the methods of the AnimalBehavior interface"""


# Dependency: temporary usage, not structural (dashed arrow)
class PaymentGateway:
    def pay(self, amount):
        print(f"Paying {amount} dollars")


class OrderService:
    def place_order(self, payment_gateway, amount):
        # Dependency on PaymentGateway
        payment_gateway.pay(amount)


pg = PaymentGateway()
os = OrderService()
os.place_order(pg, 100)        # Paying 100 dollars
"""
OrderService only depends on PaymentGateway temporarily, such as for method arguments 
or local variables. It's not a structural relationship.
"""


# Aggregation: whole-part, weak ownership (hollow diamond)
class Player:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []      # Aggregation

    def add_player(self, player):
        self.players.append(player)


# A player can belong to multiple teams, and can exist without a team.
p = Player("Tom")
team = Team("Tigers")
team.add_player(p)

for player in team.players:
    print(player.name)       # Tom
"""
Whole-part relationship, the part can exist independently. 
Team aggregates Player. A player can exist independently of a Team.
"""


# Composition: whole-part, strong ownership (solid diamond)
class Room:
    def __init__(self, name):
        self.name = name


class House:
    def __init__(self):
        self.rooms = [Room("Living Room"), Room("Bedroom")]     # Composition


h = House()
print([room.name for room in h.rooms])    # ['Living Room', 'Bedroom']
"""
Room exists only within House. If House is destroyed, the rooms are destroyed as well
"""
