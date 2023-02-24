# Constructor in Inheritance

# Method Resolution Order (MRO) = It will execute/goes from left to right

# When you create object of subclass, it will call init of subclass first
# If there is no init of subclass, it will call init of superclass

# super() will call something from superclass

class A:
    def __init__(self):
        print('In init A')

    def f1(self):
        print('Feature 1-A working')

class B:
    def __init__(self):
        print('In init B')

    def f1(self):
        print("Feature 1-B working")

class C(A,B):   #A is in the left, B in the right ... Remember MRO
    def __init__(self):
        super().__init__()  #It will call init from class A, not B
        print('In init C')

    def feat(self):     #It will call f1 from class A, not B
        super().f1()

obj = C()   #In init A
            #In init C
obj.f1()    #Feature 1-A working