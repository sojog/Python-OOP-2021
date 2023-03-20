#Abstract Base Classes (ABCs)
import abc
from abc import ABC, abstractmethod 

class Trainable(ABC):
    @abstractmethod
    def train(self):
        pass


class Animal(ABC): 
    @abstractmethod
    def move(self):
        pass

    @abc.abstractproperty 
    def hair(self):
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
	def move(self): 
		print("I can crawl") 

class Dog(Animal): 
	def move(self): 
		print("I can bark") 

class Lion(Animal): 
	def move(self): 
		print("I can roar") 


# Nu se poate initializa un animal
# anObject = Animal()
anObject = Human()
print(anObject.hair)