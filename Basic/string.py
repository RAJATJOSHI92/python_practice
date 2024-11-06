# --------multiline--------#
x='''jfhedocndiovhn ocndlcjdc dc
ndld
nd;
dm'd;
dm'
dwc'''

print(x)

#----with for loop---#
s="rajat"
for i in s:
    print(i)
    #print(i,end="")

    #------with array------#
s1="rajat"
print(s1[1])

#-----length find-----#
r="rajat"
print(len(r))

#--------find word in string------#

s="rajat"
if "jaa" in s:
    print("yes it is available")
else:
    print("not  available")

print("ja" in s)  # return boolean


s="rajat"
if "jaa"not in s:
    print("yes not  available")
else:
    print("it is  available")


#---slicing string------#

s="rajat"
print(s[2:4])

print(s[:4])

#-----negative slicing------#

print(s[-4:-2])


#  upper, lower, replace,split,stripe method------#


s="    rajat , joshi    "
print(s.upper())
print(s.lower())
print(s.replace("r","R"))
print(s.split(","))
print(s.strip())


#----concat------#

s="rajat"
s1="joshi"
print(s+s1)
print(s+" "+s1)
print(s)

#------f string -----#
s=23
print(f"rajat age is {s}")

print(f"float number is {s:.2f}")


#------ some useful methods------#

s="rajat"
print(s.capitalize())
print(s.endswith("t"))
print(s.find("at"))
print(s.islower())
print(s.isupper())
print(s.count("a",0,2))
print(s.count("a"))


#-------boolean-------#


s="rajat"
if s.endswith("t"):
    print("it is lower")
else:
    print("not lower")

 #--------operator-------@

if 2>3:
    print("greater")
else:
    print("not greater")

print(5**3)

x=5
x**=3
print(x)

