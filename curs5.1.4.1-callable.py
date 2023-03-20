class Document:
    def __init__ (self, title, author):
        self.__title = title
        self.__author = author 
        self.__is_published = False

    def __str__(self):
        is_pub = " " if self.__is_published else " nu " 
        return "Documentul <<" + self.__title + ">> de catre " + self.__author + is_pub + "este publicat"

    def __call__(self):
        self.__is_published = not self.__is_published

doc = Document("Cum sa inveti Python", "Silviu Ojog")
print(doc)

## Callable inseamna chemarea lui ca pe o functie
doc()
print(doc)

doc()
print(doc)
    



