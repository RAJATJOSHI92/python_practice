class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)

class B(A):
    pass

p=A("rajat",32)
p.show()
p1=B("joshi",33)
p1.show()

#-----------------------------

class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(self.name,self.age)
class B(A):
    def __init__(self,name,age):
        A.__init__(self,name,age)

p=B("rajat",24)
p.show()

#-----------------------------
class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(self.name,self.age)
class B(A):
    def __init__(self,name,age):
      super().__init__(name,age)
      self.height=183
p=B("rajat",23)
print(p.height)


#------------------------------
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
p=B("rajat",23,183)
p.show()

