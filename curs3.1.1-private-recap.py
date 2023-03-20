#########################################
## Definirea clasei
class Human: 
    #Constructorul Clasei 
    def __init__(self, name, gender, cnp):
        #variabila publica
        self.name = name
        #variabila interna sau protected
        self._gender = gender
        #variabila privata
        self.__cnp = cnp
#########################################

#Crearea unei clase
aHumanObject = Human('Silviu', 'M', 'xxxxxxxxxxx')

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