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

class Animal:

    __hungry = "Yes" # private attributes
    __name = "No name"
    __owner = "No owner"

    def __init__(self):
        pass

    def __del__(self):
        pass

    def set_owner(self, newOwner):
        self.__owner = newOwner
        return

    def get_owner(self):
        return self.__owner

    def set_name(self, newName):
        self.__name = newName
        return

    def get_name(self):
        return self.__name

    def noise(self):
        print('errr')
        self.__hiddenmethod()
        return

    def __hiddenmethod(self): # a way to encapsulate a method
        print ("Hard to find")

def main():
    dog = Animal()

    dog.set_owner('iolia')
    print dog.get_owner()

    #print dog.__owner # error

    dog.noise()

    #dog.__hiddenmethod() # error

if __name__ == '__main__': main()

