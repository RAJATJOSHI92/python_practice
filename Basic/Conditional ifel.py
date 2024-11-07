#--------------short if---------#
a=10
b=20
print( "a is greater" if a > b    else "b is greater" )

print("a") if a>b else print("B")



#-----------------short else if------------#
a=2
b=10

print("a") if a>b else print("=") if a==b else print("b")


#----------------and ,or ,not-----------------#
a=2
b=10

if not a > b:
    print("b is greater")
else:
    print("a is greater")

a=2
b=10
c=45

if a>b and a>c:
     print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater")

a=2
b=10
c=45

if a>b or a>c:
    print("a is greater")
elif b>a or b>c:
    print("b is greater")
else:
    print("c is greater")


#--------------------pass---------------#
a=2
b=10
if a>b:
    pass
