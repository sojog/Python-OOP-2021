import re

#Aici construim o clasa Exceptie 
class ImproperNameException(Exception):
    def __str__ (self):
        return "ImproperNameException"
    def __init__(self, name, message="The provided name is wrong: "):
        self.message = message + name
        super().__init__(self.message)


class User:
    __contor_id = 0
    def __init__(self, name, email, telephone_nr):
        self.__contor_id = self.__contor_id + 1
        self.id = self.__contor_id

        if type(name) == str:
            if len(name) <= 3:
                raise Exception("Name should be more than 3 characters.")
            else:
                pattern = re.compile(r'([a-zA-Z])\D*([a-zA-Z])$')
                print(pattern.match(name))
                if pattern.match(name):
                    self.name = name
                else:
                    raise ImproperNameException(name)
                
        else:
            print("The name must be a string")
            raise TypeError
            

        self.email = email
        self.telephone_nr = telephone_nr

try:
    elvis = User("Elvis99", "email@gmail.com", 12313123)
except ImproperNameException as ex:
    print(ex)
    print(ex.__class__)
    print(ex.__str__)
except TypeError:
    print("Type Error")
except Exception as ex:
    print(ex)




try:
    dragos = User("Elvis", "email@gmail.com", 12313123)

except:
    print("User error")
