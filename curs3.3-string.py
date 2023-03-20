#########################################
class Person:
    
    def __init__(self, firstname, lastname):
        #variabila publica
        self.firstname = firstname
        #variabila privata
        self.lastname = lastname
   
    def show (self):
        print (f"Person: {self.firstname} {self.lastname}")
    
    def __str__(self):
        return f"Person: {self.firstname} {self.lastname}"

class Student(Person):
    def __init__(self, firstname, lastname, indexnumber):
        super().__init__(firstname, lastname)
        self.indexnumber = indexnumber 

    def show (self):
        print (f"Student: {self.firstname} {self.lastname} {self.indexnumber}")
        super().show()

aPerson = Person("John", "Doe")
aPerson.show()
print(aPerson)


aStudent = Student ("Joe", "Doe", 1232143)
aStudent.show()
print(aPerson)