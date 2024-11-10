class A:
    def __init__(self, a):
        self.a = a
    def __add__(self, other):

         return  self.a + other.a
obj1=A(2)
obj2=A(3)
obj3=A("rajat")
obj4=A("joshi")

print(obj1+obj2)
print(obj3+obj4)
print(A.__add__(obj1,obj2))
print(A.__add__(obj3,obj4))
print(obj1.__add__(obj2))
print(obj3.__add__(obj4))



#--------------------
class Complex:

    def __init__(self, a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return self.a+other.a,self.b+other.b

obj1=Complex(1,2)
obj2=Complex(3,4)
print(obj1+obj2)

print(obj1.__add__(obj2))
print(Complex.__add__(obj1,obj2))