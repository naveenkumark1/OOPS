# Method Overriding

# Method Overriding = Two methods in different class with same name and same parameters or argument

class A:
    def show(self):
        print('In A show')

class B:
    def show(self):
        print('In B show')

obj = A()
obj.show()  #In A show

obj2 = B()
obj2.show() #In B show