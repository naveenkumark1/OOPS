# Inner Class

class Student:  #This is Outer Class
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.smartphone = self.Smartphone()

    def show(self):
        print("My name :",self.name,",",self.age,"years old")
        self.smartphone.show()

    class Smartphone:   #This is Inner Class
        def __init__(self):
            self.brand = "Asus"
            self.storage = "1TB"
            self.ram = "16GB"

        def show(self):
            print("Smartphone specification :",self.brand,self.storage,self.ram)

s1 = Student("Penk",18)
sp1 = Student.Smartphone()

s1.show()

