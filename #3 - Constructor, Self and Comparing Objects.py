# Constructor, Self and Comparing Object

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def compare(self,other):
        if self.age > other.age:
            print(self.name,"is older than",other.name)
        elif self.age < other.age:
            print(self.name,"is younger than",other.name)
        else:
            print("They are same age")

h1 = Human('Navin',28)
h2 = Human('Penk',18)

h1.compare(h2)  #Result : Navin is older than Penk


