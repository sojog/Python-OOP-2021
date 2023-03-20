class A:
    def __init__(self):
        self.b = "hello"     
    def someFunction(self):
    	pass

    def __str__(self):
        return "Ce scrie aici!"

class B(A):
    pass


obj =  A()

#Returneaza toate atributele si metodele unui obiect intr-o lista
print(dir(obj))

print(obj.__class__)

print(obj.__class__.__name__)

print("Module: " + obj.__class__.__module__)

print(obj.__dict__)

print(obj.__str__)
print(obj.__str__())

# # obj.__sizeof__ este o metoda
print(obj.__sizeof__)
# # apelarea metodei se face  obj.__sizeof__()
print(obj.__sizeof__())


print("is callable")
print(callable(obj))


# # Function introspection
print(obj.someFunction.__name__)
print(obj.someFunction.__code__)
print(obj.someFunction.__module__)




