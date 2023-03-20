#########################################
class Human:
    # Variabila statica
    GENDERS = ["M", "F", "UNKNOWN"]
    __ADULT_AGE = 18

    def __init__(self, name, gender, cnp):
        
        #variabila publica
        self.name = name

        #variabila interna
        if gender in Human.GENDERS:
            self._gender = gender
        else:
            self._gender = "UNKNOWN"

        #variabila privata
        self.__cnp = cnp
    
    def is_adult (self):
        # Incepand cu 2002     
        return int(self.__cnp[1:3]) > 2

    def public_method(self):
        print("Accesarea metodei publice: " + self.name)

    def _internal_method(self):
        print("Accesarea metodei interne: " + self._gender)

    def __private_method(self):
        print("Accesarea metodei private: " + self.__cnp)


    def another_public_method (self):
        #pot sa acesez privata pentru sunt in interiorul clasei (in corpul clasei)
        self.__private_method()

class Man(Human):
    def new_method(self):
        pass

    def public_method(self):
        return "Altceva"

human = Human("George", "M", "195hkdsahdka")
human.is_adult()
human.public_method()

man = Man("Andrei", "M", "409409232")
man.is_adult()
man.new_method()
man.public_method()


class Student(Human):
    def student_public_method(self):
        print("Accesarea metodei publice: " + self.name)

    def student_internal_method(self):
        print("Accesarea metodei interne: " + self._gender)

    def student_private_method(self):
        ##### -> nu mai pot accesa self.__cnp -> este in exteriorul clasei
        print("Accesarea metodei private: " )  #+ self.__cnp
        # self.__cnp apartine clasei de baza, nu clasei derivate

    
#######################################
# Aici se termina corpul clasei 
#########################################


#Crearea unei clase
aHumanObject = Human('Silviu', 'M', '190xxxxxxxx')

aStudentObject = Student('Silviu', 'M', '190xxxxxxxx')



print (aHumanObject.is_adult())


#Acesarea unei metode publice
aHumanObject.public_method()
#Acesarea aceleasi metode publice dintr-o clasa derivata
aStudentObject.public_method()
#Acesarea unei metode publice
aStudentObject.student_public_method()



#Acesarea unei metode interne
aHumanObject._internal_method()

#Acesarea unei metode interne dintr-o clasa derivata
aStudentObject._internal_method()

#Acesarea unei metode interne a clasei derivate
aStudentObject.student_internal_method()




#Acesarea unei metode private
# ----> EROARE ---> aHumanObject.__private_method()


#Acesarea unei metode private
aHumanObject.another_public_method()
#Acesarea unei metode private dintr-o clasa derivata
aStudentObject.another_public_method()
#Acesarea unei metode private dintr-o clasa derivata
aStudentObject.student_private_method()


#Accesarea unui atribut public din clasa
print(aHumanObject.name)

#Accesarea unui atribut intern din clasa
#Este posibil, dar nu este dezirabil (Nu pentru asta este facut)
print(aHumanObject._gender)


#Accesarea unui atribut privat din clasa
#Este imposibil, si indezirabil (Nu pentru asta este facut) 
#print(aHumanObject.__cnp)    #Genereaza eroare


#Functioneaza dar nu este de dorit
#!!!!!!!!!!!!!!!!!!!!!!!!!!
print(aHumanObject._Human__cnp)
#!!!!!!!!!!!!!!!!!!!!!!!!!!