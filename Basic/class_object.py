#---------------creating class-----------------#
class A:
    print("rajat")
p=A()

print(p)  # refer to address

class A:
    x=5
p=A()
print(p.x)


class A:
    def __init__(self,name,age):
       self.name=name
       self.age=age
       print("age is :",self.age," "+" Name  is :"+self.name)

p=A("rajat",23)
print(p.name,p.age)



class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
p=A("rajat",24)
print(p)


#-------with function--------------#

class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
         print(self.name,self.age)
p=A("rajat",25)
p.show()



#---------modify,delete---------------#
class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
p=A("rajat",25)
p.age=26
p.show()

#---------------------
class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
p=A("rajat",25)
del p.age
p.show()


del p


