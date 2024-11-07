"""A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression."""

#-------BASIC-------------------#

y=lambda x:x*5
print(y(5))


y= lambda x,y,z:x+y+z
print(y(2,3,4))

y= lambda x,y:x*y
print(y(3,5))

#---------with fucnction-----#

def function(n):
    return lambda x:x*n

y=function(5)
z=function(6)
print(y(11))
print(z(11))

