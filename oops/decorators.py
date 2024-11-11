"""
Decorators in Python are functions that takes another function as an argument
and extends its behavior without explicitly modifying it.
"""

def hello():
    print("this is hello")

variable=hello   #assigning function to variable
hello()
variable()



def passing(hh):
    hh()
    hh()
def hello():
    print("hello")

passing(hello)  # passing funtion as a argument



def return_to_upper():
    return str.upper

to_upper = return_to_upper()

print(to_upper("scaler topics"))


# returning function from function without parameter
def returntofuntion():
    def inner():
        print("inner called")
    return  inner
ss =returntofuntion()
ss()


#------------ returning function from function with parameter

def returntofuntion(message):
    def inner():
        print("inner called a "+message)
    return  inner
ss =returntofuntion("rajat")
ss()
ss1 =returntofuntion("joshi")
ss1()


#--------------Decorators function with parameters


def dacorator(fun):
    def inner():
        print("hello")
        fun()
        print("hello1")
    return inner

def hello():
    print("inner")

s1=dacorator(hello)
s1()

#----------------Syntactic Decorator
def dacorator(fun):
    def inner():
        print("hello")
        fun()
        print("hello1")
    return inner

@dacorator
def hello():
    print("inner")

hello()

#---------------closure function-----
def f1(x):
    def f2(y):
        return x + y
    return f2

adder = f1(12)
print(adder(4))