class A:
    def __init__(self):
        self.b = "hello" 
        self.c = "another hello"    
    def __str__(self):
        return "ceva"

class B(A):
    pass


obj =  B()
print(obj)


# bool_value_variable = hasattr(obj,'a')
# print(bool_value_variable)

# bool_value_variable = hasattr(obj,'b')
# print(bool_value_variable)

# istrue = isinstance(obj, A)
# print(istrue)

# istrue = type(obj) is A
# print(istrue)



# #Returneaza toate atributele si metodele unui obiect intr-o lista
print(dir(obj))

#Returneaza toate varibilele unei obi instantiat, intr-un dictionar 
#print(vars(obj))