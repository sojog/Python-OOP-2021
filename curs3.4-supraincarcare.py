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
    def __init__(self, firstname = None , lastname = None, indexnumber = None):
        super().__init__(firstname, lastname)
        self.indexnumber = indexnumber 

    def show (self):
        print (f"Student: {self.firstname} {self.lastname} {self.indexnumber}")
        super().show()
    
    def __str__(self):
        return f"Person: {self.firstname} {self.lastname} {self.indexnumber}"



aStudent1 = Student ("Joe", "Doe", 1232143)
aStudent2 = Student("Joe", "Doe")
aStudent3 = Student("Joe")
aStudent4 = Student()

print(aStudent1)
print(aStudent2)
print(aStudent3)
print(aStudent3)