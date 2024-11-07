""""
Set items are unordered, unchangeable, and do not allow duplicate values.

"""
#-------------basic--------------#
set={1,2,3,4,5,6}
print(set)

set={1,2,3,4,"rajat",False,0}   #0 and false is considered same
print(set)

print(len(set))

print(type(set))


""" thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)"""


#-----------------------accessing set--------------#
set={1,2,3,4,5,6}
print(set)

for x in set:
    print(x)


print(1 in set)

print(1 not in set)

#--------------------adding ---------------#
set={1,2,3,4,5,6}
set.add(11)
print(set)

set={1,2,3,4,5,6}
set2={7,8}
set2.update(set)
print(set2)

#-----------removing--------------#

set={1,2,3,4,5,6}
set.remove(4)
print(set)

set={1,2,3,4,5,6}
set.pop()
print(set)

set={1,2,3,4,5,6}
set.discard(4)
print(set)

set={1,2,3,4,5,6}
del set
print(set)

#---------------looping-----------#
set={1,2,3,4,5,6}
print(set)

for x in set:
    print(x)


#-----------------join------------#
set={1,2,3,4,5,6}
set2={1,4,7,8,9}
set3=set.union(set2)
print(set3)


set={1,2,3,4,5,6}
t=(1,4,7,8,9)
set3=set.union(set2)    # other data tyoe
print(set3)

