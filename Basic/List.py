#-------accessing list-----#

list=[1,2,3,4,"rajat"]

print(list)
print(list[4])
print(list[0:4])
print(list[-4:-1])
print(list)

#-------changing list-----#

list=[1,2,3,4,"rajat"]
list[0]="joshi"
print(list)

list[0:3]=["water","melon"]
print(list)


#----------add items-----------#

mylist = ['apple', 'banana', 'cherry']
mylist2=[1,2,3]

mylist.append("watermelon")
print(mylist)
mylist.insert(0,"rajat")
print(mylist)
mylist.extend(mylist2)
print(mylist)


mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')     # works with index
print(mylist[1])


mylist = ['apple', 'banana', 'cherry']
tuple=(1,2,3,4)
mylist.extend(tuple)      #append any type of object
print(mylist)



fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)


#---------------removing itenms-----------#
mylist = ['apple', 'banana', 'cherry',1,3,2]
mylist2 = ['apple', 'banana', 'cherry',1,3,2]

mylist.remove(1)
print(mylist)
mylist.pop(1) # works with index
print(mylist)
mylist2.pop()  # remove all list
print(mylist2)
mylist2 = ['apple', 'banana', 'cherry',1,3,2]
del mylist2[0]
print(mylist2)
del mylist2


#--------looping---------#

mylist = ['apple', 'banana', 'cherry',1,3,2]

for x in mylist:
    print(x)

for x in range(len(mylist)):
    print(mylist[x])
mylist = ['apple', 'banana', 'cherry',1,3,2,4]
[print(x) for x in mylist]


#------------list comprehensive---------------#
mylist = ['apple', 'banana', 'cherry',1,2,3]
mylist2=[ x for x in mylist]
print(mylist2)

mylist2=[ x for x in mylist if x!="apple"]
print(mylist2)


mylist2=[x for x in mylist]
print(mylist2)


mylist2=[x if x != "banana" else "orange" for x in mylist]
print(mylist2)

#--------------------sorting-----------------#
mylist = [5,1,2,3]

mylist.sort()
print(mylist)

mylist.sort(reverse=True)
print(mylist)

mylist.reverse()
print(mylist)


#------------copy,join --------#
mylist = [5,1,2,3]
x=mylist.copy()
print(x)


mylist = [5,1,2,3]
list2=["rrrr","ffff"]
list3= list2+mylist
print(list3)


for x in mylist:
    list2.append(x)
print(list2)

mylist = [5,1,2,3]
list2=["rrrr","ffff"]
list2.extend(mylist)
print(list2)


