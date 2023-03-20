class Library:
    menu = [
        "1. Add new book.",
        "2. Modify the details of the book.",
        "3. Delete a book.",
        "4. List all books.",
        "5. Exit program."
    ]

    lista_carti = []

    def show_menu(self):
        for item in self.menu:
            print(item)
    
    def add_new_book(self, book):
        self.lista_carti.append(book)

    def list_all_books(self):
        for book in self.lista_carti:
            print(book)

    def remove_book(self,book):
        self.lista_carti.remove(book)


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return  self.name


class Roman(Book):
    def __init__(self, name, nr_volume):
        super().__init__(name)
        self.nr_volume = nr_volume
   

class Lucrare_stiintifica(Book):
    def __init__(self, name, revista):
        super().__init__(name)
        self.revista = revista


class Manual(Book):
    def __init__(self, name, materie):
        super().__init__(name)
        self.materie = materie

    def __str__(self):
        return  self.name + " " + self.materie

class Author:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Multiple_authors(Author):
    def __init__(self, authors):
        name  = ""
        for author in authors:
            name += author.name
        super().__init__(name)
        self.authors = authors

class Unknown_author(Author):
    def __init__(self):
        super().__init__("Author unknown.")


baltagul = Roman("Baltagul", 2)
abcdar  = Manual("ABCDAR", "romana")
lucrareStiintif = Lucrare_stiintifica("Blockchain", "Science Magazine")
biblia = Book("Biblia")

tolkien = Author("Tolkien")
jerome = Author("Jerome")
rebreanu = Author("Rebreanu")
necunoscut = Unknown_author()
mai_multi = Multiple_authors([tolkien, jerome, rebreanu])
print(tolkien)
print(necunoscut)
print(mai_multi)

    

#Obiect de tip Library
libraria_Eminescu = Library()

libraria_Eminescu.add_new_book(biblia)
libraria_Eminescu.add_new_book(baltagul)
libraria_Eminescu.add_new_book(lucrareStiintif)
libraria_Eminescu.add_new_book(abcdar)
libraria_Eminescu.list_all_books()

# libraria_Eminescu.show_menu()
# 
# libraria_Eminescu.remove_book("Test")
# print("############")
# libraria_Eminescu.remove_book(biblia)
# libraria_Eminescu.list_all_books()

