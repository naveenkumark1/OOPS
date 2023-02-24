# Types of Methods

# Instance method (works with instance variable, use (self))
    # Accessor method
    # Mutator method

# Class method (works with class variable, use(cls), use @classmethod)

# Static method (works without instance variable and class variable, use @staticmethod)

class Student:
    school = 'BINUS'

    def __init__(self,n1,n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    #This is instance method:
    def avg(self):
        print("The average scores :",(self.n1 + self.n2 + self.n3) / 3)

    #This is class method:
    @classmethod
    def get_school(cls):
        print("I studied at",cls.school)

    #This is static method
    @staticmethod
    def info():
        print("This is Student Class")

s1 = Student(90,85,95)
s2 = Student(100,75,90)

s1.avg()    #call instance method
Student.get_school()    #call class method
Student.info()  #call static method

