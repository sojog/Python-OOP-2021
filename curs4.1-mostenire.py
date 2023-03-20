#########################################
## Definirea unei clase de baza
class Angajat: 
    #Constructorul Clasei 
    def __init__(self, name, salariu):
        #variabila publica
        self.name = name
        #variabila interna sau protected - folosite pentru a incapsula informatia
        self._salariu = salariu
    
    def plataImpozite (self):
    	return  self._salariu * 25 / 100

    #Conceptul de overloading (supraîncărcarea)
    # Functia poate fi chemata in 2 moduri:
    #       object.salariuPerOra ()
    #       object.salariuPerOra (40) 
    def salariuPerOra (self, oreLucrate = 40):
    	return self._salariu / oreLucrate 
#########################################


#########################################
## Definirea unei clase derivate (mostenite/copil)
class AngajatIT(Angajat): 
    #Constructorul Clasei 
    def __init__(self, name, salariu, reducere):
        #Chemarea constructorului din clasa de baza
        super().__init__(name, salariu)
        self.__reducere = reducere
    	
        
    	
        
    #Conceptul de overriding (suprascriere)
    #Functionalitatea a fost schimbata in clasa derivata, dar ea se cheama in acelasi fel
    #        baseObject.plataImpozite ()
    #        childObject.plataImpozite () 
    def plataImpozite (self):
    	return  self._salariu * (25 - self.__reducere) / 100 


    
#########################################


#Crearea unei obiect de tip Angajat
angajat = Angajat('Silviu', 2000)
impozite = angajat.plataImpozite()
print (impozite)

salariuPerOra =  angajat.salariuPerOra()
print (salariuPerOra)



#Crearea unei obiect de tip AngajatIT
angajatIT  = AngajatIT('Silviu', 15000, 25)

impozite = angajatIT.plataImpozite()
print (impozite)

salariuPerOra =  angajatIT.salariuPerOra()
salariuPerOra20 =  angajatIT.salariuPerOra(20)
print (salariuPerOra)




