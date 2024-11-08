"""
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
You can define as many exception blocks as you want.
"""
#--------------try/except with else and finally
try:
    print(x)
except:
    print("variable not defined")

#-------------------multiple except
try:
    print(x)
except NameError:
    print("variable not definedddd")
except:
    print("something else happened")

try:
    print(x)
except NameError:
    print("variable not definedddd")
else:
    print("something else happened")


try:
    print(x)
except NameError:
    print("variable not definedddd")
finally:
    print("something else happened")

#----------raise exception matually

x=-1
if x<0:

    raise Exception("x is less than 0")

s="rajat"

if not type(s) is int:
    raise TypeError("no integer defined")


