# Operator Overloading

# If you want to perform any operation on the objects,
# you have define all these method by yourself

class Student:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def __add__(self, other):   #define add method by yourself
        m1 = self.n1 + other.n1
        m2 = self.n2 + other.n2
        m3 = Student(m1,m2)
        return m3

s1 = Student(90,85)
s2 = Student(70,95)
s3 = s1 + s2    #behind the scenes : Student.__add__(s1,s2)
print(s3.n1)