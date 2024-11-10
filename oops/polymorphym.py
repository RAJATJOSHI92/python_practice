#------------------

class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(self.name,self.age)
class B(A):
    def __init__(self,name,age,height):
        super().__init__(name,age)
        self.height=height
    def show(self):
        print(self.name,self.age,self.height)
p1=A("joshi",30)
p=B("rajat",23,183)
p.show()
p1.show()


#--------------------

class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("class A")

class B(A):

    def show(self):
        print("class B")

class C(A):

    def show(self):
        print("class C")

a=A("rajat",23)
b=B("joshi",24)
c=C("indian",25)

for x in (a,b,c):
    print(x.name)
    print(x.age)
    x.show()