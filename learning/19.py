#class and inheritance
class Mammals:
    def __init__(self, carnivore, herbivore, age):
        self.carnivore=carnivore
        self.herbivore=herbivore
        self.age=age

    def find_type(self):
        if (self.carnivore==True):
            print('The animal is carnivore')
        elif (self.herbivore==True):
            print('The animal is herbivore')
        else:
            print('The animal is not defined')

class Dogs(Mammals):
    def bark(self):
        print('I am a dog and i bark')
        print(f"The Dog is of age {self.age}")
arjun=Mammals(True,False,13)
kummananna=Mammals(False,True,11)
Tom=Mammals(False,False,25)
jimmy=Dogs(True,False,22)
arjun.find_type()
kummananna.find_type()
Tom.find_type()
print(Tom.carnivore)
jimmy.find_type()
jimmy.bark()

