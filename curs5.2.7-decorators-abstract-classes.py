#Abstract Base Classes (ABCs)
import abc
from abc import ABC, abstractmethod 


class Animal(ABC): 
    @abstractmethod
    def move(self):
        pass

    @abc.abstractproperty 
    def hair(self):
        pass

    def varsta(self):
        return 0


    

class Mamifer(Animal):
    pass

class Human(Animal):
    def move(self):
        print("I can walk and run") 
    
    @property
    def hair(self):
        return True


    # @abc.abstractproperty 
    # def gender(self):
    #     pass

class Snake(Animal): 
    @property
    def hair(self):
        return False
    

class Boa(Snake):
    def move(self):
        print("I can crawl") 
    


class Dog(Animal): 
	def move(self): 
		print("I can bark") 

class Lion(Animal): 
	def move(self): 
		print("I can roar") 


# Nu se poate initializa un animal
anObject = Boa()
# anObject = Human()
print(anObject.hair)
print(anObject.varsta())