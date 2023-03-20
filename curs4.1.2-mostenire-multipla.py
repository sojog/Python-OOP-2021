class Parent:
    def __init__(self):
        print ("parent")

class Left(Parent):
    def __init__(self):
        super().__init__()
        print ("left-derived-parent")

class Right(Parent):
    def __init__(self):
        super().__init__()
        print ("right-derived-parent")

class Child(Right, Left):
    def __init__(self):
        super().__init__()
        print ("child")



child = Child()