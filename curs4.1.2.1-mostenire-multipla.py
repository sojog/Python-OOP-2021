class Parent(object):
    def __init__(self):
        #super(Parent, self).__init__()
        print ("parent")
    

class Left(Parent):
    def __init__(self):
        #super(Left, self).__init__()
        #super(Left, self).__init__()
        super().__init__()
        print ("left-derived-parent")

class Right(Parent):
    def __init__(self):
        #super(Right, self).__init__()
        super().__init__()
        print ("right-derived-parent")

class Child(Right, Left):
    def __init__(self):
        #super().__init__()
        super(Left, self).__init__()
        #Left.__init__()
        print ("child")



child = Child()