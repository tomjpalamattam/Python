#class and constructor
class Person:
    def __init__(self,name):  #constructor
        self.name= name
    def talk(self):
        print(f"Hi my name is {self.name}")


john=Person("John Smith")
bob=Person("Bob Dilan")
john.talk()
print(john.name)
bob.talk()
