#------------Basic-------------------#

array=["rajat","joshi","indian"]

#--------------
x=array[0]
print(x)
#---------------
array[0]="Rajat"
x=array[0]
print(x)
#---------------
array.append("canadian")
print(array)
#-----------------
array.pop(1)
print(array)

#--------------------
array.remove("indian")
print(array)

array.sort()
print(array)

del array