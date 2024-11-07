"""Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc."""


#---------BAsic----------#
t=(1,2,3,4)
print(t)

print(len(t))
t=(1,2,3,"rajat",4,4,4,4)
print(t)

t=(1)   # this is int type
t1=(1,) # this is tuple
print(type(t),type(t1))


t=tuple((1,2,3,4,5,6,11,"rrr"))   #   use tuple constructor but use two extra braces
print(t)


#-----------accessing tuple--------------#
t=(1,2,3,4)
print(t)

for x in t:
    print(x)

print(t[1])
print(t[:3])
print(t[:-2])


#---------------updating -----------#
t=(1,2,3,4)
t2=(5,6,7)
t3= t+t2
print(t3)

t=(1,2,3,4)
t2=(5,6,7)

y=list(t)  # conveting to list
print(y)
y.append(t2)
t=tuple(y)
print(t)



t=(1,2,3,4)
y=list(t)
y.remove(4)
t=tuple(y)
print(t)


#-----------assigning value to variable----------------#

t=(1,2,3)
(a,b,c)=t
print(f"a={a} b={b} c={c}")

t=(1,2,3,4)
(a,b,*c)=t
print(f"a={a} b={b} c={c}")

#-----------------multiply tuple------#
t=(1,2,3,4)
y=t*2
print(y)


#------methods-------#
t=(1,2,3,4,3)
print(t.count(3))


t=(1,2,3,4,3)
print(t.index(3))   # return first appearing value in tuple
