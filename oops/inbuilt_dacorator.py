# --------@classMethod-------------
class jello:
   a = 20
   name = "rajat"

   def __init__(self, b, c):
       self.b = b
       self.c = c

   def show(self):
       print(self.b, self.c)

   @classmethod
   def a_update(cls, c):
       cls.c = c


obj = jello(10, 20)
obj2 = jello(30, 40)
jello.a_update(2222)  #update value of a everywhere
obj.show()
obj2.show()
print(jello.a)



#---------staticmethod------
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(9, 8)
print(result)

#-------withstaticmethod

class demo:
    def hello(h):
        print(h)

demo.hello =staticmethod(demo.hello)
demo.hello("rajat")

#-----------@pr0perty--------------
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Setting the person_name() function as a property using the @property decorator.
    @property
    def person_name(self):
        return self.name

if __name__ == "__main__":
    Jack = Person("Jack", 26)
    print("The name of the Person is:", Jack.person_name)


#-------setter------------
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Setting the person_name() function as a property using the @property decorator.
    @property
    def person_name(self):
        return self.name

    # Setting the person_name() as a setter decorator.
    @person_name.setter
    def person_name(self, new_name):
        self.name = new_name

if __name__ == "__main__":
    Jack = Person("Jack", 26)
    print("The old name of the Person is:", Jack.person_name)

    new_name = "Jack Sparrow"
    # modifying the name of the Person.
    Jack.person_name = new_name

    print("The new name of the Person is:", Jack.person_name)
