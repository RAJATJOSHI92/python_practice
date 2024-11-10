class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print(self.a,self.b)

obj1=A("rajat","joshi")
obj1.show()


#---------------multiple inheritence-------
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print("class A called")
        print(self.a,self.b)


class B:
    def show1(self):
        print("class B called")

class C(A,B):
    def show2(self):
        print("class c called")



obj1=C("rajat","joshi")
obj1.show()
obj1.show1()
obj1.show2()


#-----------------super()---------------
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print(self.a,self.b)
class B(A):
    def __init__(self,aa,bb):
        self.aa=aa
        self.bb=bb
        super().__init__("rajat","joshi")

    def show1(self):
         print(self.aa,self.bb)

obj1=B("indian","canadian")
obj1.show()
obj1.show1()


#--------------adding prperties--------
class A:
    def __init__(self,aa,b):
        self.a=aa
        self.b=b
    def show(self):
        print(self.a,self.b)
class B(A):
    def __init__(self ,ab,b,c):
        self.a=ab
        self.b=b
        self.c=c
        super().__init__(ab,b)


    def show1(self):
         print(self.a,self.b,self.c)

obj1=B("rajat","joshi","123")
obj1.show()
obj1.show1()
