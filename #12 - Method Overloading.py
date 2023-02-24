# Method Overloading

# Method Overloading = Two methods in the same class with the same name
#                      but different parameters or arguments

class Student:
    def sum(self, a=None, b=None, c=None):  #default value is None if parameter unfilled
        if a != None and b != None and c != None:
            return a+b+c
        elif a != None and b != None:
            return a+b
        else:
            return a

obj = Student()
print(obj.sum(5,4,3))
print(obj.sum(5,4))
print(obj.sum(5))

