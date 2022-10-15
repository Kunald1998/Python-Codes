print("Demonstration of String sequence data type.")
# PROPERTIES OF LIST DATA TYPE.
# data = Heterogeneous eg. kunald988@gmail.com
# Ordered = Yes
# Indexed = Yes
# Mutable = No  eg. String[11] = "P" this gives TypeError: 'str' object does not support item assignment.
# Duplicate = Yes


String = "Marvellous Infosystems"

print(String)
print(type(String))
print("Accessing the data from string using index: ",String[11])
print("Accessing the data from string using index: ",String[-11])


for i in String:
    print(i," ",end="")
print("")
for i in range(0,len(String),1):
    print(String[i]," ",end="")
print("")
