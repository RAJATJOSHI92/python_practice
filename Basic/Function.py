#-------------------creating --------------#

def function():
    print("rajat")

function()  # calling


def function(name):          # single argument
    print("name is "+name)
function("rajat")
function("joshi")
function("indian")

def function(fname,lname):      # double argument
    print("first name is "+fname,"\n"+"last name is "+lname)

function("rajat","joshi")

#---------*args--------------#

"""f you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.
"""

def function(*name):
    print(name[0])

    print(name[1])

function("rajat","joshi","indian")


#----------keyword argument-----------#

def function(name1,name2,name3):

     print(name1)
     print(name2)
     print(name3)

function(name1="rajat",name2="joshi",name3="indian")

#--------**keyword argument-------------#
"""If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.
"""

def function(**names):
    print("First name is "+names["fname"])
    print("Last name is "+names["lname"])

function(fname="rajat",lname="joshi")


#--------default  parameter-------------#

def function(name="rajat"):
    print("MY NAME IS " +name)

function("joshi")
function("indian")
function()      # default


#---------passinf list as argument---------#


def function(name):
    print(name)
    for x in name:
        print(x)


list={"rajat","joshi"}
function(list)



#------------return value------------------------#

def function(a):
    return a*a
print(function(5))


#----------------pass keyword--------------------#

def function():
    pass
print("rajat")

function()