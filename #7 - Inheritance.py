# Inheritance

# There are 3 different type:
# - Single level inheritance
# - Multi level Inheritance
# - Multiple Inheritance

#This is single level inheritance:
class A:    #This is superclass
    def f1(self):
        print("Feature 1 working")

class B(A):     #This is subclass, will include methods from class A
    def f2(self):
        print("Feature 2 working")

#This is Multi level Inheritance:
class C:    #This is superclass
    def f3(self):
        print("Feature 3 working")

class D(C):     #This is subclass, will include methods from class C
    def f4(self):
        print("Feature 4 working")

class E(D):     #This is subclass, will include methods from class C and D
    def f5(self):
        print("Feature 5 working")

#This is Multiple Inheritance:
class F:    #This is superclass
    def f6(self):
        print("Feature 6 working")

class G:    #This is superclass
    def f7(self):
        print("Feature 7 working")

class H(F,G):   #This is subclass, will include methods from class F and G
    def f8(self):
        print("Feature 8 working")


