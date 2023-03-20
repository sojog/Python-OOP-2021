class Student:
    def __init__(self, cursuri):
        self.cursuri = list(cursuri)
        self.note = dict()

    def add_new_course (self, curs):
        self.cursuri.append(curs)
        return Student(self.cursuri)
    
    def __add__(self, curs_nou):
        self.cursuri.append(curs_nou)
        return Student(self.cursuri)
    
    def __str__(self):
        str_cursuri = ""
        for curs in self.cursuri:
            str_cursuri = str_cursuri + curs.nume_curs 
        return  "Lista cursuri:" + str_cursuri

class Curs:
    def __init__(self, nume_curs, departament = "Python"):
        self.nume_curs = nume_curs
        self.departament = departament
    def __eq__(self, alt_curs):
        print(self.nume_curs)
        print(alt_curs)
        return self.nume_curs ==  alt_curs.nume_curs
    

curs1 = Curs("PY_POO")
curs4 = Curs("PY_POO", "Python")
curs3 = Curs("PY_POO", "Java")
curs2 = Curs("PY_Fundamentals")


student = Student([])
student = student.add_new_course(curs1)
# print(student)

student = student + curs1
print(student)





