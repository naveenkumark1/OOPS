# The __init__ Method

# __init__ is similar to constructors in C++ and Java
# Usages : to initialize (assign value) to the data member of the class when an object of class is created

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hi, my name is",self.name, "and I'm",self.age,"old!")

# Create an object:
human1 = Human("Navin",28)
human2 = Human("Penk",18)

human1.greeting()
human2.greeting()