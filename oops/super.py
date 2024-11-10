class Animal:
    def __init__(self):
        self.legs=4
        self.mammal=True
        self.Domestic=True
        self.Tail=True

    def ismammal(self):
         if self.mammal:
             print("it is mammal")
    def isDomestic(self):
         if self.Domestic:
             print("it is Domestic")
    def isTail(self):
         if self.Tail:
             print("it is Tail")
class Dog(Animal):
    def __init__(self):
        super().__init__()
    def ismammal(self):
        super().ismammal()
class Horses(Animal):
    def __init__(self):
        super().__init__()
    def haslegsandtail(self):
        if self.Tail and self.legs==4:
            print("has legs and tail")
obj=Dog()
obj.ismammal()
obj2=Horses()
obj2.ismammal()
obj2.haslegsandtail()


#---------------with multiple------

class Mammal:
    def __init__(self,name):
        print(name,"is mammal")
class canfly(Mammal):
    def __init__(self,canfly):
        print(canfly,"can fly")
        super().__init__(canfly)
class canswim(Mammal):
    def __init__(self,canswim):
        print(canswim,"can swim")
        super().__init__(canswim)
class Animal(canswim,canfly)   :
    def __init__(self,name):
        super().__init__(name)
oo=Animal("dog")


#-------------------multilevel super------
class Mammal:
    def __init__(self,name):
        print(name,"is mammal")
class canfly(Mammal):
    def __init__(self,canfly):
        print(canfly,"can fly")
        super().__init__(canfly)
class canswim(canfly):
    def __init__(self,canswim):
        print(canswim,"can swim")
        super().__init__(canswim)
class Animal(canswim):
    def __init__(self,name):
        super().__init__(name)

oo=Animal("Dog")