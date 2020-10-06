"""
class Animal:

    hungry = "Yes"
    name = "No name"
    owner = "No owner"

    def __init__(self):
        pass

    def set_owner(self, newOwner):
        self.owner = newOwner
        return

    def getOwner(self):
        return self.owner

    def noise(self):
        print('errr')
        return

def main():
    dog = Animal()

    dog.set_owner('iolia')
    print dog.getOwner()

    print dog.owner # no encapsulation

if __name__ == '__main__': main()
"""

__metaclass__ = type

class Animal:

    __name = "No name"
    __owner = "No owner"

    def __init__(self, **kvargs):
        self._attributes = kvargs

    def set_attributes(self, key, value):
        self._attributes[key] = value
        return

    def get_attributes(self, key):
        return self._attributes.get(key, None)

    def noise(self):
        print('errr')
        return

    def move(self):
        print('The animal moves forward')
        return

    def eat(self):
        print('Crunch, Crunch')
        return

class Dog(Animal):

    def __init__(self, **kvargs):
        super(Dog, self).__init__()
        self._attributes = kvargs

    def noise(self):
        print("Woof, woof")
        Animal.noise(self)
        return

class Cat(Animal):
    def __init__(self,
                 **kvargs):
        super(Cat, self).__init__()
        self._attributes = kvargs

    def noise(self):
        print ('Meow')
        return

    def noise2(self):
        print('Purrr')
        return

class Dat(Dog, Cat): # whichever class is listed first, is going to be the class method that is going to be used in instances where both of the classes inherited have a method with the same name

    def __init__(self, **kvargs):
        super(Dat, self).__init__()
        self._attributes = kvargs

    def move(self):
        print('Chases Tails')
        return

def playWithAnimal(Animal):
    Animal.noise()
    Animal.eat()
    Animal.move()
    print(Animal.get_attributes('__name'))
    print(Animal.get_attributes('__owner'))
    print '\n'
    Animal.set_attributes('clean', 'Yes')
    print(Animal.get_attributes('clean'))

def main():
    """bruno = Dog(__name = 'Bruno', __owner = 'iolia')
    kiwi = Cat(__name = 'Kiwi', __owner = 'spongebob')
    playWithAnimal(bruno) # polymorphism
    playWithAnimal(kiwi)"""

    """japhie = Dat(__name = 'Japhie', __owner = 'iolia')
    japhie.move()
    japhie.noise()
    japhie.noise2()
    print japhie.get_attributes('__name')"""

    kiwi = Cat(__name = 'Kiwi', __owner = 'spongebob')
    print issubclass(Cat, Animal)
    print Cat.__bases__
    print kiwi.__class__
    print kiwi.__dict__


if __name__ == '__main__': main()

