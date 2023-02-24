# Duck Typing

# "If it's look like a duck, swims like a duck, and quack like a duck, then it probably is a duck

# We dont care whether the object is a duck or not
# We only care if it behaves like a duck or not

# Ex:
# If there is an object which is "IDE" and it has a method "execute", thats it.
# It doesn't matter which class object it is

class PyCharm:
    def execute(self):
        print("Compiling & Running")

class MyIDE:
    def execute(self):
        print("Spell check")
        print("Compiling & Running")

class Laptop:
    def run_code(self,ide):
        ide.execute()

#Using PyCharm
ide1 = PyCharm()
lap1 = Laptop()
lap1.run_code(ide1)

#Using MyIDE
ide2 = MyIDE()
lap2 = Laptop()
lap2.run_code(ide2)

#Both PyCharm and MyIDE have a method "execute", then it probably it's an IDE