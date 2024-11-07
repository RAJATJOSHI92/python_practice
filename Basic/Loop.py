#----------------looping---------------#
list={"rajat","joshi","indian"}


for x in list:
    if x=="joshi":
        break
    print(x)


for x in list:
    print(x)
    if x=="joshi":
        break

for x in list:
    if x=="joshi":
        continue
    print(x)

for x in range(1,20,3):
    print(x)

for x in list:
    print(x)
else:
    print("finished")