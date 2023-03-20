class Produs:
    def __init__(self, price):
        self.__price = price
        
    
    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if (type(new_price) is int) and (new_price > 0):
            self.__price = new_price

    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price):
        if (type(new_price) is int) and (new_price > 0):
            self.__price = new_price

    @price.deleter
    def price(self):
        #If want to totally delete it use del
        #del self.__price
        #Or otherwise, to make the value None:
        self.__price = None


prod = Produs(200)
print(prod.price)


#Setter


# #Traditional getter
print(prod.get_price())

# #Traditional getter
prod.set_price(50)

# #Traditional getter
print(prod.get_price())

print(prod.price)

# #Deleter
del prod.price

#Setter
print(prod.get_price())

#Getter
print(prod.price)