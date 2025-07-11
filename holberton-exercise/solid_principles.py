# Single Responsibility Principle(SRP):
"""
each class should only do one thing

e.g., a class EmailSender should only be responsible for sending emails
"""

# Open/Closed Principle (OCP)
"""
add new features by extending the code, not by modifying existing code 

e.g., Suppose you have a Shape class. To support a new shape, like Triangle,
you create a new Triangle class that extends Shape, instead of changing the Shape class
"""

# Liskov Substitution Principle (LSP):
"""
subclass shoule be able to replace the parent class

e.g., If you have a function that uses a Bird class, you should be able to pass a Sparrow
without breaking the function. 
“pass a Sparrow” means providing a Sparrow subclass instance as the parameter to a function
that was originally designed to accept a Bird object.
"""


class Bird:
    def fly(self):
        print("I can fly!")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying!")


def let_bird_fly(bird):
    bird.fly()


bird = Bird()
let_bird_fly(bird)    # I can fly!

sparrow = Sparrow()
let_bird_fly(sparrow)  # Sparrow flying!


# Interface Segregation Principle (ISP)
"""
Interfaces should be small and specific, not forcing classes to implement unnecessary methods 

e.g., If you have an interface Printer, don’t include methods like scan() and fax() if some
printers only need to print. Separate them into smaller interfaces.

"""

# Dependency Inversion Principle (DIP)
"""
Depend on abstractions; details depend on abstractions

e.g., A PaymentService class depends on a PaymentMethod interface, not on a specific class like
CreditCardPayment. You can switch payment methods easily by implementing the same interface.

"""
