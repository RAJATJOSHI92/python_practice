class A:
    def __init__(self):
        self.a="Inside A"
    def show(self):
        print(self.a)
class B(A):
    def __init__(self):
        super().__init__()
        self.a="Inside B"


    def show(self):
        print(self.a)

obj1=A()
obj2=B()
obj1.show()
obj2.show()

#--------------------with multiple--------------

class A:
    def show(self):
        print("class A method")
class B:
    def display(self):
        print("class B method")
class C(A,B):
    def show(self):
        A.show(self)    #----------calling parent method
        super().show()   #----------calling parent method
        print("class C method")
obj1=C()
obj1.display()
obj1.show()

#--------------------mutilevel with method overloading---------------
class A:
    def display(self):
        print("class B method")
class B(A):
    def show(self,a):
        self.a=a
        print("class A method",self.a)
class C(B):
    def show(self ,a,b):
       self.a=a
       self.b=b
       print("class C method",self.a,self.b)

obj1=C()
obj1.display()
obj1.show(23,34)

obj2=B()
obj2.show(333)
