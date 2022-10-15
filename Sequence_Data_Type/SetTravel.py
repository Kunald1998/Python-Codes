print("Demonstration of Set sequence data type.")

# data = Hetrogenous
# Ordered = No
# Indexed = No
# Mutable = Yes
# Duplicate = No

data = {11,21,51,101,11,21,151,121} # Duplicate
data1 = {11,90.12,True,"Hello"} #Hetrogenous

print("Output using for-each loop:")
for no in data:
    print(no,end=" ")
print("")

# Below for loop is not allowed. because it contains index.
# Set data type does not have index due to this we can not use for loop with the index.
# data[index_number] this is not allowed.

"""print("Output using for with index:")

for i in range(0,len(Data),1):
    print(Data[i],end=" ")
print("")

print("Output using while loop: ")
i = 0
while(i < len(Data)):
    print(Data[i],end = " ")
    i+=1
print("\n__________")"""


