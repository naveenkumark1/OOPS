# Types of Variable in Python

# There are 2 types of variable in OOP:
# 1. Instance variable
# 2. Class (Static) Variable

# namespace is an area where you create and store object/variable

class Smartphone:
    OS = 'Android'  #This is class variables

    def __init__(self,ram,storage):
        self.ram = ram  #This is instance variables
        self.storage = storage  #This is instance variables

    def show(self):
        print("OS :",self.OS, ", RAM :",self.ram, ", Storage :",self.storage)

sp1 = Smartphone(3,32)
sp2 = Smartphone(4,64)

sp1.show()  # Result : OS : Android , RAM : 3 , Storage : 32
sp2.show()  # Result : OS : Android , RAM : 4 , Storage : 64

#Change the variable:
sp1.storage = 64     #It will only change for sp1 object
Smartphone.OS = "iOS"   #It will change for all object

sp1.show()  # Result : OS : iOS , RAM : 3 , Storage : 64
sp2.show()  # Result : OS : iOS , RAM : 4 , Storage : 64